"""
Update OSM data
"""

import tempfile
import requests
import pathlib
import zipfile
import subprocess
import overpy
import json
import argparse
import atexit

CR_ZIP_URL='http://download.geofabrik.de/europe/czech-republic-latest-free.shp.zip'
OVERPASS="http://overpass-turbo.eu/"

DATA_DIR = None

def _clean():

    if DATA_DIR:
        shutil.rmtree(DATA_DIR)

atexit.register(_clean)

def download_osm():

    tempdir = tempfile.mkdtemp()
    fn = "cech-republic-latests-free.zip"
    fp = pathlib.Path(tempdir, fn)
    r = requests.get(CR_ZIP_URL, stream=True)

    with open(fp, "wb") as out:
        for chunk in r.iter_content(chunk_size=128):
            out.write(chunk)

    zf = zipfile.ZipFile(fp)
    zf.extractall(path=tempdir)
    return tempdir

def _update_ogr2ogr(source, destination, where=None):

    cmd = ["ogr2ogr", "-f", "GeoJSON"]
    if where:
        cmd.append("-where")
        cmd.apend(where)
    cmd.append(destination)
    cmd.append(source)
    subprocess.run(["ogr2ogr", "-f", "GeoJSON", destination, source])


def _update_overpass(query, destination):

    api = overpy.Overpass()
    bbox = [48.5227428999999972, 12.0223825000000009,
            51.0917286000000033, 18.8873178000000017]

    # fetch all ways and nodes
    result = api.query(airport_query)
    geojson = {"type": "FeatureCollection", "features": []}
    for way in result.get_ways():
        if "iata" not in way.tags or not way.tags["iata"]:
            continue
        geojson["features"].append({
            "type": "Feature",
            "properties": way.tags,
            "geometry": {
                "type": "Point",
                "coordinates": [float(way.nodes[0].lon), float(way.nodes[0].lat)]
            }
        })

    for relation in result.get_relations():
        first_member = relation.members[0]
        if isinstance(first_member, overpy.RelationWay):
            lon, lat = float(way.nodes[0].lon), float(way.nodes[0].lat)
        else:
            lon, lat = float(first_member.lon), float(first_member.lat)
        geojson["features"].append({
            "type": "Feature",
            "properties": relation.tags,
            "geometry": {
                "type": "Point",
                "coordinates": [lon, lat]
            }
        })
    with open(destination, "w") as out:
        json.dump(geojson, out)

def _update_transport(data_dir, target_dir):
    fn = "gis_osm_railways_free_1.shp"
    source = pathlib.Path(data_dir, fn)
    destination = pathlib.Path(target_dir, "rail.geojson")
    _update_ogr2ogr(source, destination)

    fn = "gis_osm_roads_free_1.shp"
    destination = pathlib.Path(target_dir, "highway.geojson")
    source = pathlib.Path(data_dir, fn)
    _update_ogr2ogr(source, destination, "fclass like 'motorway%'")

    fn = "gis_osm_roads_free_1.shp"
    destination = pathlib.Path(target_dir, "primary.geojson")
    source = pathlib.Path(data_dir, fn)
    _update_ogr2ogr(source, destination, "fclass like 'primary%'")

    fn = "gis_osm_roads_free_1.shp"
    destination = pathlib.Path(target_dir, "secondary.geojson")
    source = pathlib.Path(data_dir, fn)
    _update_ogr2ogr(source, destination, "fclass like 'secondary%'")


    destination = pathlib.Path(target_dir, "airports.geojson")
    query = """
        [out:json][timeout:25];
        (relation["iata"]({bbox}); node["iata"]({bbox}); way["iata"]({bbox}););
        out body;
        >;
        out skel qt;
    """.format(bbox=",".join([str(x) for x in bbox]))
    _update_overpass(query, destination)


    destination = pathlib.Path(target_dir, "ferry.geojson")
    ferry_query = """
        [out:json][timeout:25];
        (node["amenity"="ferry_terminal"]({bbox}););
        out body;
        >;
        out skel qt;
    """.format(bbox=",".join([str(x) for x in bbox]))
    _update_overpass(query, destination)


def update(target, source):
    if not source:
        source = download_osm()
        global DATA_DIR
        DATA_DIR = source

    _update_transport(source, target)

def main():
    parser = argparse.ArgumentParser(description='Get fresh copy of OSM (mainly transport) data')
    parser.add_argument('--target', type=str, required=True,
                        help='name of target directory')
    parser.add_argument('--source', type=str, required=False,
                        help='name of source directory (with downloaded and unzipped OSM data from GeoFabrik)')

    args = parser.parse_args()

    update(args.target, args.source)

if __name__ == "__main__":
    main()

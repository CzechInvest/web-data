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
import shutil

CR_ZIP_URL='http://download.geofabrik.de/europe/czech-republic-latest-free.shp.zip'
OVERPASS="http://overpass-turbo.eu/"

DATA_DIR = None

PARAMS = {
    "rail": {
        "type": "geofabrik",
        "source": "gis_osm_railways_free_1.shp",
        "destination": "rail.geojson",
        "where": None
    },
    "highway": {
        "type": "geofabrik",
        "source": "gis_osm_roads_free_1.shp",
        "destination": "highway.geojson",
        "where": "fclass like 'motorway%'"
    },
    "primary": {
        "type": "geofabrik",
        "source": "gis_osm_roads_free_1.shp",
        "destination": "primary.geojson",
        "where": "fclass like 'primary%'"
    },
    "secondary": {
        "type": "geofabrik",
        "source": "gis_osm_roads_free_1.shp",
        "destination": "secondary.geojson",
        "where": "fclass like 'secondary%'"
    },
    "airports": {
        "type": "overpass",
        "destination": "airports.geojson",
        "query": """
            [out:json][timeout:25];
            (
                relation["iata"]({bbox});
                way["iata"]({bbox});
            );
            out body;
            >;
            out skel qt;
        """,
        "filters": "iata",
        "types": ["relation", "way"]
    },
    "ferry": {
        "type": "overpass",
        "destination": "ferry.geojson",
        "query": """
            [out:json][timeout:25];
            (node["amenity"="ferry_terminal"]({bbox}););
            out body;
            >;
            out skel qt;
        """,
        "filters": None,
        "types": ["node"]
    },

}


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


def _update_overpass(query, destination, filters, types):

    api = overpy.Overpass()
    bbox = [48.5227428999999972, 12.0223825000000009,
            51.0917286000000033, 18.8873178000000017]

    query = query.format(bbox=",".join([str(x) for x in bbox]))
    print(query)

    # fetch all ways and nodes
    result = api.query(query)
    geojson = {"type": "FeatureCollection", "features": []}
    print(len(result.ways))
    print(len(result.nodes))
    print(len(result.relations))
    if "way" in types:
        for way in result.get_ways():
            if filters and filters not in way.tags or not way.tags[filters]:
                continue
            geojson["features"].append({
                "type": "Feature",
                "properties": way.tags,
                "geometry": {
                    "type": "Point",
                    "coordinates": [float(way.nodes[0].lon), float(way.nodes[0].lat)]
                }
            })

    if "relation" in types:
        for relation in result.get_relations():
            if filters:
                if filters not in relation.tags or not relation.tags[filters]:
                    continue
            first_member = relation.members[0].resolve()
            #if isinstance(first_member, overpy.RelationWay):
            lon, lat = float(first_member.nodes[0].lon), float(first_member.nodes[0].lat)
            #else:
            #    lon, lat = float(first_member.lon), float(first_member.lat)
            geojson["features"].append({
                "type": "Feature",
                "properties": relation.tags,
                "geometry": {
                    "type": "Point",
                    "coordinates": [lon, lat]
                }
            })

    if "node" in types:
        for node in result.get_nodes():
            if filters:
                if filters not in node.tags or not node.tags[filters]:
                    continue
            geojson["features"].append({
                "type": "Feature",
                "properties": node.tags,
                "geometry": {
                    "type": "Point",
                    "coordinates": [float(node.lon), float(node.lat)]
                }
            })
    with open(destination, "w") as out:
        json.dump(geojson, out)



def _update_transport(data_dir, target_dir, name=None):

    global PARAMS

    if name:
        keys = name
    else:
        keys = PARAMS.keys()


    for key in keys:
        if PARAMS[key]["type"] == "geofabrik":
            _update_ogr2ogr(
                pathlib.Path(data_dir, PARAMS[key]["source"]),
                pathlib.Path(target_dir, PARAMS[key]["destination"]),
                PARAMS[key]["where"]
            )
        elif PARAMS[key]["type"] == "overpass":
            _update_overpass(
                PARAMS[key]["query"],
                pathlib.Path(target_dir, PARAMS[key]["destination"]),
                PARAMS[key]["filters"],
                PARAMS[key]["types"]
            )

def update(target, source=None, names=None):
    if not source and not names:
        source = download_osm()
        global DATA_DIR
        DATA_DIR = source

    _update_transport(source, target, names)


def main():
    parser = argparse.ArgumentParser(description='Get fresh copy of OSM (mainly transport) data')
    parser.add_argument('--target', type=str, required=True,
                        help='name of target directory')
    parser.add_argument('--source', type=str, required=False,
                        help='name of source directory (with downloaded and unzipped OSM data from GeoFabrik)')
    parser.add_argument('--name', type=str, required=False, nargs="+",
                        help='name of final dataset (rail, ferry, airports, highway, ...)')

    args = parser.parse_args()

    update(args.target, args.source, args.name)

if __name__ == "__main__":
    main()

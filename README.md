# web-data
Data for web map application

| kategorie | Etapa | Vrstva  | Vstup (XLSX) | Výstup (GeoJSON) | Filtrovat podle |
|-----------|-------|---------|--------------|------------------|-------|
|  Doprava  | 1     | Letecká doprava | OpenStreetMap | [airports.geojson](doprava/airports.geojson) | |
|  Doprava  | 1     | Lodní doprava | OpenStreetMap | [ferry.geojson](doprava/ferry.geojson) | |
|  Doprava  | 1     | Dálnice | OpenStreetMap | [highway.geojson](doprava/highway.geojson) | |
|  Doprava  | 1     | Silnice 1. třídy | OpenStreetMap | [primary.geojson](doprava/primary.geojson) | |
|  Doprava  | 1     | Silnice 2. třídy | OpenSreetMap  | [secondary.geojson](doprava/secondary.geojson) | |
|  Podnikatelská síť  | 1     | Automobilový průmysl | Dtb_src_export_20171005.xlsx | [dodavatele.geojson](podnikatelska_sit/dodavatele.geojson)| `sectors` |
| Podnikatelská síť  |  1 | Letecký průmysl | Dtb_src_export_20171005.xlsx | [dodavatele.geojson](podnikatelska_sit/dodavatele.geojson)| `sectors` |
| Podnikatelská síť  |  1 | Elektronika a elektrotechnika | Dtb_src_export_20171005.xlsx | [dodavatele.geojson](podnikatelska_sit/dodavatele.geojson)| `sectors` |
| Podnikatelská síť  |  1 | Energetika | Dtb_src_export_20171005.xlsx | [dodavatele.geojson](podnikatelska_sit/dodavatele.geojson)| `sectors` |
| Podnikatelská síť  |  1 | ICT Informační a komunikační | Dtb_src_export_20171005.xlsx | [dodavatele.geojson](podnikatelska_sit/dodavatele.geojson)| `sectors` |
| Podnikatelská síť  |  1 | Zpracování kovů | Dtb_src_export_20171005.xlsx | [dodavatele.geojson](podnikatelska_sit/dodavatele.geojson)| `sectors` |
| Podnikatelská síť  |  1 | Výroba plastových výlisků a pryže | Dtb_src_export_20171005.xlsx | [dodavatele.geojson](podnikatelska_sit/dodavatele.geojson)| `sectors` |
| Podnikatelská síť  |  1 | Strojírenství | Dtb_src_export_20171005.xlsx | [dodavatele.geojson](podnikatelska_sit/dodavatele.geojson)| `sectors` |
| Podnikatelská síť  |  1 | Materiály a obaly | Dtb_src_export_20171005.xlsx | [dodavatele.geojson](podnikatelska_sit/dodavatele.geojson)| `sectors` |
| Podnikatelská síť  |  1 | Zdravotnická technika, biotechnologie a farmaceutický průmysl | Dtb_src_export_20171005.xlsx | [dodavatele.geojson](podnikatelska_sit/dodavatele.geojson)| `sectors` |
| Podnikatelská síť |  1 | 10 největších firem podle sektorů |  | | |
| Podnikatelská síť  |  1 | Top investice podle původu | | | |
| Vzdělávání a VVI |  1 | Who is Who Czech research - HT | whoishow.xlsx | [whoiswho.geojson](vzdelavani/whoiswho.geojson)| `sectors` |
| Vzdělávání a VVI |  1 | Who is Who Czech research - AE | whoishow.xlsx | [whoiswho.geojson](vzdelavani/whoiswho.geojson)| `sectors` |
| Vzdělávání a VVI |  1 | Who is Who Czech research - AU | whoishow.xlsx | [whoiswho.geojson](vzdelavani/whoiswho.geojson)| `sectors` |
| Vzdělávání a VVI |  1 | Who is Who Czech research - BI | whoishow.xlsx | [whoiswho.geojson](vzdelavani/whoiswho.geojson)| `sectors` |
| Vzdělávání a VVI |  1 | Who is Who Czech research - IT | whoishow.xlsx | [whoiswho.geojson](vzdelavani/whoiswho.geojson)| `sectors` |
| Vzdělávání a VVI |  1 | Who is Who Czech research - NN | whoishow.xlsx | [whoiswho.geojson](vzdelavani/whoiswho.geojson)| `sectors` |
| Vzdělávání a VVI |  1 | Who is Who Czech research - EE | whoishow.xlsx | [whoiswho.geojson](vzdelavani/whoiswho.geojson)| `sectors` |
| Vzdělávání a VVI |  1 | Who is Who Czech research - CT | whoishow.xlsx | [whoiswho.geojson](vzdelavani/whoiswho.geojson)| `sectors` |
| Vzdělávání a VVI |  1 | VOŠ | | |
| Vzdělávání a VVI |  1 | SOU | | |
| Vzdělávání a VVI |  1 | SOŠ | | |
| Vzdělávání a VVI |  1 | ZŠ | | |
| Vzdělávání a VVI |  1 | MŠ | | |
| Vzdělávání a VVI |  1 | Mezinárodní školy | | |
| Vzdělávání a VVI |  1 | Inovační centra | Seznam_INFRASTRUKTURA_actual.xlsx | [pi_vtp.geojson](vzdelavani/pi_vtp.geojson) | `type` |
| Vzdělávání a VVI |  1 | VTParky | Seznam_INFRASTRUKTURA_actual.xlsx | [pi_vtp.geojson](vzdelavani/pi_vtp.geojson) | `type` |
| Vzdělávání a VVI |  1 | Univerzity dle fakult || | |
| Start-up |  1 | Podnikatelské inkubátory | Seznam_INFRASTRUKTURA_actual.xlsx | [pi_vtp.geojson](vzdelavani/pi_vtp.geojson) | `type` |
| Start-up |  1 | Akcelerátory | Seznam_INFRASTRUKTURA_actual.xlsx | [pi_vtp.geojson](vzdelavani/pi_vtp.geojson) | `type` |
| Start-up |  1 | Coworking centra | Seznam_INFRASTRUKTURA_actual.xlsx | [coworking.geojson](startup/coworking.geojson) | |
| Start-up |  1 | Business angels | cs.org investori.xlsx | [business_angels.geojson](startup/business_angels.geojson) |  |
| Start-up |  1 | ESA BIC SUPy | ESABIC_SUP.xlsx | [sup_bic.geojson](startup/sub_bic.geojson) |  |
| Start-up |  1 | CS, CA, CD podpořené z projektů | STARTUPY pro GIS.XLSX | [startupy.geojson](startup/startupy.geojson) |  |
| Veřejná podpora |  1 | Pobídky - podporované projekty | | |  |
| Veřejná podpora |  1 | Pobídkové mapy - investice| IP pro Jáchyma.xlsx, RUIAN | [orp.geojson](verejna_podpora/orp.geojson) | `investice` |
| Veřejná podpora |  1 | Pobídkové mapy - investice| IP pro Jáchyma.xlsx, RUIAN | [orp.geojson](verejna_podpora/orp.geojson) | `granty` |
| Nemovitosti |  1 | Průmyslové zóny podpořené státem| | |  |
| Nemovitosti | 1 | Zvýhodněné průmyslové zóny | IP proj Jáchyma.xlsx | [pz.geojson](verejna_podpora/pz.geojson) | |
| Nemovitosti | 1 | Brownfields | Export_CI GIS.XLSX | [brownfields.geojson](verejna_podpora/brownfields.geojson) | |
| Socioekonomické ukazatele | 1 | Počet obyvatel | GIS_Veru_Socio-demograf. ukazatele.xlsx | [pz.geojson](verejna_podpora/pz.geojson) | |
| Socioekonomické ukazatele | 1 | Průměrná mzda | GIS_Veru_Socio-demograf. ukazatele.xlsx | [kraje.geojson](socioekonomicka/kraje.geojson) |
| Socioekonomické ukazatele | 1 | Míra nezaměstnanosti | GIS_Veru_Socio-demograf. ukazatele.xlsx | [kraje.geojson](socioekonomicka/kraje.geojson) |
| Socioekonomické ukazatele | 1 | Počet nezaměstnaných | GIS_Veru_Socio-demograf. ukazatele.xlsx | [kraje.geojson](socioekonomicka/kraje.geojson) |
| Socioekonomické ukazatele | 1 | Počet obyvatel | GIS_Veru_Socio-demograf. ukazatele.xlsx | [kraje.geojson](socioekonomicka/kraje.geojson) |
| Socioekonomické ukazatele | 1 | Počet obyvatel na jedno pracovní místo | GIS_Veru_Socio-demograf. ukazatele.xlsx | [kraje.geojson](socioekonomicka/kraje.geojson) |
| Socioekonomické ukazatele | 1 | Jazyková vybavenost| GIS_Veru_Socio-demograf. ukazatele.xlsx | [kraje.geojson](socioekonomicka/kraje.geojson) |
| Regionální kanceláře | 1 | Regionální kanceláře CI |RK_tabproJachyma.xlsx | [rk.geojson](rk/reg_offices.geojson) | |


## Conversion from GeoJSON to Geobuf (Protocol Buffers)

### Install

```bash
npm install -g geobuf
```

### Command Line
```bash
json2geobuf data.geojson > data.pbf
```

## OverPass queries
Use in http://overpass-turbo.eu/
### International airports
```
[out:json][timeout:25];
(
  relation["iata"]({{bbox}});
  node["iata"]({{bbox}});  
  way["iata"]({{bbox}});  
);
out body;
>;
out skel qt;
```

### See Also
- [Geobuf](https://github.com/mapbox/geobuf)
- [Protocol Buffers](https://developers.google.com/protocol-buffers/)

## Kraje a Okresy

Download data from http://vdp.cuzk.cz/vdp/ruian/vymennyformat/vyhledej e.g.
http://vdp.cuzk.cz/vymenny_format/soucasna/20171231_ST_UKSH.xml.gz

```
ogr2ogr -f GeoJSON  -s_srs +init=epsg:5514 -t_srs +init=epsg:4326 -sql "select Kod, Nazev, GeneralizovaneHranice from Okresy" okresy.geojson ~/Stažené/20171231_ST_UKSG.xml 
ogr2ogr -f GeoJSON  -s_srs +init=epsg:5514 -t_srs +init=epsg:4326 -sql "select Kod, Nazev, GeneralizovaneHranice from ORP" ORP.geojson ~/Stažené/20171231_ST_UKSG.xml 
ogr2ogr -f GeoJSON  -s_srs +init=epsg:5514 -t_srs +init=epsg:4326 -sql "select Kod, Nazev, GeneralizovaneHranice from Vusc" kraje.geojson ~/Stažené/20171231_ST_UKSG.xml
```
## Data update

```
python3 src/lib/osm.py
```

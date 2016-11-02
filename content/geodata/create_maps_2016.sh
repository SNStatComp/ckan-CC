#!/bin/sh

if [ ! -f Uitvoer_shape ]
then
  if [ ! -f kaart2016.zip ]
  then
    wget -O kaart2016.zip https://www.cbs.nl/-/media/_pdf/2016/35/shape%202016%20versie%2010.zip
  fi

  unzip kaart2016.zip
fi

mkdir maps
mkdir amsterdam
mkdir tmp


# === Prepare neighbourhood map

# Convert to GeoJSON
ogr2ogr -f "GeoJSON" tmp/buurt_2016.geojson Uitvoer_shape/buurt_2016.shp -s_srs EPSG:28992 -t_srs EPSG:4326

# Simplify
mapshaper tmp/buurt_2016.geojson \
  -simplify 1% \
  -filter "WATER === 'NEE'" \
  -o maps/buurt_2016.geojson force format=geojson id-field=BU_CODE

# Select neighbourhoods in Amsterdam
mapshaper tmp/buurt_2016.geojson \
  -simplify 10% \
  -filter "GM_NAAM === 'Amsterdam' && WATER === 'NEE'" \
  -o amsterdam/buurt_2016.geojson force format=geojson id-field=BU_CODE

rm -f tmp/buurt_2016.geojson



# === Prepare district map

# Convert to GeoJSON
ogr2ogr -f "GeoJSON" tmp/wijk_2016.geojson Uitvoer_shape/wijk_2016.shp -s_srs EPSG:28992 -t_srs EPSG:4326

# Simplify
mapshaper tmp/wijk_2016.geojson \
  -simplify 1% \
  -filter "WATER === 'NEE'" \
  -o maps/wijk_2016.geojson force format=geojson id-field=WK_CODE

# Select neighbourhoods in Amsterdam
mapshaper tmp/wijk_2016.geojson \
  -simplify 10% \
  -filter "GM_NAAM === 'Amsterdam' && WATER === 'NEE'" \
  -o amsterdam/wijk_2016.geojson force format=geojson id-field=WK_CODE

rm -f tmp/wijk_2016.geojson


# ==== Prepare municipality map

# Convert to GeoJSON
ogr2ogr -f "GeoJSON" tmp/gem_2016.geojson Uitvoer_shape/gem_2016.shp -s_srs EPSG:28992 -t_srs EPSG:4326

# Simplify
mapshaper tmp/gem_2016.geojson \
  -simplify 10% \
  -filter "WATER === 'NEE'" \
  -o maps/gem_2016.geojson force format=geojson id-field=GM_CODE

# Select neighbourhoods in Amsterdam
mapshaper tmp/gem_2016.geojson \
  -simplify 10% \
  -filter "GM_NAAM === 'Amsterdam' && WATER === 'NEE'" \
  -o amsterdam/gem_2016.geojson force format=geojson id-field=GM_CODE

rm -f tmp/gem_2016.geojson





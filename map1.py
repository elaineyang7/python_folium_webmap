import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

# creating map center point and view
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="OpenStreetMap")#Stamen Watercolor")
fgv = folium.FeatureGroup(name="Volcanoes")

# create for loop for volcanoes data
for lt, ln, name, el in zip(lat, lon, name, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=name,
    fill_color=color_producer(el), fill=True, color='gray', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgp)
map.add_child(fgv)

map.add_child(folium.LayerControl())


map.save("Map1.html")

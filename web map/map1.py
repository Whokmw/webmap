import folium
import pandas as pd


def color_producer(elev):
    if elev < 1000:
        return "green"
    elif 1000 <= elev <= 3000:
        return "orange"
    else:
        return "red"
    
data = pd.read_csv("Volcanoes.txt")
lat = list(data['LAT'])
lon = list(data["LON"])
name = list(data['NAME'])
elev = list(data['ELEV'])
map = folium.Map(location=[38.58, -99.09], zoom_start=6, titles="Stamen Terrain")
fgv = folium.FeatureGroup(name="Volcanoes")
for lat, lon, elev, name in zip(lat, lon, elev, name):
    fgv.add_child(folium.CircleMarker(location=[lat, lon], popup=str(elev)+"m", tooltip=name, radius=4.8, fill_color=color_producer(elev), color="grey", fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(), style_function=lambda x: {"fillColor": "green" if x["properties"]["POP2005"] < 10000000 else "orange" if 10000000 <= x['properties']["POP2005"] < 20000000 else "red"}))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("map1.html")
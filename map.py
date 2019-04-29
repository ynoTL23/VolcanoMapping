import folium
import pandas

data = pandas.read_csv("VolcanoMapping\Volcanoes.csv")
latitude = list(data["LATITUDE"])
longitude = list(data["LONGITUDE"])
volcano_name = list(data["NAME"])
location = list(data["LOCATION"])
elevation = list(data["ELEVATION"])
volcano_type = list(data["TYPE"])

html_formatting = """
<h4>Volcano: <a href = "https://www.google.com/search?q=%s Volcano" target = "_blank">%s</a></h4>
Location: %s<br>
Longitude: %f<br>
Latitude: %f<br>
Elevation: %d meters<br>
Volcano Type: %s
"""

# Determine coloring for markers of volcano locations
def map_marker_color(elevation):
    if elevation < 1500:
        return 'green'
    elif 1500 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location = [31.174177, -3.756138], zoom_start = 3, tiles = "OpenStreetMap")

population_fg = folium.FeatureGroup(name = "Population")
volcano_fg = folium.FeatureGroup(name = "Volcanoes")

# Population Map - Population of Countries in 2005
population_fg.add_child(folium.GeoJson(
    data = open('VolcanoMapping\world_population.json', 'r', 
    encoding = 'utf-8-sig').read(), 
    style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

# Latitude, Longitude, Volcano Name, Volcano Location
for name, loc, lat, long, elev, volcano_type in zip(volcano_name, location, latitude, longitude, elevation, volcano_type): 
    iframe = folium.IFrame(html = html_formatting % (name, name, loc, long, lat, elev, volcano_type), width = 275, height = 150)
    marker = folium.CircleMarker(location = [lat, long], popup = folium.Popup(iframe), tooltip = name, radius = 6, color = map_marker_color(elev), weight = 2, fill = True, fill_opacity = 0.4)

    volcano_fg.add_child(marker)


map.add_child(population_fg)
map.add_child(volcano_fg)
map.add_child(folium.LayerControl())

map.save("VolcanoMapping\map.html")

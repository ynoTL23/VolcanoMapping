# Volcano Mapping
Written in Python, uses the Folium library to visualize global locations of volcanoes on a map.

<img src="https://github.com/ynoTL23/VolcanoMapping/raw/master/img/main%20map.png" width=75%>

Each location has a dot to interact with. Upon clicking, a popup will appear with generic information about the current volcano.

<img src="https://github.com/ynoTL23/VolcanoMapping/raw/master/img/volcano%20map.png" width=75%> <img src="https://github.com/ynoTL23/VolcanoMapping/raw/master/img/volcano%20dot%20hover.png" width=20%>


Each popup has a header with a link that performs a Google search for the volcano when clicked. Other information includes GPS coordinates, location, elevation and the volcano's type. Dots are also colored according to the volcano's elevation.

<img src="https://github.com/ynoTL23/VolcanoMapping/raw/master/img/volcano%20dot%20popup.png" width=25%>

The map also creates a visual boundary around the countries of the world and colors them according to their population size in 2005.

<img src="https://github.com/ynoTL23/VolcanoMapping/raw/master/img/population%20map.png" width=75%>

```
Countries with population in range [0 - 9,999,999] will be green
Countries with population in range [10,000,000 - 19,999,999] will be orange
Countries with population in range [20,000,000 - inf] will be red
```
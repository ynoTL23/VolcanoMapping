# Volcano Mapping
Written in Python, uses the Folium library to visualize global locations of volcanoes on a map.

Each location has a dot to interact with. Upon clicking, a popup will appear with generic information about the current volcano.

Each popup has a header with a link that performs a Google search for the volcano when clicked. Other information includes GPS coordinates, location, elevation and the volcano's type. Dots are also colored according to the volcano's elevation.

The map also creates a visual boundary around the countries of the world and colors them according to their population size in 2005.

> Countries with population in range [0 - 9,999,999] will be green

> Countries with population in range [10,000,000 - 19,999,999] will be orange

> Countries with population in range [20,000,000 - inf] will be red
import folium
import pandas

#get longitude and latitude values from text file
volacano_data = pandas.read_csv("Volcanoes_of_the_World.csv")
longitude = list(volacano_data["x"])
latitude = list(volacano_data["y"])
name = list(volacano_data["NAME"])
height = list(volacano_data["ELEV"])


#set map default location
map = folium.Map(location=[51., -0.03], zoom_start = 10)

feature_group = folium.FeatureGroup(name = "volcanoe_map")

#adds markers on the map for volcanoes to feature group
for lon, lat, name, height in zip(latitude, longitude, name, height):
    volcano_colour = ''
    height = int(height)
    if height <= 1800:
        volcano_colour = 'green'
    elif height > 2300:
        volcano_colour = 'red'   
    else:
        volcano_colour = 'blue'
    feature_group.add_child(folium.CircleMarker(location = [lon, lat], radius = 6, popup = name, 
    fill_color = volcano_colour, color = 'grey', fill_opacity = 0.7))



#adds items in feature group to the map
map.add_child(feature_group)
map.add_child(folium.LayerControl())
map.save("web_map_base.html")

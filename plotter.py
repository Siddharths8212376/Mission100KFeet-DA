import pandas as pd 
import gmplot

coords = pd.read_csv('parsed_coordinates.csv')

print(coords.head())



# map_ = folium.Map(location=[coords['LAT'][0], coords['LONG'][0]], zoom_start=15)
# lat_, long_ = coords['LAT'].tolist(), coords['LONG'].tolist()
# coordinates = [list(i) for i in zip(lat_, long_)]
# # coordinates = []
# # for a, b in zip(lat_, long_):
# #     coordinates.append([a, b])

# for index, coord in enumerate(coordinates[:-1]):
#     folium.CircleMarker(coord, popup='location ' + str(index + 1), color='crimson').add_to(map_)
#     folium.PolyLine(locations=[(coordinates[index][0], coordinates[index][1]), (coordinates[index + 1][0], coordinates[index + 1][1])], line_opacity=0.5).add_to(map_)
#     arrows = get_arrows(locations=[(coordinates[index][0], coordinates[index][1]), (coordinates[index + 1][0], coordinates[index + 1][1])], P1=index, P2=index + 1, n_arrows=1)
#     for arrow in arrows:
#         arrow.add_to(map_)
        
# map_.save('coordinates.html')

lat_, long_ = coords['LAT'].tolist(), coords['LONG'].tolist()

gmap = gmplot.GoogleMapPlotter(coords['LAT'][0], coords['LONG'][0], 13)
# gmap.apikey = "AIzaSyABZm6Z_UOFebgfTZCarocPQEErmn9kP7U"
gmap.scatter(lat_, long_, '#FF0000', size=1, marker=False)
gmap.heatmap(lat_, long_)
gmap.plot(lat_, long_, color='cornflowerblue', edge_width=1)

gmap.draw('parsemap.html')
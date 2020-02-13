import csv
data = open('raw_data.txt', encoding='utf-8', errors='ignore')
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

content = data.readlines()
print(len(content))
coordinates = []
for each_line in content:
    # print(each_line)
    try:
        _, link, _ = each_line.split("'")
        # print(link)
        _, location = link.split("=")
        _, coords = location.split(":")
        lat_, long_ = coords.split(",")
        
        # print(lat_, long_)
        if is_number(lat_) and is_number(long_):
            coordinates.append([lat_, long_])
    except:
        pass

print(len(coordinates))
# print(coordinates[:50])
with open('parsed_coordinates.csv', mode='w') as coords_file:
    coord_writer = csv.writer(coords_file)
    coord_writer.writerow(['LAT', 'LONG'])
    for coord in coordinates:
        coord_writer.writerow([coord[0], coord[1]])

    


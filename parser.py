import csv
import json
import pandas as pd 
import numpy as np 
import schedule
import time

def parse():
    data = open('./mission_flight/lora_final.txt', encoding='utf-8', errors='ignore')
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    content = data.readlines()
    print(len(content))
    coordinates = []
    index_line = 0
    for each_line in content:
        # print(each_line)
        try:
            _, link, _ = each_line.split("'")
            # print(link)
            _, location = link.split("=")
            _, coords = location.split(":")
            lat_, long_ = coords.split(",")
            
            # print(lat_, long_)
            # lats range from -90 to 90 
            # and longs range from -180 to 180
            if is_number(lat_) and is_number(long_):
                lat_ = float(lat_)
                long_ = float(long_)
                # checking for valid coordinates
                if (lat_ >= -90 and lat_ <= 90) and (long_ >= -180 and long_ <= 180):
                    # checking for regions inside wayanad
                    if (lat_ >= 11 and lat_ <= 12) and (long_ >= 75 and long_ <= 77):
                        if [lat_, long_] not in coordinates[-1:]:
                            coordinates.append([lat_, long_])
                            index_line += 1
        except:
            pass
    parse_coordinates = []
    
    for index, coord in enumerate(coordinates[:-1]):
        if (abs(coord[0] - coordinates[index + 1][0]) <= 0.004 and (abs(coord[1] - coordinates[index + 1][1]) <= 0.004)):
            parse_coordinates.append(coord)
    print(len(parse_coordinates))
    
    # generate more points between two coordinates
    def intermediates(p1, p2, nb_points=15):
        """"Return a list of nb_points equally spaced points
        between p1 and p2"""
        # If we have 8 intermediate points, we have 8+1=9 spaces
        # between p1 and p2
        x_spacing = (p2[0] - p1[0]) / (nb_points + 1)
        y_spacing = (p2[1] - p1[1]) / (nb_points + 1)

        return [[p1[0] + i * x_spacing, p1[1] +  i * y_spacing] 
                for i in range(1, nb_points+1)]
    set_coordinates = []
    for index, coord in enumerate(parse_coordinates[:-1]):
        intermediates_ = intermediates(coord, parse_coordinates[index + 1], 20)
        set_coordinates.append(coord)
        for coordinate in intermediates_:
            # coordinates.insert(index + 1, coordinate)
            set_coordinates.append(coordinate)
    set_coordinates.append(coordinates[-1])

    print(len(set_coordinates))


    # print(coordinates[:50])
    with open('parsed_coordinates.csv', mode='w') as coords_file:
        coord_writer = csv.writer(coords_file)
        coord_writer.writerow(['LAT', 'LONG'])
        for coord in set_coordinates:
            coord_writer.writerow([coord[0], coord[1]])

    # csv to json conversion using pandas
    csv_file = pd.DataFrame(pd.read_csv('parsed_coordinates.csv'))
    csv_file.to_json('./PUB/coords_new.json', orient='records')

schedule.every(5).seconds.do(parse)

ans = 1
while True:
    # if ans == 0:
    #     break
    schedule.run_pending()
    time.sleep(1)
    
# parse()

    
    
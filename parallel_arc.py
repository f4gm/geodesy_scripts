# Made by: f4gm
# github.com/f4gm

import math

def parallel_segment(eccentricity, semi_major, latitude_1, latitude_2, longitude_1, longitude_2):
    dif_longitude = abs(longitude_2 - longitude_1)
    radius_1 = semi_major*math.cos(latitude_1)/pow(1 - eccentricity*pow(math.sin(latitude_1), 2), 1/2)
    radius_2 = semi_major*math.cos(latitude_2)/pow(1 - eccentricity*pow(math.sin(latitude_2), 2), 1/2)
    parallel_segment_1 = radius_1*dif_longitude
    parallel_segment_2 = radius_2*dif_longitude
    return str(parallel_segment_1) + "," + str(parallel_segment_2)

path = "insert-path"
name_file = "insert-name-file.txt"
semi_major = 6378137
semi_minor = 6356752.314
ecc = (semi_major**2 - semi_minor**2)/semi_major**2

print("Calculating segments...")
file = open(path + name_file, "r")
file_result = open(path + "result.txt", "w")
file_result.write("Latitude 1,Latitude 2,Longitude 1,Longitude 2,Parallel Arc 1,Parallel Arc 2\n")
for line in file:
    new_line = ""
    if line.endswith("\n"):
        for character in range(len(line) - 1):
            new_line += line[character]
    else:
        new_line = line
    
    new_line = new_line.split(",")
    file_result.write(new_line[0] + "," + new_line[1] + "," + new_line[2] + "," + new_line[3] + "," + parallel_segment(ecc, semi_major, float(new_line[0]), float(new_line[1]), float(new_line[2]) , float(new_line[3])) + "\n")

print("Segments successfully calculated!")
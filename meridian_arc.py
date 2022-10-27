# Made by: f4gm
# github.com/f4gm

import math

def meridian_segment(eccentricity, semi_major, latitude_1, latitude_2):
    if latitude_2 < latitude_1:
        last = latitude_2
        latitude_2 = latitude_1
        latitude_1 = last
    
    constant_A = 1 + 3/4*eccentricity + 45/64*(eccentricity**2)
    constant_B = 3/4*eccentricity + 15/16*(eccentricity**2)
    constant_C = 15/16*(eccentricity**2)
    return semi_major*(1 - eccentricity)*(constant_A*(latitude_2 - latitude_1) - 1/2*constant_B*(math.sin(2*latitude_2) - math.sin(2*latitude_1)) + 1/4*constant_C*(math.sin(4*latitude_2) - math.sin(4*latitude_1)))

path = "insert-path"
name_file = "inser-name-file.txt"
semi_major = 6378137
semi_minor = 6356752.314
ecc = (semi_major**2 - semi_minor**2)/semi_major**2

print("Calculating segments...")
file = open(path + name_file, "r")
file_result = open(path + "result.txt", "w")
file_result.write("Latitude 1,Latitude 2,Meridian Arc\n")
for line in file:
    new_line = ""
    if line.endswith("\n"):
        for character in range(len(line) - 1):
            new_line += line[character]
    else:
        new_line = line
    
    new_line = new_line.split(",")
    file_result.write(new_line[0] + "," + new_line[1] + "," + str(meridian_segment(ecc, semi_major, float(new_line[0]), float(new_line[1]))) + "\n")

print("Segments successfully calculated!")
file.close()
file_result.close()
# Made by: f4gm
# github.com/f4gm

import math

def area(eccentricity, semi_minor, latitude_1, latitude_2, longitude_1, longitude_2):
    dif_longitude = abs(longitude_2 - longitude_1)
    factor = dif_longitude/(2*math.pi)
    mean_latitude = (latitude_1 + latitude_2)/2
    dif_latitude = latitude_2 - latitude_1
    constant_A = 1 + 1/2*eccentricity + 3/8*(eccentricity**2) + 5/16*(eccentricity**3) + 35/128*(eccentricity**4)
    constant_B = 1/6*eccentricity + 3/16*(eccentricity**2) + 3/16*(eccentricity**3) + 35/192*(eccentricity**4)
    constant_C = 3/80*(eccentricity**2) + 1/16*(eccentricity**3) + 15/64*(eccentricity**4)
    constant_D = 1/112*(eccentricity**3) + 5/256*(eccentricity**4)
    constant_E = 5/2304*(eccentricity**4)

    area = 4*math.pi*factor*(semi_minor**2)*(constant_A*math.sin(1/2*dif_latitude)*math.cos(mean_latitude) - constant_B*math.sin(3/2*dif_latitude)*math.cos(3*mean_latitude) + constant_C*math.sin(5/2*dif_latitude)*math.cos(5*mean_latitude) - constant_D*math.sin(7/2*dif_latitude)*math.cos(7*mean_latitude) + constant_E*math.sin(9/2*dif_latitude)*math.cos(9*mean_latitude))
    
    return str(latitude_1) + "," + str(latitude_2) + "," + str(longitude_1) + "," + str(longitude_2) + "," + str(abs(area))

path = "insert-path"
name_file = "inser-file-name.txt"

# WGS84 ellipsoid
semi_major = 6378137
semi_minor = 6356752.314
ecc = (semi_major**2 - semi_minor**2)/semi_major**2

print("Calculating segments...")
file = open(path + name_file, "r")
file_result = open(path + "result.txt", "w")
file_result.write("Latitude 1,Latitude 2,Longitude 1,Longitude 2, Area\n")
for line in file:
    new_line = ""
    if line.endswith("\n"):
        for character in range(len(line) - 1):
            new_line += line[character]
    else:
        new_line = line
    
    new_line = new_line.split(",")
    file_result.write(area(ecc, semi_minor, float(new_line[0]), float(new_line[1]), float(new_line[2]), float(new_line[3])) + "\n")

print("Calculated area!")
# Made by: f4gm
# github.com/f4gm

import math

def meridian_radius(semi_major, eccentricity, latitude):
    return (semi_major*(1 - eccentricity))/(pow(1 - eccentricity*pow(math.sin(latitude) ,2), 3/2))

def vertical_radius(semi_major, eccentricity, latitude):
    return semi_major/(pow(1 - eccentricity*pow(math.sin(latitude), 2), 1/2))

path = "insert-path"
name_file = "insert-file-name.txt"
semi_major = 6378137
semi_minor = 6356752.314
ecc = (semi_major**2 - semi_minor**2)/semi_major**2

print("Calculating curvatures...")
file = open(path + name_file, "r")
file_result = open(path + "result.txt", "w")
file_result.write("Latitude,M,N\n")
for line in file:
    new_line = ""
    if line.endswith("\n"):
        for character in range(len(line) - 1):
            new_line += line[character]
    else:
        new_line = line
    file_result.write(str(new_line) + "," + str(meridian_radius(semi_major, ecc, float(new_line))) + "," + str(vertical_radius(semi_major, ecc, float(new_line))) + "\n")

print("Calculated curvatures!")
file.close()
file_result.close()
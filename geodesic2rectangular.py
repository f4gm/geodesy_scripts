# Made by: f4gm
# github.com/f4gm

import math

def geodesic2rectangular(lat, lon, height, ecc, semi_major):
    normal = semi_major/pow(1 - ecc*(math.sin(lat)**2), 1/2)
    X = (normal + height)*math.cos(lat)*math.cos(lon)
    Y = (normal + height)*math.cos(lat)*math.sin(lon)
    Z = (normal*(1 - ecc) + height)*math.sin(lat)
    return str(X) + "," + str(Y) + "," + str(Z)

path = "insert-path"
name_file = "insert-file-name.txt"

# WGS84
semi_major = 6378137
semi_minor = 6356752.314
ecc = (semi_major**2 - semi_minor**2)/semi_major**2

print("Calculting...")
file = open(path + name_file, "r")
file_result = open(path + "result.txt", "w")
file_result.write("Latitude,Longitude,Height,X,Y,Z\n")
for line in file:
    new_line = ""
    if line.endswith("\n"):
        for character in range(len(line) - 1):
            new_line += line[character]
    else:
        new_line = line
    
    new_line = new_line.split(",")
    file_result.write(new_line[0] + "," + new_line[1] + "," + new_line[2] + "," + geodesic2rectangular(float(new_line[0]), float(new_line[1]), float(new_line[2]), ecc, semi_major) + "\n")

print("Coordinates successfully calculated!")
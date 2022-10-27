# Made by: f4gm
# github.com/f4gm

import math

def dms2rad(angle):
    angle = angle.split(":")
    if float(angle[0]) < 0:
        angle = (float(angle[0]) - float(angle[1])/60 - float(angle[2])/3600)*math.pi/180
    else:
        angle = (float(angle[0]) + float(angle[1])/60 + float(angle[2])/3600)*math.pi/180
    return angle

def rad2dms(angle):
    angle = angle*180/math.pi
    degrees = int(angle)
    minutes = int((angle - degrees)*60)
    seconds = (angle - degrees - minutes/60)*3600
    return str(degrees) + ":" + str(minutes) + ":" + str(seconds)

def radians2second(angle):
    return angle*(180/math.pi)*3600

def find_acimut(lat_A, lon_A, lat_B, lon_B, angle):
    dif_lat = lat_B - lat_A
    dif_lon = lon_B - lon_A

    if dif_lat < 0 and dif_lon == 0:
        # South line
        return 0
    elif dif_lat < 0 and dif_lon < 0:
        # First quadrant
        return angle
    elif dif_lat == 0 and dif_lon < 0:
        # West line
        return math.pi/2
    elif dif_lat > 0 and dif_lon < 0:
        # Second quadrant
        return math.pi - angle
    elif dif_lat > 0 and dif_lon == 0:
        # North line
        return math.pi
    elif dif_lat > 0 and dif_lon > 0:
        # Third quadrant
        return math.pi + angle
    elif dif_lat == 0 and dif_lon > 0:
        # East line
        return 3*math.pi/2
    elif dif_lat < 0 and dif_lon > 0:
        # Fourth quadrant
        return 2*math.pi - angle

def rev(angle):
    if angle > 2*math.pi:
        return angle - 2*math.pi
    else:
        return angle

def inverse_puissant(ecc, semi_major, lat_A, lon_A, lat_B, lon_B):
    lat_A = dms2rad(lat_A)
    lon_A = dms2rad(lon_A)
    lat_B = dms2rad(lat_B)
    lon_B = dms2rad(lon_B)
    dif_lat = lat_B - lat_A
    dif_lon = lon_B - lon_A
    arc = math.sin(1/3600*math.pi/180)
    W_A = (1 - ecc*(math.sin(lat_A)**2))**0.5
    W_B = (1 - ecc*(math.sin(lat_B)**2))**0.5
    normal_A = semi_major/W_A
    normal_B = semi_major/W_B
    meridian_A = semi_major*(1 - ecc)/(W_A**3)
    
    # Inverse Puissant
    B = 1/(meridian_A*arc)
    C = math.tan(lat_A)/(2*normal_A*meridian_A*arc)
    D = 3*ecc*math.sin(lat_B)*math.cos(lat_B)*arc/(2*(W_B**2))
    E = (1 + 3*(math.tan(lat_B)**2))/(6*(normal_B**2))

    X = normal_B*math.sin(dif_lon)*math.cos(lat_B)
    Y = (-1*radians2second(dif_lat) - C*(X**2) - D*(radians2second(dif_lat)**2))/(B*(1 - E*(X**2)))
    alpha = rev(find_acimut(lat_A, lon_A, lat_B, lon_B, math.atan(abs(X/Y))))
    geodesic_line = abs(X/math.sin(alpha))
    
    return str(lat_A) + "," + str(lon_A) + "," + str(lat_B) + "," + str(lon_B) + "," + str(X) + "," + str(Y) + "," + rad2dms(alpha) + "," + str(geodesic_line)

path = "insert-path"
name_file = "insert-name-file.txt"

ellipsoid = 1
if ellipsoid == 1:
    # WGS84
    semi_major = 6378137
    semi_minor = 6356752.314
elif ellipsoid == 2:
    # International 1924 Hayford
    semi_major = 6378388
    semi_minor = 6356911.946
ecc = (semi_major**2 - semi_minor**2)/semi_major**2

print("Calculating...")
file = open(path + name_file, "r")
file_result = open(path + "result.txt", "w")
file_result.write("Latitude A,Longitude A,Latitude B,Longitude B,X,Y,Alpha,Geodesic Line\n")
for line in file:
    new_line = ""
    if line.endswith("\n"):
        for character in range(len(line) - 1):
            new_line += line[character]
    else:
        new_line = line
    
    new_line = new_line.split(",")
    file_result.write(inverse_puissant(ecc, semi_major, new_line[0], new_line[1], new_line[2], new_line[3]) + "\n")

print("Successfully calculated!")
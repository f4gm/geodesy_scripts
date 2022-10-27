# Made by: f4gm
# github.com/f4gm

import math

def rad2dms(angle):
    angle = angle*180/math.pi
    degrees = int(angle)
    minutes = int((angle - degrees)*60)
    seconds = (angle - degrees - minutes/60)*3600
    return str(degrees) + ":" + str(minutes) + ":" + str(seconds)

def dms2rad(angle):
    angle = angle.split(":")
    if float(angle[0]) < 0:
        angle = (float(angle[0]) - float(angle[1])/60 - float(angle[2])/3600)*math.pi/180
    else:
        angle = (float(angle[0]) + float(angle[1])/60 + float(angle[2])/3600)*math.pi/180
    return angle

def puissant(eccentricity, semi_major, latitude, longitude, acimut, distance):
    acimut = dms2rad(acimut)

    # Calculate latitude
    arc = math.sin(math.pi/648000)
    w = pow(1 - eccentricity*pow(math.sin(latitude), 2), 1/2)
    N = semi_major/w
    M =  semi_major*(1 - eccentricity)/w**3
    B = 1/(M*arc)
    C = math.tan(latitude)/(2*N*M*arc)
    D = (3*eccentricity*math.sin(latitude)*math.cos(latitude)*arc)/(2*w**2)
    E = (1 + 3*pow(math.tan(latitude), 2))/(6*N**2)

    d_phi = distance*B*math.cos(acimut) + (distance**2)*C*pow(math.sin(acimut), 2) - (distance**3)*B*E*math.cos(acimut)*pow(math.sin(acimut), 2)
    D_phi = d_phi + D*d_phi**2

    latitude_B = latitude - math.radians(D_phi/3600)

    # Calculate longitude
    N_B = semi_major/pow(1 - eccentricity*pow(math.sin(latitude_B), 2), 1/2)
    D_lambda = math.asin(math.sin(distance/N_B)*math.sin(acimut)/math.cos(latitude_B))

    longitude_B = longitude - D_lambda

    # Calculate against acimuth
    mean_latitude = (latitude + latitude_B)/2
    F = (math.sin(mean_latitude)*pow(math.cos(mean_latitude), 2)*arc**2)/12
    D_acimut = D_lambda*3600*math.sin(mean_latitude)/math.cos(math.radians(D_phi/3600)/2) + ((D_lambda*3600)**3)*F

    contra_acimut = acimut + math.pi + math.radians(D_acimut/3600)

    if contra_acimut > 2*math.pi:
        contra_acimut = contra_acimut - math.pi

    return str(rad2dms(latitude_B)) + "," + str(rad2dms(longitude_B)) + "," + str(rad2dms(contra_acimut))

path = "insert-path"
name_file = "inser-file-name.txt"
semi_major = 6378137
semi_minor = 6356752.314
ecc = (semi_major**2 - semi_minor**2)/semi_major**2
print("Start point")
latitude_A = float(dms2rad(input("Latitude (d:m:s): ")))
longitude_A = float(dms2rad(input("Longitude (d:m:s): ")))

print("Calculating coordinates...")
file = open(path + name_file, "r")
file_result = open(path + "result.txt", "w")
file_result.write("Acimut,Geodesic line,Latitude,Longitude,Against acimut\n")
for line in file:
    new_line = ""
    if line.endswith("\n"):
        for character in range(len(line) - 1):
            new_line += line[character]
    else:
        new_line = line
    
    new_line = new_line.split(",")
    file_result.write(new_line[0] + "," + new_line[1] + "," + puissant(ecc, semi_major, latitude_A, longitude_A, new_line[0], float(new_line[1])) + "\n")

print("Coordenates successfully calculated!")
from __future__ import print_function
import numpy as np
import cv2
import argparse

TARGET_COLORS = {"Red": (255, 0, 0), "Yellow": (255, 255, 0), "Green": (0, 255, 0), "Black": (0, 0, 0), "White": (255, 255, 255), "Cyan": (38, 74, 96), "Blue": (0, 102, 304)}

def color_difference (color1, color2):
    return sum([abs(component1-component2) for component1, component2 in zip(color1, color2)])

def readImage(filePath):
	img = cv2.imread(filePath, 0)
	ret, binaryImage = cv2.threshold(img, 10, 255, cv2.THRESH_BINARY)
	return binaryImage
	
def printImage(filePath):
	black="30"
	red="31"
	green="32"
	yellow="33"
	blue="34"
	purple="35"
	cyan="36"
	white="37"
	img = cv2.imread(filePath)
	width = len(img)
	length = len(img[0])
	my_color = (123, 234, 100)
	differences = [[color_difference(my_color, target_value), target_name] for target_name, target_value in TARGET_COLORS.items()]
	differences.sort()  # sorted by the first element of inner lists
	my_color_name = differences[0][1]
	for i in range(0,length):
		for j in range(0,width):
			string = "\033[1;"
			my_color = img[i,j]
			differences = [[color_difference(my_color, target_value), target_name] for target_name, target_value in TARGET_COLORS.items()]
			differences.sort()  # sorted by the first element of inner lists
			my_color_name = differences[0][1]
			if my_color_name == "Green":
				string = string+"32;40m"
			elif my_color_name == "Red":
				string = string+"31;40m"
			elif my_color_name =="Yellow":
				string = string+"33;40m"
			elif my_color_name =="Black":
				string = string+"30;40m"
			elif my_color_name =="White":
				string = string+"37;40m"
			elif my_color_name =="Cyan":
				string = string+"36;40m"
			elif my_color_name =="Blue":
				string = string+"34;40m"
			string=string+"A"
			print(string,end='')
			
		print()

if __name__ == '__main__':
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--image", help = "path to the image")
	args = vars(ap.parse_args())
	printImage(args["image"])

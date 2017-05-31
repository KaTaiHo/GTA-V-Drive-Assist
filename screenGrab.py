import numpy as np
from PIL import ImageGrab
import cv2
import time
from input import PressKey
import pyautogui

movement_dict = {'W' : 0x11, 'A' : 0x1E, 'S' : 0x1f, 'D' : 0x20}

def draw_lines(img, lines):
	try:
		for line in lines:
			coords = line[0]
			cv2.line(img, (coords[0], (coords[1])), (coords[2], coords[3]), [255, 255, 255], 3)
	except:
		pass

def region_of_interest(img, vertices):
	mask = np.zeros_like(img)
	cv2.fillPoly(mask, vertices, 255)
	masked = cv2.bitwise_and(img, mask)
	return masked

def process_img(original_image):
	# processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
	processed_img = original_image
	processed_img = cv2.Canny(processed_img, threshold1 = 200, threshold2 = 300)
	processed_img = cv2.GaussianBlur(processed_img, (5,5), 0)
	vertices = np.array([[10, 500], [10, 300], [300, 200], [500, 200], [800, 300], [800, 500]], np.int32)
	processed_img = region_of_interest(processed_img, [vertices])

	#edges
	lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 180, 20, 15)
	draw_lines(processed_img, lines)
	return processed_img

time.sleep(4)

last_time = time.time()
print (type(movement_dict['W']))

while(True):
	#PressKey(movement_dict['W'])
	screen = np.array(ImageGrab.grab(bbox=(0, 40, 800, 640)))
	new_screen = process_img(screen)

	print('Loop took ' + str(time.time() - last_time))
	last_time = time.time()
	cv2.imshow('window', new_screen)
	# cv2.imshow('window2', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
	if cv2.waitKey(25) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
		break
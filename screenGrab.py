import numpy as np
from PIL import ImageGrab
import cv2
import time
from input import PressKey

movement_dict = {'W' : 0x11, 'A' : 0x1E, 'S' : 0x1f, 'D' : 0x20}

def process_img(original_image):
	processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
	processed_img = cv2.Canny(processed_img, threshold1 = 200, threshold2 = 300)
	return processed_img

def run():
	time.sleep(4)

	last_time = time.time()
	print (type(movement_dict['W']))

	while(True):
		PressKey(movement_dict['W'])
		screen = np.array(ImageGrab.grab(bbox=(0, 40, 800, 640)))
		new_screen = process_img(screen)

		print('Loop took ' + str(time.time() - last_time))
		last_time = time.time()
		cv2.imshow('window', new_screen)
		# cv2.imshow('window2', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
		if cv2.waitKey(25) & 0xFF == ord('q'):
			cv2.destroyAllWindows()
			break
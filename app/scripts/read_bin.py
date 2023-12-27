# encoding: utf-8

import os
import numpy as np
import matplotlib.pyplot as plt
import cv2

image_bin_path = r'/media/psf/work/data/ost_calibration/imu_to_vpcam/2023-12-21-taurus-30fps-success-1-cam0/0_img_.bin'
# image_bin_path = r'/Users/wayne/Documents/work/data/ost_calibration/imu_to_vpcam/0_img_.bin'

w, h, c = 1920, 1200, 1
sz = w * h * c

with open(image_bin_path, 'rb') as f:
	f.seek(0, 2)
	sz = f.tell()
	print(f'{(sz // np.dtype(np.uint8).itemsize)=}')
	f.seek(0, 0)

with open(image_bin_path, 'rb') as f:
	data = f.read()
	images = np.frombuffer(data, dtype=np.uint8)
	N = len(data) // sz
	print(images.shape, N)
	images = images.reshape((-1, h, w, c))
	for i in range(N):
		img = images[i].squeeze()
		plt.imshow(img)
		plt.show()
	# N = len(data) // sz
	# print(N)
	# print(len(data))
	# for i in range(N):
	# 	img = np.frombuffer(data[i * sz : (i + 1) * sz], dtype=np.uint8)
	# 	img = img.reshape((h, w, c))
	# 	plt.imshow(img)
	# 	plt.show()

with open(image_bin_path, 'rb') as f:
	f.seek(idx * self.size_per_image)
	data = np.frombuffer(f.read(self.size_per_image), dtype=np.uint8).reshape((self.h, self.w, self.c)).squeeze()


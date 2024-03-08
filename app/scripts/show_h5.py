# coding: utf-8

import cv2
import h5py


path = r'/media/psf/work/data/ost_calibration/imu_to_vpcam/20240228-60Hz-1920x1200-naked-fix-6mm-cam2imu_largeboard_taurus_test2/0_img_640x400.h5'
cv2.namedWindow('haha')
with h5py.File(path, 'r') as h:
	data = h['images']
	print(data.shape)
	for i in range(len(data)):
		cv2.imshow('haha', data[i].squeeze())
		cv2.waitKey(1)

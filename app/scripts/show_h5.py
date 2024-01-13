# coding: utf-8

import cv2
import h5py


path = r'/media/psf/work/data/ost_calibration/imu_to_vpcam/20240104-60Hz-taurus-32_33-wearing-cam2imu_fast_shrink-test1/0_img_640x400.h5'
cv2.namedWindow('haha')
with h5py.File(path, 'r') as h:
	data = h['images']
	print(data.shape)
	for i in range(len(data)):
		cv2.imshow('haha', data[i].squeeze())
		cv2.waitKey(1)

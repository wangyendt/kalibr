# author: wangye(Wayne)
# license: Apache Licence
# file: sync_imu_cam_timestamp_bin.py
# time: 2023-12-12-20:44:57
# contact: wang121ye@hotmail.com
# site:  wangyendt@github.com
# software: PyCharm
# code is far away from bugs.


import sys
import os
import pandas as pd

if len(sys.argv) < 1:
	print(f'Usage: python3 {__file__} "path/to/dataset"')
	exit(0)
dataset_root = sys.argv[1]
header = '#timestamp [ns]'
imu_file = os.path.join(dataset_root, 'data.csv')
cam_file = os.path.join(dataset_root, '0_save_timestamp.txt')
imu_data = pd.read_csv(imu_file)
cam_ts = pd.read_csv(cam_file, header=None)
imu_data.iloc[:,0] = imu_data.iloc[:,0] - imu_data.iloc[0,0] + cam_ts.iloc[0,0]
imu_data.to_csv(imu_file, index=False)
# data.columns = [header]
# data.to_csv(imu_file, index=False)

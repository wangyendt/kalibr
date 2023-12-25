# author: wangye(Wayne)
# license: Apache Licence
# file: change_imu_format_from_taurus_txt_to_euroc_data_csv.py
# time: 2023-12-20-19:31:57
# contact: wang121ye@hotmail.com
# site:  wangyendt@github.com
# software: PyCharm
# code is far away from bugs.


import sys
import os
import pandas as pd
import collections
import numpy as np
import re

if len(sys.argv) < 1:
	print(f'Usage: python3 {__file__} "path/to/dataset"')
	exit(0)
dataset_root = sys.argv[1]

imu_file = os.path.join(dataset_root, 'mav0/imu0/data.txt')
print(imu_file)
if not os.path.exists(imu_file):
	print('no need to transfer from taurus data to euroc data')
	exit(0)


sensor_data = collections.defaultdict(list)
sensor_data_npy = collections.defaultdict(np.array)
with open(imu_file, 'r', encoding='UTF-16LE', errors='ignore') as f:
# with open(path, 'r', encoding='UTF-8', errors='ignore') as f:
	lines = f.readlines()
	print(len(lines))
	for i, line in enumerate(lines):
		line = line.strip()
		if not any(kw in line for kw in ('acc', 'gyro', 'mag')): continue
		if 'get response!!!!65' in line: continue
		sensor, data = re.findall(r'(.*) = (.*)', line)[0]
		sensor_data[sensor].append([float(d) for d in data.split(' ') if d])
sensor_data_npy['acc'] = np.array(sensor_data['acc'])[:, :3]
sensor_data_npy['gyro'] = np.array(sensor_data['gyro'])[:, :3]
sensor_data_npy['mag'] = np.array(sensor_data['mag'])[:, :3]
N = min(len(sensor_data_npy['acc']), len(sensor_data_npy['gyro']), len(sensor_data_npy['mag']))
print(f'{N=}')
sensor_data_npy['acc'] = sensor_data_npy['acc'][:N]
sensor_data_npy['gyro'] = sensor_data_npy['gyro'][:N]
sensor_data_npy['mag'] = sensor_data_npy['mag'][:N]
sensor_data_npy['ts'] = np.array(sensor_data['acc'])[:, 3][:N]
print(f"{sensor_data_npy['ts'][np.where(sensor_data_npy['mag'][:, 2] < -500)]=}")
sensor_data_npy['ts'] -= sensor_data_npy['ts'][0]
sensor_data_npy['ts'] /= 1e4
sensor_data_npy['ts'] *= 1e9
sensor_data_npy['ts'] = sensor_data_npy['ts'].astype(int)
data = pd.DataFrame(np.c_[sensor_data_npy['ts'], sensor_data_npy['gyro'], sensor_data_npy['acc']])
data.columns = '#timestamp [ns],w_RS_S_x [rad s^-1],w_RS_S_y [rad s^-1],w_RS_S_z [rad s^-1],a_RS_S_x [m s^-2],a_RS_S_y [m s^-2],a_RS_S_z [m s^-2]'.split(',')
data['#timestamp [ns]'] = data['#timestamp [ns]'].astype(int)
print(data.head())
data.to_csv(imu_file.replace('data.txt', 'data.csv'), index=False)

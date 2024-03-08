# coding: utf-8


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path = r'/media/psf/work/data/ost_calibration/imu_to_vpcam/20240228-60Hz-1920x1200-naked-fix-6mm-cam2imu_largeboard_taurus_test2/data.csv'
data = pd.read_csv(path)
h = data.columns
data = data.values
print(data.shape)
ts = data[:,0]
ts -= ts[0]
ts /= 1e9
gyro = data[:,1:4]
acc = data[:,4:7]
# data_new = data[ts > 14.8]
# dn = pd.DataFrame(data_new, columns=h)
# dn.to_csv(path.replace('data.csv', 'data_n.csv'), index=False)
plt.figure()
plt.subplot(211)
plt.plot(ts, acc)
plt.subplot(212)
plt.plot(ts, gyro)
plt.show()

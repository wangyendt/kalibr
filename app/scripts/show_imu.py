# coding: utf-8


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path = r'/media/psf/work/data/ost_calibration/imu_to_vpcam/20240104-60Hz-taurus-32_33-wearing-cam2imu_fast_shrink-test1/data.csv'
data = pd.read_csv(path).values
print(data.shape)
ts = data[:,0]
ts -= ts[0]
ts /= 1e9
gyro = data[:,1:4]
acc = data[:,4:7]
plt.figure()
plt.subplot(211)
plt.plot(ts, acc)
plt.subplot(212)
plt.plot(ts, gyro)
plt.show()

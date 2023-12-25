dataset_root=/media/psf/work/data/ost_calibration/imu_to_vpcam/bin_test_cam0
device=mercury

if [[ $device == mercury ]]; then
    cp cam-camchain-mercury_cam0.yaml $dataset_root/cam0-camchain.yaml
    cp cam-camchain-mercury_cam1.yaml $dataset_root/cam1-camchain.yaml
    cp ./imu_mercury.yaml $dataset_root/imu.yaml
elif [[ $device == taurus ]]; then
    cp cam-camchain-taurus-shaded_cam0.yaml $dataset_root/cam0-camchain.yaml
    cp cam-camchain-taurus-shaded_cam1.yaml $dataset_root/cam1-camchain.yaml
    cp ./imu_taurus.yaml $dataset_root/imu.yaml
    python3 ./change_imu_format_from_taurus_txt_to_euroc_data_csv.py "$dataset_root"
else
    echo "Unidentified device: " $device
fi
cp ./april_6x6.yaml $dataset_root/aprilgrid.yaml

python3 ./sync_imu_cam_timestamp_bin.py "$dataset_root"
kalibr_dir=/home/wayne/work/code/catkin_wss/kalibr_ws
cd $kalibr_dir
export KALIBR_MANUAL_FOCAL_LENGTH_INIT=500
bash ./run_kalibr_cam_imu_bin.sh $dataset_root 0 # calibrate cam0
# bash ./run_kalibr_cam_imu_bin.sh $dataset_root 1 # calibrate cam1


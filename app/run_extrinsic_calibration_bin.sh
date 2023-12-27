dataset_root=/media/psf/work/data/ost_calibration/imu_to_vpcam/2023-12-21-taurus-30fps-success-1-cam0
kalibr_dir=/home/wayne/work/code/catkin_wss/kalibr_ws
device=taurus
which_cam=0

if [[ $device == mercury ]]; then
    cp configs/cam-camchain-mercury_cam0.yaml $dataset_root/cam0-camchain.yaml
    cp configs/cam-camchain-mercury_cam1.yaml $dataset_root/cam1-camchain.yaml
    cp configs/imu_mercury.yaml $dataset_root/imu.yaml
elif [[ $device == taurus ]]; then
    cp configs/cam-camchain-taurus-shaded_cam0.yaml $dataset_root/cam0-camchain.yaml
    cp configs/cam-camchain-taurus-shaded_cam1.yaml $dataset_root/cam1-camchain.yaml
    cp configs/imu_taurus.yaml $dataset_root/imu.yaml
    python3 ./change_imu_format_from_taurus_txt_to_euroc_data_csv.py "$dataset_root"
else
    echo "Unidentified device: " $device
fi
cp configs/april_6x6.yaml $dataset_root/aprilgrid.yaml

python3 ./sync_imu_cam_timestamp_bin.py "$dataset_root"


cd $kalibr_dir
export KALIBR_MANUAL_FOCAL_LENGTH_INIT=500
source devel/setup.sh
export LD_PRELOAD=/lib/aarch64-linux-gnu/libGLdispatch.so
root=$dataset_root
target=$root/aprilgrid.yaml
camchain_yaml=$root/cam${which_cam}-camchain.yaml
imu_yaml=$root/imu.yaml
bin_file=$root/${which_cam}_img_.h5
bin_timestamp_file=$root/${which_cam}_save_timestamp.txt
imu_file=$root/data.csv

rosrun kalibr kalibr_calibrate_imu_camera --target $target --cam $camchain_yaml --imu $imu_yaml --binfile $bin_file --bintimestampfile $bin_timestamp_file --imufile $imu_file # --imu-models scale-misalignment-size-effect # --show-extraction # --bag-from-to 20 400 # --show-extraction



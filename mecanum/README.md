### Cài đặt và Khởi chạy

**1. Tạo workspace và tải mã nguồn:**
```bash
mkdir -p ~/mecanum_ws/src
cd ~/mecanum_ws/src
git clone https://github.com/hiep-noob/V-V-n-Hi-p.git mecanum
```
2. Biên dịch dự án:
```
cd ~/mecanum_ws
colcon build --packages-select mecanum --symlink-install
```
3. Kích hoạt môi trường và Khởi chạy hệ thống:
```
source install/setup.bash
ros2 launch mecanum sim.launch.py
```
4. Lệnh chạy đồ thị encoder 4 bánh:
```
ros2 run rqt_plot rqt_plot
```


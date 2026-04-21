# Mecanum
Project Giữa kỳ_Vũ Văn Hiệp
# Mecanum Arm Robot — ROS2 Humble Simulation

## Yêu cầu hệ thống
- Ubuntu 22.04
- ROS2 Humble
- Gazebo Classic (11)

## 1. Cài đặt dependencies

```bash
# Gazebo + ROS2 control
sudo apt install -y \
  ros-humble-gazebo-ros \
  ros-humble-gazebo-ros2-control \
  ros-humble-ros2-control \
  ros-humble-ros2-controllers \
  ros-humble-robot-state-publisher \
  ros-humble-joint-state-publisher

# TurtleBot3 world (môi trường mô phỏng)
sudo apt install -y ros-humble-turtlebot3-gazebo

# Python GUI
sudo apt install -y python3-tk
```

## 2. Clone và build

```bash
mkdir -p ~/mecanum_ws/src
cd ~/mecanum_ws/src
git clone https://github.com/hiep-noob/Mecanum.git mecanum
cd ~/mecanum_ws
colcon build --packages-select mecanum --symlink-install
source install/setup.bash
```

3. Cấp quyền thực thi cho các script
```
chmod +x ~/mecanum_ws/src/mecanum/mecanum_dashboard.py
chmod +x ~/mecanum_ws/src/mecanum/scripts/teleop_node.py
chmod +x ~/mecanum_ws/src/mecanum/src/arm_teleop.py
chmod +x ~/mecanum_ws/src/mecanum/src/mecanum_control.py
chmod +x ~/mecanum_ws/src/mecanum/src/mecanum_drive_controller.py
```
## 4. Khởi chạy mô phỏng

```bash
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:~/mecanum_ws/src
cd ~/mecanum_ws
source install/setup.bash
export LIBGL_ALWAYS_SOFTWARE=1
ros2 launch mecanum sim.launch.py
```
## 4. Công cụ bổ sung

```bash
# Đồ thị encoder 4 bánh
ros2 run rqt_plot rqt_plot
```

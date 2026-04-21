import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from builtin_interfaces.msg import Duration

class RobotController(Node):
    def __init__(self):
        super().__init__('robot_controller_node')
        
        # 1. Publisher điều khiển di chuyển (Bánh xe)
        self.cmd_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        
        # 2. Publisher điều khiển các khớp (Arm & Prismatic)
        self.joint_pub = self.create_publisher(JointTrajectory, 'set_joint_trajectory', 10)
        
        # Tạo vòng lặp điều khiển sau mỗi 0.1 giây
        self.timer = self.create_timer(0.1, self.execute_move)
        self.get_logger().info('Đang khởi động hệ thống điều khiển...')

    def execute_move(self):
        # --- ĐIỀU KHIỂN BÁNH XE ---
        vel = Twist()
        vel.linear.x = 0.2  # Tiến về phía trước 0.2 m/s
        vel.linear.y = 0.5  # Bò ngang trái 0.1 m/s (Chỉ mecanum mới làm được)
        self.cmd_pub.publish(vel)

        # --- ĐIỀU KHIỂN CÁNH TAY & KHỚP TRƯỢT ---
        traj = JointTrajectory()
        # QUAN TRỌNG: Tên này phải khớp 100% với thuộc tính name trong thẻ <joint> ở URDF
        traj.joint_names = ['Arm_Joint', 'Prismatic_Joint'] 
        
        point = JointTrajectoryPoint()
        # positions[0] cho Arm (Radian), positions[1] cho Prismatic (Mét)
        point.positions = [0.8, 0.01]  # Xoay Arm ~45 độ, nâng trượt lên 4cm
        point.time_from_start = Duration(sec=1)
        
        traj.points.append(point)
        self.joint_pub.publish(traj)

def main():
    rclpy.init()
    node = RobotController()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

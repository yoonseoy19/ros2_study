import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class TurtleSubscriber(Node):
    def __init__(self):
        super().__init__('my_subscriber')
        self.subscription = self.create_subscription(
            Pose, '/turtle1/pose', self.pose_callback, 10)

    def pose_callback(self, msg):
        self.get_logger().info(
            f'x={msg.x:.2f}, y={msg.y:.2f}, theta={msg.theta:.2f}')

def main(args=None):
    rclpy.init(args=args)
    node = TurtleSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

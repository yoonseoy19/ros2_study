import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtlePublisher(Node):
    def __init__(self):
        super().__init__('my_publisher')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.8
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = TurtlePublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

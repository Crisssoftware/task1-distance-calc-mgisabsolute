import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from std_msgs.msg import Float64
import math

class DistanceCalculator(Node):
    def __init__(self):
        super().__init__('distance_calculator')
        self.subscription = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.pose_callback,
            10
        )
        self.publisher = self.create_publisher(Float64, '/turtle1/distance_from_origin', 10)

    def pose_callback(self, msg):
        x = msg.x
        y = msg.y
        distance = math.sqrt(x**2 + y**2)
        distance_msg = Float64()
        distance_msg.data = distance
        self.publisher.publish(distance_msg)
        self.get_logger().info(f"Distance from origin: {distance:.2f}")


def main(args=None):
    rclpy.init(args=args)
    distance_calculator = DistanceCalculator()
    rclpy.spin(distance_calculator)
    distance_calculator.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

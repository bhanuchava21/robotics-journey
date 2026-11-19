import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Talker(Node):
    def __init__(self):
        super().__init__('talker')

        #Parameters
        self.declare_parameter('message', 'Hello from Bhanu')
        self.declare_parameter('rate', 1.0) 

        self.message = self.get_parameter('message').value
        rate = self.get_parameter('rate').value

        self.publisher = self.create_publisher(String, 'chatter', 10)
        self.count = 0
        self.timer = self.create_timer(1.0/rate, self.publish_message)


    def publish_message(self):
        msg = String()
        msg.data = f'{self.message}: {self.count}'
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.count += 1


def main():
    rclpy.init()
    node = Talker()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()                
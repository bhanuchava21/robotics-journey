import time
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from example_interfaces.action import Fibonacci




class FibonacciServer(Node):
    def __init__(self):
        super().__init__('fibonacci_server')
        self.action_server = ActionServer(
            self, Fibonacci, 'fibonacci', self.execute_callback
        )

    def execute_callback(self, goal_handle):
        self.get_logger().info(f'Goal received: {goal_handle.request.order} numbers')
        feedback = Fibonacci.Feedback()
        feedback.sequence = [0, 1]

        for i in range(1, goal_handle.request.order):
            feedback.sequence.append(feedback.sequence[i] + feedback.sequence[i - 1])
            self.get_logger().info(f'Feedback: {feedback.sequence}')
            goal_handle.publish_feedback(feedback)
            time.sleep(1)

        goal_handle.succeed()
        result = Fibonacci.Result()
        result.sequence = feedback.sequence
        return result            


def main():
    rclpy.init()
    node = FibonacciServer()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()        
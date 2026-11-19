from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_first_pkg',
            executable='talker',
            parameters=[{'message': 'Namaste from launch', 'rate': 2.0}],
        ),
        Node(
            package='my_first_pkg',
            executable='listener',
        ),
    ])
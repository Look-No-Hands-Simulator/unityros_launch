from launch import LaunchDescription
from launch_ros.actions import Node
import socket

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

# You could use namespaces inside the nodes
def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('ROS_IP', default_value=IPAddr, description='IP address of machine running ROS2.'),
        Node(
            package='unity_robotics_demo',
            executable='position_service',
            name='position_service'
        ),
        Node(
            package='ros_tcp_endpoint',
            executable='default_server_endpoint',
            name='server_endpoint'
        )
    ])


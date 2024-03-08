from launch import LaunchDescription
from launch_ros.actions import Node

from ament_index_python import get_package_share_directory
from launch_ros.substitutions import FindPackageShare
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, TextSubstitution
from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription
from launch.conditions import IfCondition, UnlessCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PythonExpression

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
        ),
        Node(
            package='unity_robotics_demo',
            executable='color_publisher',
            name='color_publisher'
        )
    ])


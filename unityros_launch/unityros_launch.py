from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('ROS_IP', default_value='YOURIPHERE', description='IP of machine running ROS2.'),
        Node(
            package='unity_robotics_demo',
            namespace='',
            executable='position_service',
            name='position_service'
        ),
        Node(
            package='ros_tcp_endpoint',
            namespace='',
            executable='default_server_endpoint',
            name='server_endpoint'
        )
    ])


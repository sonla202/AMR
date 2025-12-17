from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
import os

def generate_launch_description():
    package_dir = os.path.join(os.getenv('HOME'), 'dev_ws/src/articubot_one/launch')
    rtabmap_params_path = os.path.join(package_dir, 'rtabmap_params.yaml')

    return LaunchDescription([
        Node(
            package='realsense2_camera',
            executable='realsense2_camera_node',
            name='realsense2_camera',
            parameters=[{
                'depth_module.profile': '424x240x15',  
                'rgb_camera.profile': '424x240x15',
                'enable_gyro': True,
                'enable_accel': True,
                'pointcloud.enable': True,             
                'align_depth': True,                   
                'ordered_pointcloud': True              
            }],
        ),
        
        Node(
            package='rtabmap_slam',
            executable='rtabmap',
            name='rtabmap',
            parameters=[rtabmap_params_path],  
            remappings=[
                ('/rgb/image', '/camera/color/image_raw'),
                ('/depth/image', '/camera/aligned_depth_to_color/image_raw'),
                ('/rgb/camera_info', '/camera/color/camera_info')
            ]
        )
    ])

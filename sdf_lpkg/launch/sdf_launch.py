#this is a python file to launch a single gazebo simulation
import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess


def generate_launch_description():
    
    sdf_path = os.path.join("src/sdf_lpkg/world/testbuild3.sdf") # is the path to the sdf file thats gonna be launched
    
    return LaunchDescription([
        # now the command to execute the gazebo simulation is placed here 
        ExecuteProcess(
            cmd=['gz','sim',sdf_path],
            output='screen'
        ),
    
        
    ])
#!/usr/bin/env bash
cd AirSim
ROS_PACKAGE_PATH="$ROS_PACKAGE_PATH:/sim/AirSim"
roslaunch launch/airsim.launch
# ROS_Practices

Installation of ROS in Ubuntu 14.04
http://wiki.ros.org/indigo/Installation/Ubuntu


$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'


$ sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net --recv-key 0xB01FA116


$ sudo apt-get install ros-indigo-desktop-full


$ rosdep update
$ sudo rosdep init


$ echo "source /opt/ros/indigo/setup.bash" >> ~/.bashrc
$ sudo apt-get install python-rosinstall

Install NEXTAGE Open 
http://wiki.ros.org/rtmros_nextage/Tutorials/Install%20NEXTAGE%20OPEN%20software%20on%20your%20machine


$ sudo apt-get update && sudo apt-get install ros-indigo-rtmros-nextage ros-indigo-rtmros-hironx


$ rtmlaunch nextage_ros_bridge nextage_ros_bridge_simulation.launch


$ rtmlaunch hironx_ros_bridge hironx_ros_bridge_simulation.launch   (HIRO)
$ rtmlaunch nextage_ros_bridge nextage_ros_bridge_simulation.launch (NEXTAGE OPEN)




/opt/ros/indigo/lib/python2.7/dist-packages/hironx_ros_bridge
/opt/ros/indigo/lib/python2.7/dist-packages/hrpsys/hrpsys_config.py




baron@baron-Lenovo-ideapad-310-14ISK:~$ echo $ROS_PACKAGE_PATH
/opt/ros/indigo/share:/opt/ros/indigo/stacks




ROS Tutorial




http://wiki.ros.org/ROS/Tutorials/NavigatingTheFilesystem
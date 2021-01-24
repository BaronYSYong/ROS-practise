# ROS Nextage Practice

## Environment
* Ubuntu 14.04
* ROS Indigo

## Interactive ROS Indigo environment with Docker
* https://opensource-robotics.tokyo.jp/?p=2936&lang=en

## Installation of ROS Indigo in Ubuntu 14.04
http://wiki.ros.org/indigo/Installation/Ubuntu

```
$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
$ sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net --recv-key 0xB01FA116
$ sudo apt-get install ros-indigo-desktop-full
$ rosdep update
$ sudo rosdep init
$ echo "source /opt/ros/indigo/setup.bas h" >> ~/.bashrc
$ sudo apt-get install python-rosinstall
```

## Install NEXTAGE Open 
http://wiki.ros.org/rtmros_nextage/Tutorials/Install%20NEXTAGE%20OPEN%20software%20on%20your%20machine

```
$ sudo apt-get update && sudo apt-get install ros-indigo-rtmros-nextage ros-indigo-rtmros-hironx
$ rtmlaunch hironx_ros_bridge hironx_ros_bridge_simulation.launch   (HIRO)
$ rtmlaunch nextage_ros_bridge nextage_ros_bridge_simulation.launch (NEXTAGE OPEN)
```

## Webpage
* http://wiki.ros.org/rtmros_nextage/Tutorials
* http://wiki.ros.org/rtmros_nextage/Tutorials/Programming_Hiro_NEXTAGE_OPEN_RTM
* http://docs.ros.org/indigo/api/hironx_rpc_server/html/
* https://rtmros-nextage.readthedocs.io/en/latest/
  * https://opensource-robotics.tokyo.jp/?page_id=681

## Command
* setTargetPose('rarm', [0.32, -0.18, 0.06], [-3, -1.5, 3.0], tm=3)
* setTargetPoseRelative('rarm', 'RARM_JOINT5', dz=0.01, tm=3)
* getCurrentPosition('RARM_JOINT5')
* getCurrentRPY('RARM_JOINT5')
* setJointAngle(self, jname, angle, tm)
* setJointAngles(self, angles, tm)
* setJointAnglesOfGroup(self, gname, pose, tm, wait=True)
* getJointAngles(self)

## Reference
* /opt/ros/indigo/lib/python2.7/dist-packages/hironx_ros_bridge
* /opt/ros/indigo/lib/python2.7/dist-packages/nextage_ros_bridge
* /opt/ros/indigo/lib/python2.7/dist-packages/hrpsys/hrpsys_config.py
* /opt/ros/indigo/share/nextage_ros_bridge/script/nextage.py

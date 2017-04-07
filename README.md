# ROS_Practices

## Installation of ROS in Ubuntu 14.04
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

## ROS Tutorial
http://wiki.ros.org/ROS/Tutorials/NavigatingTheFilesystem

## ROS Command
```
$ echo $ROS_PACKAGE_PATH
/opt/ros/indigo/share:/opt/ros/indigo/stacks
```

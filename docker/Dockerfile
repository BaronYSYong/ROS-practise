FROM ubuntu:trusty

RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list' && \
	apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net --recv-key 0xB01FA116 
	
RUN apt-get update && \
    apt-get install -y \
    ros-indigo-desktop-full \
    ros-indigo-rtmros-nextage ros-indigo-rtmros-hironx \
    python-rosinstall 
    
RUN rosdep init && rosdep update && \
    echo "source /opt/ros/indigo/setup.bash" >> ~/.bashrc
    
    
    

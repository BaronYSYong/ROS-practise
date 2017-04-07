from hironx_ros_bridge.ros_client import ROS_Client
from nextage_ros_bridge.nextage_client import NextageClient

from hrpsys import rtm
import argparse

import math

class NEXTAGE(NextageClient, object):
    def connect(cls):
        '''!@brief
        Modified from 
        /opt/ros/indigo/share/nextage_ros_bridge/script/nextage.py
        '''        
        parser = argparse.ArgumentParser(description='hiro command line interpreters')
        parser.add_argument('--host', help='corba name server hostname')
        parser.add_argument('--port', help='corba name server port number')
        parser.add_argument('--modelfile', help='robot model file nmae')
        parser.add_argument('--robot', help='robot modlule name (RobotHardware0 for real robot, Robot()')
        parser.add_argument('--dio_ver', help="Version of digital I/O. Only users "
                            "whose robot was shipped before Aug 2014 need to "
                            "define this, and the value should be '0.4.2'.")
        args, unknown = parser.parse_known_args()
        
        print args
        print unknown

        if args.host:
            rtm.nshost = args.host
        if args.port:
            rtm.nsport = args.port
        if not args.robot:
            args.robot = "RobotHardware0" if args.host else "HiroNX(Robot)0"
        if not args.modelfile:
            args.modelfile = "/opt/jsk/etc/NEXTAGE/model/main.wrl" if args.host else "" 

        # support old style format
        if len(unknown) >= 2:
            args.robot = unknown[0]
            args.modelfile = unknown[1]
            
    def circle_eef(self, radius=0.01, eef='larm', step_degree=5, ccw=True, duration=0.1):
        '''
        Modified from 
        http://wiki.ros.org/rtmros_nextage/Tutorials/Programming_Hiro_NEXTAGE_OPEN_RTM
        
        Moves the designated eef point-by-point so that the trajectory as a whole draws a circle.

        Currently this only works on the Y-Z plane of *ARM_JOINT5 joint.
        And it's the most intuitive when eef maintains a "goInitial" pose where circle gets drawn on robot's X-Y plane
        (see the wiki for the robot's coordinate if you're confused http://wiki.ros.org/rtmros_nextage/Tutorials/Programming#HiroNXO_3D_model_coordination).

        Points on the circular trajectory is based on a standard equation https://en.wikipedia.org/wiki/Circle#Equations

        @param radius: (Unit: meter) Radius of the circle to be drawn.
        @param step_degree: Angle in degree each iteration increments.
        @param ccw: counter clock-wise.
        @param duration: Time for each iteration to be completed.
        '''
        goal_deg = GOAL_DEGREE = 360
        start_deg = 0
        if eef == 'larm': 
            joint_eef = 'LARM_JOINT5'
        elif eef == 'rarm':
            joint_eef = 'RARM_JOINT5'
        eef_pos = self.getCurrentPosition(joint_eef)
        eef_rpy = self.getCurrentRPY(joint_eef)
        print('eef_pos={}'.format(eef_pos))
        X0 = eef_pos[0]
        Y0 = eef_pos[1]
        ORIGIN_x = X0
        ORIGIN_y = Y0 - radius
        print('ORIGIN_x={} ORIGIN_y={}'.format(ORIGIN_x, ORIGIN_y))
        i = 0
        for theta in range(start_deg, goal_deg, step_degree):
            if not ccw:
                theta = -theta
            x = ORIGIN_x + radius*math.sin(math.radians(theta))  # x-axis in robot's eef space is y in x-y graph
            y = ORIGIN_y + radius*math.cos(math.radians(theta))
            eef_pos[0] = x
            eef_pos[1] = y
            print('#{}th theta={} x={} y={} X0={} Y0={}'.format(i, theta, x, y, X0, Y0))
            self.setTargetPose(eef, eef_pos, eef_rpy, duration)
            self.waitInterpolation()
            i += 1

if __name__ == '__main__':
    robot = NEXTAGE()
    robot.init()

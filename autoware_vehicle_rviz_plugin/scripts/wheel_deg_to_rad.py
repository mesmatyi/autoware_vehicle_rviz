#!/usr/bin/env python

from signal import SIGABRT, signal
import rospy
import math

from autoware_vehicle_msgs.msg import Steering
from std_msgs.msg import Float32

pub = None

def callback(msg):
    steer = Steering()
    steer.header.stamp = rospy.Time.now()
    steer.header.frame_id = 'base_link'

    steer.data = msg.data * (math.pi/180)


    if pub is not None:
        pub.publish(steer)



if __name__ == '__main__':
    rospy.init_node('wheel_deg_to_rad')
    rospy.Subscriber('/wheel_angle_deg',Float32,callback)
    pub = rospy.Publisher('wheel_angle_rad', Steering, queue_size=10)
    rospy.spin()
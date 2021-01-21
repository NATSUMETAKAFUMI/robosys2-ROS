#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

def callback(message):
    print(message.data)

if __name__ == "__main__":
    rospy.init_node('time_sub')
    sub = rospy.Subscriber('time_search', Float64, callback)
    rospy.spin()

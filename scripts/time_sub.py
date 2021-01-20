#!/usr/bin/env python3

import rospy
from robosys2-ROS.msg import Date

def callback(message):
   print("date : %d, time : %f" % (message.date, message.time))
    
if __name__ == "__main__":
   rospy.init_node('time_sub')
   sub = rospy.Subscriber('time_search', Date, callback)
   rospy.spin()

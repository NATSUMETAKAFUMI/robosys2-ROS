#!/usr/bin/env python3

import rospy
from std_msgs.msg import Date

def talker():
   print("date : %d, time : %f" % (message.date, message.time))
    
if __name__ == '__main__':
   rospy.init_node('time_sub')
   sub = rospy.Subscriber('time_search', Date, callback)
   rospy.spin()

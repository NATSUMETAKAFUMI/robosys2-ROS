#!/usr/bin/env python3

import rospy
from std_sgs.msg import Data

def talker():
   print("data : %d, time : %f" % (message.date, message.time))
    
if __name__ == '__main__':
   rospy.init_node('time')
   sub = rospy.Subscriber('time_search', Date, callback)
   rospy.spin()

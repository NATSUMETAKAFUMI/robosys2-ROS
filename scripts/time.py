#!/usr/bin/env python3

import rospy
import datetime
from std_msgs.msg import Int32

dt_now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
rospy.init_node('time')
pub = rospy.Publisher('time_search', Int32, queue_size=1)
rate = rospy.Rate(10)
n = 0

print(dt_now)

print(dt_now.tzinfo)

while not rospy.is_shutdown():
    pub.publish(n)
    rate.sleep()

#!/usr/bin/env python3

import rospy
from datetime import datetime
from std_msgs.msg import Date

def talker():
    l = []
    d = ()
    rate = rospy.Rate(10)
while not rospy.is_shutdown():
    d.date = ' '
    l.time = ' '
    now = datetime.now()
    l = str(now)
    
    for i in range(0,10):
        d.date += l[i]
    for i in range(11,25):
        d.time += l[i]
    d.date = int(d.date.replace('_', ' '))
    d.time = float(d.time.replace(':',' '))
    pub.publish(d)
    rate.sleep()
    
if __name__ == '__main__':
    rospy.init_node('time_pub')
    pub = rospy.Publisher('time_search', Date, queue_size=1)
    talker()
    rospy.spin()

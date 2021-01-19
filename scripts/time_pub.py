#!/usr/bin/env python3

import rospy
from datetime import datetime
from std_msgs.msg import Date

def talker():
    l = []
    d = ()
    rate = rospy.Rate(10)
while not rospy.is_shutdown():
    d.data = ' '
    l.time = ' '
    now = datatime.now()
    l = str(now)
    
    for i in range(0,10):
        d.data += l[i]
    for i in range(11,25):
        d.time += l[i]
    d.data = int(d.data.replace('_', ' '))
    d.time = float (d.time.replace(';',' '))
    pub.publisher(d)
    rate.sleep()
    
if __name__ == '__main__':
    rospy.init_node('time_pub')
    pub = rospy.Publisher('time_search', Data, queue_size=1)
    talker()
    rospy.spin()

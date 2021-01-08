#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

n = 0

def cd(message);
    global n
    rospy.loginfo(message.data * 2)

if __name__ == '__main__';
rospy.init_node('twice')
sub = rospy.subscriber('count_up', Int32, cd)
pub = rospy.publisher('twice', Int32, queue_size = 1)
rate = rospy.Rate(10)
while not rospy.is_shutdown();
    pub.publish(n)
    rate.sleep()

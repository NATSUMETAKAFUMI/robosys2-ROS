#!/usr/bin/env python3

import rospy
import datetime

dt_now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))

print(dt_now)

print(dt_now.tzinfo)

#!/usr/bin/env python3
import rospy

if __name__ == '__main__':
    rospy.init_node(name="first")

    rospy.loginfo("Test node has been started.")
    
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        rospy.loginfo("hello")
        rate.sleep()
#!/usr/bin/env python

import rospy
import random
from std_msgs.msg import UInt16

def servo_publisher():
    rospy.init_node('servo_publisher')
    pub = rospy.Publisher('servo', UInt16, queue_size=10)
    rate = rospy.Rate(1)  # Frecuencia de publicación en Hz

    while not rospy.is_shutdown():
        angle = random.randrange(0, 180) # Cambia el valor aquí aleatoriamente
        pub.publish(angle)
        rate.sleep()

if __name__ == '__main__':
    try:
        servo_publisher()
    except rospy.ROSInterruptException:
        pass
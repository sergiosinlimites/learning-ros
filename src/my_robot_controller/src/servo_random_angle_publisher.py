#!/usr/bin/env python

import rospy
from std_msgs.msg import UInt16
import serial

SERIAL_PORT = '/dev/ttyACM0' # Puerto de comunicación al Arduino
BAUD_RATE = 57600 # Baudios de recepción y emisión

def servo_callback(data):
    servo_angle = data.data
    # Código para enviar el ángulo al servo conectado al Arduino
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
        ser.write(str(servo_angle).encode())
        ser.close()
    except serial.SerialException as e:
        rospy.logerr('Error al enviar datos al Arduino'.format(str(e)))

def servo_publisher():
    rospy.init_node('servo_publisher')
    rospy.Subscriber('servo', UInt16, servo_callback)
    rospy.spin()

if __name__ == '__main__':
    servo_publisher()
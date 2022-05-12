#!/usr/bin/env python
import rospy
from std_msgs.msg import #importar tipo de mensaje (float, int, etc)
# http://wiki.ros.org/msg tipos de mensajes en ROS


def chatter_callback(message):

    rospy.loginfo(rospy.get_caller_id() + " I heard %s", message) #imprimo mensaje suscrito
    pub.publish({mensaje_a_publicar})


def listener():

    global pub #variable de publicador
    
    pub = rospy.Publisher('/publicador', {tipo_de_mensaje},queue_size=50) #publica
    rospy.Subscriber("{nodo_a_suscribir}",{tipo_de_mensaje},chatter_callback) # funcion suscriptora
    rospy.init_node('listener',anonymous=True)#nombre de nodo

    rospy.spin()

if __name__ == '__main__':
    
    listener()

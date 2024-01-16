#!/usr/bin/env python3
import rclpy

from rclpy.node import Node 
from std_msgs.msg import Float32,String
from geometry_msgs.msg import Point


class basestation(Node):
    def __init__(self):
        super().__init__("basestation")# type: ignore 
        self.subscriber1 = self.create_subscription(Float32,"topic_1",self.callback1, 10 )
        self.subscriber2 = self.create_subscription(Point,"topic_2",self.callback2,10)
        self.subscriber3 = self.create_subscription(String,"topic_3",self.callback3,10)

    def callback1(self,msg:Float32):
        self.get_logger().info("Recived altitude value: "+str(msg._data))
        
    
    def callback2(self,msg:Point):
        String = f"Recieved Location Data:({msg.x}, {msg.y}, {msg.z})"
        self.get_logger().info(String)

    def callback3(self,msg:String):
        String = f"Mission Status: {msg.data}"
        self.get_logger().info(String)



def main (args=None):
    rclpy.init(args = args)
    node = basestation()
    rclpy.spin(node)
    rclpy.shutdown()


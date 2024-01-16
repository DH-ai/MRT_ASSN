
import rclpy
from rclpy.node import Node 
from random  import randint
from std_msgs.msg import String

class daughter3(Node):

    def __init__(self):
        super().__init__("d_rover3")#type: ignore
        self.publisher = self.create_publisher(String,"topic_3",10)
        self.timre = 10 #used 10s as mission not going to fail and accomplished each second
        self.create_timer(self.timre,self.timer_callback)

    def timer_callback(self):
        temp = randint(1,10)
        msg = String()
        msg.data = "Acomplished " if temp>=5 else "Failed"
        self.publisher.publish(msg)
        self.get_logger().info(msg.data)
    
def main(args = None):
    rclpy.init(args= args)
    node = daughter3()
    rclpy.spin(node)
    rclpy.shutdown()

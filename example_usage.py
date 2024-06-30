import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

class RobotState: #define a class for robot state
    def __init__(self):
        self.linear_speed = 0.0 #initial state for linear speed

robot_state = RobotState() #instance for robot state

def odom_callback(msg): #callback function for odometry message
    # Extract the linear speed from the odometry message
    linear_speed = msg.twist.twist.linear.x
    robot_state.linear_speed = linear_speed #update linear speed

def create_odom_subscriber(node): #subscription to /odom topic with queue size 10
    # called when a new message is recieved 
    node.create_subscription(Odometry, '/odom', odom_callback, 10)

def get_current_linear_speed(): #returns current speed of robot
    return robot_state.linear_speed

def create_velocity_publisher(node): #publisher to /cmd_vel topic with queue size 10
    # allows the node to publish Twist message to control of robot's velocity 
    return node.create_publisher(Twist, '/cmd_vel', 10)

def set_wheel_speed(publisher, linear_speed, angular_speed=0.0): 
# creates a Twist message to set robot's linear & angular speed 
    msg = Twist()
    msg.linear.x = linear_speed
    msg.angular.z = angular_speed
    publisher.publish(msg) #publish using publisher

def initialize_node(node_name):
    rclpy.init() # initialize ROS2 system
    node = Node(node_name) #create a node 
    create_odom_subscriber(node) #set up odometry subscriber 
    return node

def shutdown_node(node): #destroys node & shuts down system
    node.destroy_node()
    rclpy.shutdown()

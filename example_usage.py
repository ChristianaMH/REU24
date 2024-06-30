import rclpy
import pkg_ros2_library_py.ros2_library as ros2lib #import library
import time

def main(): #initialize using library
    node = ros2lib.initialize_node('example_node')

    try:
        # Create a velocity publisher
        vel_publisher = ros2lib.create_velocity_publisher(node)
        
        # Set initial wheel speed (0.5 m/s)
        ros2lib.set_wheel_speed(vel_publisher, 0.5) 
        
        # Allow some time to observe the speed change
        for _  in range(20):
            rclpy.spin_once(node, timeout_sec=0.1) #0.1 timeout to process incoming message/callback
            current_speed = ros2lib.get_current_linear_speed() #gets current speed & prints it
            print(f'Current linear speed: {current_speed}')
            time.sleep(0.1) #0.1 delay

        ros2lib.set_wheel_speed(vel_publisher, 0.0)  # Stop the robot (0.0 m/s)
        
    except KeyboardInterrupt: #stop program with key interrupt
        pass
    finally:
        ros2lib.shutdown_node(node) #ensures proper shutdown

if __name__ == '__main__':
    main() #executes main function


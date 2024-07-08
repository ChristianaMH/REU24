# Using ROS2 Library Package:
This package is used to simplify ROS2 function calls for future development. It includes basics for initializing a node, setting up a subscriber to recieve odometry messages, extracting the robot's current linear speed, as well as other functionalities described in this markdown file. This package is meant to be used as a layer of abstraction for future development.

### Library Functions
<b>RobotState Class</b>
* <b>\_\_init__(self)</b> : initializes linear speed to be stored and updated.
* <b>odom_callback(msg)</b> : executed when a new message is receieved on the '/odom' topic. This function extracts the linear speed for the odometry message and updates the linear speed attribute within the robot_state instance.
* <b>create_odom_subscriber(node)</b> : creates a subscription to '/odom' topic for the given node. This function sets the odom_callback function to be called whenever a new odometry message is receieved. This subscription has a queue size of 10.
* <b>get_current_linear_speed()</b> : returns the current linear speed of the robot. This function provides the latest linear speed extracted from the odometry messages.
* <b>create_velocity_publisher(node)</b> : creates and returns a publisher for the '/cmd_vel' topic for the given node. This publisher is used to send velocity commands (messages of type Twist) to control the robot's movement. This publisher has a queue size of 10.
* <b>set_wheel_speed(publisher, linear_speed, angular_speed)</b> : creates a Twist message with the specified linear and angular speed and publishes it to the given publisher. This function sets the wheel speeds of the robot thus controling its linear and angular velocities.
* <b>initialize_node(node_name)</b> : initializes the ros2 client library (rclpy), creates a node with the given name, and sets up the odometry subscriber for this node using the create_odom_subscriber function. This function returns the initialized node.
* <b>shutdown_node(node)</b> : destroys the given node and shuts down the ros2 client library (rclpy). This function properly terminates the node once finished with the communication.

### Example Usage Excutable
This excutable file demonstrates an example of using the ros2 library. This script initializes a node called example_node and uses the pkg_ros2_library_py pacakage to control the robot's movement. It creates a velocity publisher for the '/cmd_vel' topic and sets the robot's linear speed to 0.5 m/s. The script then enters a loop, where it processes incoming messages, retrieves the current linear speed from odometry messages, and prints it to the console every 0.1 seconds. After 20 iterations, it stops the robot by setting the speed to 0.0 m/s and shuts down the ROS2 node.

### Building the Package
#### Step 1. Connect to Docker Container
1. Open a new terminal and connect to docker (this will be terminal A).
2. Connect with 2 additional terminals (these will be terminals B and C).\
If you are unsure how to connect, follow the instructions on this [page](docker_setup.md).

#### Step 2. Navigate to the 'src' Workspace
In the terminal, type ```cd ~/yahboomcar_ros2_ws/yahboomcar_ws/src``` to navigate to the src workspace.

#### Step 3. Create Package
In the terminal, type ```ros2 pkg create pkg_ros2_library_py --build-type ament_python –dependencies rclpy –node-name ros2_library```. This will create a python package called pkg_ros2_library_py. This will hold the ros2 library with the node named ros2_library. 

If built successfully, you should see this:

![image](https://github.com/ChristianaMH/REU24/assets/106120377/9211661d-cf06-4f57-ac1b-231d4c0be501)

Now you can build the package by typing this command ```colcon build```:

![image](https://github.com/ChristianaMH/REU24/assets/106120377/24b45b12-9ec2-49ef-aeb7-7414c611a98e)

Once built, you can see your package in your src workspace:

![image](https://github.com/ChristianaMH/REU24/assets/106120377/e562151d-b66d-4275-9e58-0a4ca4cff604)

#### Step 4. Modify ros2_library.py
Navigate to where the executable files are stores: ```cd ~/yahboomcar_ros2_ws/yahboomcar_ws/src/pkg_ros2_library_py/pkg_ros2_library_py```. Here you will see the ros2_library.py file:

![image](https://github.com/ChristianaMH/REU24/assets/106120377/c1525458-4aa7-4025-8899-df79b9f62bb7)

#### Step 4. Modify ros2_library.py

Modify this file with the contents to the one in this [github](ros2_library.py).

now you can see package:

see inside pcakage:

inside (1 level up): 
![image](https://github.com/ChristianaMH/REU24/assets/106120377/8b6abc4c-39e5-4d9d-8f6b-a40ec83061b6)

inside resource: 
![image](https://github.com/ChristianaMH/REU24/assets/106120377/56c9ff3a-fccc-47fe-86df-917e085d6290)

inside test:
![image](https://github.com/ChristianaMH/REU24/assets/106120377/8847e6a3-c049-4a42-a8b0-8199365355b7)

setup.py
![image](https://github.com/ChristianaMH/REU24/assets/106120377/5f376da4-5eea-49cb-a7cd-9f4cd0b9de80)

adding to setup.py:
![image](https://github.com/ChristianaMH/REU24/assets/106120377/45dc5457-ce4b-4915-9136-22876dd13c56)




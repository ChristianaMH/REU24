# Calibrating Linear Speed
Yahboom Documentation for reference: [Linear Speed Calibration](http://www.yahboom.net/study/MicroROS-Pi5)

## Testing Linear Speed 
> [!WARNING]  
> This will require a large open area for your robot to move. Make sure the ground is clear of all objects and uneven terrain.

### Overview
This process used TF transformations to track multiple coordinate frames over time. This allows the robot to transform coordinates from one frame to the next which is needed for tasks involving navigation, localization, and sensor fusion. Specifically, we will perform a transformation from the odometry frame (odom) to the base footprint frame (base_foorprint). The odom frame represents the robot's estimated position and orinetation within the world. This is based on wheel encoders and additional sensors that can build errors over time. Unlike the odom frame, the base_footprint frame is a fixed representation of the robot's physical footprint on the ground. This is centered on the robot's center of rotation thus as the robot moves, this frame provides a consistent reference point for the robot's base. 

The transformation from odom to base_footprint is used to determine the robot's position and orientation relative to its physical footprint. This allows the robot to understand where its base is within the world which is neccessary for navigation, such as distance calculation.

The code for this can be found in this reference path: ```~/yahboomcar_ws/src/yahboomcar_bringup/yahboomcar_bringup/calibrate_linear.py```

### Step 1. Connect to Docker
1. Open a new terminal and connect to docker (this will be terminal A).
2. Connect with 2 additional terminals (these will be terminals B and C).\
If you are unsure how to connect, follow the instructions on this [page](docker_setup.md).

### Step 2. Start Data Processing Program
This program will release the TF transformation from odom to base_footprint. This change allows us to calculate the distance in which the robot has traveled and view it in the terminal. 
1. In terminal A, run this command: ```ros2 launch yahboomcar_bringup yahboomcar_bringup_launch.py```\
You should see the following output from this command. Because we have not initiated the program (robot_description), there is nothing yet to run: \
![image](https://github.com/ChristianaMH/REU24/assets/106120377/2b3f663a-8214-42c1-8cc1-3dbabcc8e8ff)
![image](https://github.com/ChristianaMH/REU24/assets/106120377/6b518174-d936-4f49-89be-fe4e50e76922)


### Step 3. Start Linear Speed Calibration Program
This is where you will see the change in speed of the robot as it executes the speed test. At first use, this will be waiting for the program execution to begin. 
1. In terminal B you opened, run this command: ```ros2 run yahboomcar_bringup calibrate_linear```

Here the program is waiting for a change in state to update:\
![image](https://github.com/ChristianaMH/REU24/assets/106120377/337d68f3-31f2-4c34-86b0-de231e62516e)

### Step 4. Execute Linear Speed Test
Now we need to open the dynamic parameter adjuster. This allows us to run the linear calibraion and test different speeds. Type this command in terminal C: ```ros2 run rqt_reconfigure rqt_reconfigure```

Here you will see a visual editor for parameter configuration. In the left column you will see a list of nodes, including <b>calibrate_linear</b> (this node is 
used to calibrate linear speed). If this node not present in the list, click the Refresh button.\
![image](https://github.com/ChristianaMH/REU24/assets/106120377/ff791402-95a1-42b4-88d6-474216f770e6)



### Step 5. Start Calibration
Click on the <b>calibrate_linear</b> node and check the <b>start_test</b> box to begin the test. In terminal B you can see the distance and error calculated as the robot travels. 

![image](https://github.com/ChristianaMH/REU24/assets/106120377/882754ef-789f-4716-b4ef-3318876fb0f7)

### Parameter Options
Here are the parameters you can change to test different conditions:
- <b>test_distance</b> : determines the distance the robot will travel (default is 1 meter forward)
- <b>speed</b> : determines the linear speed the robot will travel
- <b>tolerance</b> : determines the allowable error tolerance
- <b>odom_linear_scale_correction</b> : determines the linear speed proportional coefficient (change if test results are not cohesive)
- <b>start_test</b> : starts/stops test
- <b>direction</b> : allows calibration of the linear speed of left and right movement
- <b>base_frame</b> : determines the base coordinate system
- <b>odom_frame</b> : determines the odometer coordinate system

Once parameters have been modified, click start_test then reset start_test and start_test again to calibrate to these new modifications.

## Testing Angular Speed 
The same test can be performed on angular speed. 
angulare speed:

Follow Steps 1 & 2. In Step 3, instead type this command in terminal B: ```ros2 launch yahboomcar_bringup yahboomcar_bringup_launch.py``` This will start the car angular velocity calibration program:
![image](https://github.com/ChristianaMH/REU24/assets/106120377/475d9c73-5f7a-4e93-a7e1-a9e64046208b)

Next follow Step 4 and open the dynamic parameter adjuster with this command: ```ros2 run rqt_reconfigure rqt_reconfigure```.

Here you will see a visual editor for parameter configuration. In the left column you will see a list of nodes, including <b>calibrate_angular</b> (this node is 
used to calibrate angular speed). If this node not present in the list, click the Refresh button.\
![image](https://github.com/ChristianaMH/REU24/assets/106120377/d83c8b28-bef1-42a7-b89b-2c5b5f5e164d)

Click on the <b>calibrate_angular</b> node and check the <b>start_test</b> box to begin the test. In terminal B you can see the radius and error calculated as the robot travels. 
![image](https://github.com/ChristianaMH/REU24/assets/106120377/22642521-3c2a-4902-af08-77b048c19e5c)

### Parameter Options
Here are the parameters you can change to test different conditions:
- <b>test_angle</b> : determines the angle the robot will rotate (default is 360 degree rotation)
- <b>speed</b> : determines the linear speed the robot will travel
- <b>tolerance</b> : determines the allowable error tolerance
- <b>odom_angular_scale_correction</b> : determines the angular speed proportional coefficient (change if test results are not cohesive)
- <b>start_test</b> : starts/stops test
- <b>base_frame</b> : determines the base coordinate system
- <b>odom_frame</b> : determines the odometer coordinate system

Once parameters have been modified, click start_test then reset start_test and start_test again to calibrate to these new modifications.

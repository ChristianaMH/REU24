# Calibrating Linear Speed
Yahboom Documentation for reference: [Linear Speed Calibration](http://www.yahboom.net/study/MicroROS-Pi5)

## Testing Linear Speed 
> [!WARNING]  
> This will require a large open area for your robot to move. Make sure the ground is clear of all objects and uneven terrain.

### Step 1. Connect to Docker
A. Open a new terminal and connect to docker with this command: ```sh ros2_humble.sh```\
(add image)\
B. Open another terminal and type: ```docker ps```. This will display a list of available dockers to use.\
C. Connect to the most recent one opened (the one you are using in the previous terminal in part A) with this command:\
```docker exec -it <first 3 characters of id?> /bin/bash```\
(add image)

### Step 2. Start Data Processing Program
This program will release the TF transformation of odom->base_footprint. With this TF change, you can calculate "how far the car has gone" and input it at the terminal.\
A. In the first terminal you opened, run this command: ```ros2 launch yahboomcar_bringup yahboomcar_bringup_launch.py```\
![image](https://github.com/ChristianaMH/REU24/assets/106120377/2b3f663a-8214-42c1-8cc1-3dbabcc8e8ff)
![image](https://github.com/ChristianaMH/REU24/assets/106120377/6b518174-d936-4f49-89be-fe4e50e76922)


### Step 3. Start Linear Speed Calibration Program
This is where you will see the change in speed of the robot as it executes the speed test. At first use, this will be waiting for the program execution to begin.
A. In the second terminal you opened, run this command: ```ros2 run yahboomcar_bringup calibrate_linear```

Here the program is waiting for a change in state to update.\
![image](https://github.com/ChristianaMH/REU24/assets/106120377/337d68f3-31f2-4c34-86b0-de231e62516e)


### Step 4. Execute Linear Speed Test
To test different speed, now we need to open the dynamic parameter adjuster. Run this command in terminal C: ```ros2 run rqt_reconfigure rqt_reconfigure```

Here you will see a visual editor for parameter configuration. In the left column you will see a list of nodes, including <b>calibrate_linear</b> (this node is 
used to calibrate linear speed). If this node not present in the list, click the Refresh button.\
![image](https://github.com/ChristianaMH/REU24/assets/106120377/ff791402-95a1-42b4-88d6-474216f770e6)



### Step 5. Start Calibration
Click on the <b>calibrate_linear</b> node and check the <b>start_test</b> box to begin the test. In terminal A you can see the distance and error calculated as the robot travels. 

![image](https://github.com/ChristianaMH/REU24/assets/106120377/882754ef-789f-4716-b4ef-3318876fb0f7)

### Parameter Options
- <b>test_distance</b> : determines the distance the robot will travel (default is 1 meter forward)
- <b>speed</b> : determines the linear speed the robot will travel
- <b>tolerance</b> : determines the allowable error tolerance
- <b>odom_linear_scale_correction</b> : determines the linear speed proportional coefficient (change if test results are not cohesive)
- <b>start_test</b> : starts/stops test
- <b>direction</b> : allows calibration of the linear speed of left and right movement
- <b>base_frame</b> : determines the base coordinate system
- <b>odom_frame</b> : determines the odometer coordinate system

Once parameters have been modified, click start_test then reset start_test and start_test again to calibrate to these new modifications.

The code for this can be found in this reference path: ```~/yahboomcar_ws/src/yahboomcar_bringup/yahboomcar_bringup/calibrate_linear.py```


angulare speed:
![image](https://github.com/ChristianaMH/REU24/assets/106120377/475d9c73-5f7a-4e93-a7e1-a9e64046208b)

![image](https://github.com/ChristianaMH/REU24/assets/106120377/d83c8b28-bef1-42a7-b89b-2c5b5f5e164d)

![image](https://github.com/ChristianaMH/REU24/assets/106120377/22642521-3c2a-4902-af08-77b048c19e5c)


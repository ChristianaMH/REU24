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
```docker exec -it <first 3 characters of id?> <command>```\
(add image)

### Step 2. Start Data Processing Program
This program will release the TF transformation of odom->base_footprint. With this TF change, you can calculate "how far the car has gone" and input it at the terminal.\
A. In the first terminal you opened, run this command: ```ros2 launch yahboomcar_bringup yahboomcar_bringup_launch.py```\
(add image)

### Step 3. Start Linear Speed Calibration Program
This is where you will see the change in speed of the robot as it executes the speed test. At first use, this will be waiting for the program execution to begin.
A. In the second terminal you opened, run this command: ```ros2 run yahboomcar_bringup calibrate_linear```\
(add image)

### Step 4. Execute Linear Speed Test


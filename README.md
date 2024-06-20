# REU24
REU Summer 24 Robotics. Created by Christiana Hellenbrand

### Overview
This project uses Yahboom MicroROS Robot Pi5. The documentation for this robot can be found [here](http://www.yahboom.net/study/MicroROS-Pi5)

---
### Basic Care
${\color{orange}Battery}$
> [!WARNING]  
> You must turn off the raspberry pi before plugging it in to the power source. Not following this step can result in harm to the battery of the robot.
---
### Software Applications for Download
#### [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/raspberrypi/?lai_sr=5-9&lai_sl=l)
A VNC (Virtual Network Computing) viewer is used to remotely access and control a Raspberry Pi's graphical desktop environment from another computer. This allows users to interact with the Raspberry Pi as if they were physically connected to it, using the keyboard and mouse of the remote device. VNC is particularly useful for managing headless Raspberry Pi setups (those without a monitor, keyboard, or mouse attached) and for performing tasks remotely over a network.
#### [Angry IP Scanner](https://angryip.org/) (Optional for Setup)
Network scanner for finding raspberry pi IP address once connected to the network.

---
### Setting up Docker
Link to this [page](docker_setup.md)

---
### Linear Calibration
#### Testing Linear Movement
#### Testing Angular Movement

---
### ROS2 Related Topics
#### [What is a Docker & How does it work?](http://www.yahboom.net/public/upload/upload-html/1687333441/5%E3%80%81Enter%20the%20bot's%20docker%20container.html)
#### [Understanding ROS2 Nodes](https://docs.ros.org/en/foxy/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Nodes/Understanding-ROS2-Nodes.html)

---
### Writing Code
1. All new code/functions are written in the src folder of the workspace.\
2. After a new file is created, you must set environment variables in order to find the function package and executable file after compilation. This is done in the setup.py file.\
![image](https://github.com/ChristianaMH/REU24/assets/106120377/bd2910a7-e3af-4797-972d-61f8642e6982)
![image](https://github.com/ChristianaMH/REU24/assets/106120377/bd2910a7-e3af-4797-972d-61f8642e6982)

#### Creating a Function Package
Command to create a new function package: ```ros2 pkg create <package_name> --build-type <build-type> --dependencies <dependencies> --node-name <node-name>```

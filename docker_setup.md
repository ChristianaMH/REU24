# Docker Setup

## Overview
ROS2 contains a host which is the sever that is used to create a container (or main control) of your robot. A container, similar to a virtual machine, has an operating system but creates a small executable of the environment. It can be used to test and develop an application in one environment and run it in another. A docker builds and runs different containers. Because setting up a ROS2 enviornment can become complex, docker containers encapsulate all the dependencies, configurations, and tools to create simple and consistent development and runtime environments. Specifically, we use docker containers to isolate ROS2 from the host operating system effectively capturing the state of your environment.

### Opening a Docker Container :
When accessing the robot, a new terminal will immediately open and connect you to the most recent docker image. Will look similar to this:
![image](https://github.com/ChristianaMH/REU24/assets/106120377/8a6a57b7-b8dd-4042-b9a5-1f7eb6343119)

If this is not the case, then you can open a new terminal and type ```sh ros2_humble.sh```. This will connect you to a docker container. 

### Opening multiple terminals:
After connecting to the first docker container, open a new terminaland type ```docker ps```.
This will show all the available containers to use:
![image](https://github.com/ChristianaMH/REU24/assets/106120377/11e89e01-477f-44b5-86ef-c48188e602f1)

Use the most recent docker container that incluedes the command <b>"bin/bash"</b>. In this example, the docker would be container ID 844f6063ab4d. Note: this will not be the same for you.

To connect to this docker, type ```docker exec -it <first 3 characters of container ID> /bin/bash```. In the example used, this command would be ```docker exec -it 844 /bin/bash```.

If successful, the domain ID will match the ID used in your first terminal.
![image](https://github.com/ChristianaMH/REU24/assets/106120377/2eafdbbc-bf32-4ff1-81bf-92646dae61af)

Now you can use multiple terminals in one docker image. 


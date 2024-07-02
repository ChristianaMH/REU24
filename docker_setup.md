# Docker Setup

Opening A docker:

When accessing the robot, a new terminal will immediately open and connect you to the most recent docker image. Looks like this:
![image](https://github.com/ChristianaMH/REU24/assets/106120377/8a6a57b7-b8dd-4042-b9a5-1f7eb6343119)

If this is not the case, open a new terminal and type ```sh ros2_humble.sh```. This will connect you to the docker. 

Opening multiple terminals:
After connecting to the first docker, open a new terminaland type ```docker ps```.
This will show all the available dockers to use.

![image](https://github.com/ChristianaMH/REU24/assets/106120377/11e89e01-477f-44b5-86ef-c48188e602f1)

Use th most recent docker that incluedes the "command bin/bash". In this case, the docker would be container ID 844f6063ab4d. Note: this will not be the same for you.

To connect to this docker, type ```docker exec -it <first 3 characters of container ID> /bin/bash```. In the example used, this command would be ```docker exec -it 844 /bin/bash```.

If successful, the domain ID will match the ID used in your first terminal.
![image](https://github.com/ChristianaMH/REU24/assets/106120377/2eafdbbc-bf32-4ff1-81bf-92646dae61af)

Now you can use multiple terminals in one docker image. 


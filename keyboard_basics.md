# Keyboard Basics

This tutorial will go over how to control robot movements with a keyboard.

### Step 1. Connect to Docker
1. Open a new terminal and connect to docker (this will be terminal A).
2. Connect with 2 additional terminals (these will be terminals B and C).\
If you are unsure how to connect, follow the instructions on this [page](docker_setup.md).

### Step 2. Find the Agent Node
In the terminal, type ```ros2 node list```. This will show you a list of all active nodes. You should see '/YB_Car_Node'. This is our agent node.

### Step 3. Begin Keyboard Control
Next type ```ros2 run yahboomcar_ctrl yahboom_keyboard```. This will start your keyboard control program. If successfully connected, your terminal will look like this:

![image](https://github.com/ChristianaMH/REU24/assets/106120377/1c0a6b57-e610-4806-8b5e-ed112026e009)

### Keyboard Controls
Directional Controls:

![image](https://github.com/ChristianaMH/REU24/assets/106120377/3c539bd0-7155-45a0-90a8-00707db20e75)

Speed Controls:

![image](https://github.com/ChristianaMH/REU24/assets/106120377/51e922b2-53cb-4030-9212-c55d2fc89cb2)


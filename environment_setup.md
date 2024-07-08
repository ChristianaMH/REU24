## Environment Setup
This document will walk you through the steps for setting up the environment for your Raspberry Pi. This will require connecting to WiFi, however you can choose to follow the pre-configured WiFi method (simple) or the new WiFi connection method (requires more work).

### Pre-Configured WiFi Method
This tutorial provides a basic setup using a pre-configured network (<b>RoboBulls_Network_ENG202B</b>). The prequist for this page includes downloading [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/raspberrypi/?lai_sr=0-4&lai_sl=l). Download before continuing. 

First connect to RoboBulls_Network_ENG202B (password provided by the lab) and turn on your robot. Wait 1-5 minutes for the robot to start up. 
![image](https://github.com/ChristianaMH/REU24/assets/106120377/6a17e6b0-9d23-4c1f-bb54-69baa3b4cf9b)

The IP address for the Raspberry Pi is <b>192.168.1.188</b>. In the VNC Viewer, type this address in the top address bar. If successfully, this will prompt you to type a username and password (Enter the username: Root and password: 12345678). This can also be found in the back of the robot's handbook. After successful connection, this connetion will appear on your home page for you to connect to in the future: 
![image](https://github.com/ChristianaMH/REU24/assets/106120377/7f77e693-d843-4540-bce9-be24e82bd638)


---
### New WiFi Connection Method
This tutorial is specifically for connecting the robot to your own WiFi. There are two options for setup: 

<b>Option A: </b> Connect with a monitor
If you have a monitor, ethernet cable, and a micro hdmi cord, you can connect your Raspberry Pi directly to the monitor. However, this requires removing the casing.

<b>Option B: </b> 
Note: this requires an existing connection to the robot. It is suggested to use the previous tutorial to do so. 

Within the Raspberry Pi interface, click on the WiFi icon in the top right corner. Go to Advance Options and Edit Connections. 

![image](https://github.com/ChristianaMH/REU24/assets/106120377/543729c2-b145-4240-8741-9207f00a066b)

Click the '+' in the lower left corner to create a new WiFi connections. Select the Wireless option for Connection Type. 

![image](https://github.com/ChristianaMH/REU24/assets/106120377/726f1057-821c-455b-a51e-c30c44666896)

Under Wireless secion, the SSID will be the name of you WiFi. Also rename the Connection Name to your WiFi name as well. Under General, check the box for "Connect automatically with priority" and set the priority to a value greater than 1. 

![image](https://github.com/ChristianaMH/REU24/assets/106120377/64d23836-01ad-43b6-ab02-b25f9302688e)

If there is a password: under Wireless Security, select WPA/WPA2/WPA3 Personal and type your WiFi password. 

![image](https://github.com/ChristianaMH/REU24/assets/106120377/8ce003c7-83a5-48a2-a5e5-84a7dbaa2fe0)

Click save and exit. Now your Raspberry P will prioritize your WiFi when connecting to WiFi. This will take into affect after restarting your Raspberry Pi. 

Once connected to the WiFi, now you can search for the IP address of this connection. Use the IP Scanner (linked [here](environment_setup.md))to scan for the Pi5. Once found, this will be the IP used to connect to the Pi5. 

Note: you may have to try different IP addresses to find the right one. 

Type the IP address into the top bar of the VNC viewer. Enter the username: <b>Root</b> and password: <b>12345678</b>. If successfully, you will see the Raspberry Pi interface.


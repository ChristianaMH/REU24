## Python Function Packages
### Overview
Function packages are used to organize, manage, and distribute sets of related functionality, facilitating the development of robotic applications. These packages contain nodes, libraries, configuration files, and other resources necessary for specific tasks or functionalities within a robotic system. ROS2 packages allow developers to break down complex robotic applications into smaller, manageable, and reusable components. ROS2 packages can be easily shared and distributed within the ROS2 community, enabling developers to leverage existing solutions and contribute their own. Packages help manage namespaces and avoid conflicts by encapsulating related functionalities within a distinct package namespace.

---
### ROS2 Package Structure
ROS2 packages includes several files & folders. When a new package is built, the file structure will look like this:\
![image](https://github.com/ChristianaMH/REU24/assets/106120377/c4da06e6-76b8-4b2a-99f4-6b023f01d78c)

* /<package_name> - (example shows as my_ros) a directory with the same name as your package, used by ROS 2 tools to find your package, contains \_\_init__.py
* \_\_init__.py - used to initialize python package; sets up different package settings, variables, and imports to include
* package.xml - file containing meta information about the package including name, version, description, maintainer info, license, dependencies, etc.
* resource - folder that holds files needed by nodes or scripts to run launch and configuration files 
* setup.py - containing instructions for how to install the package
* setup.cfg - required when a package has executables, so ```ros2 run``` can find them
* test - folder that stored unit, integration, and script-related tests to ensure correct code behavior

Function packages can be written in either C or Python. In this tutorial, we will be creating a package in Python. 

### Steps
1. Connect to docker and navigate to src folder with this command: ```cd ~/yahboomcar_ros2_ws/yahboomcar_ws/src```
2. Use this command to create a new python package: ```ros2 pkg create --build-type ament_python <pkg_name>```. \
Replace <pkg_name> with the name of your pacakge. Include '''--node-name <node_name>``` if you'd like to include a Hello World executable (recommended).
3. For example, to create a package called 'test_pkg' with a node called 'test_node', we would type: ```ros2 pkg create --build-type ament_python test_pkg --node-name test_node```
4. After running this command, a new folder within your src workspace will appear.
5. To all packages in src, run ```colcon build```. To build only your new package, run ```colcon build --packages-select <pkg_name>``. Any errors with your package will be shown here.
6. After your package has been built, run ```source install/local_setup.bash``` to source the setup file. This will allow you to use your package's executables.
7. To run the excutable that you created using --node-name, run this command: ```ros2 run <pkg_name> <node_name>```. This will return a message that says "Hi from <pkg_name>".

### Modifying Executable
You can edit the executable file to write code for your package by going ```cd ~/yahboomcar_ros2_ws/yahboomcar_ws/src/pkg_name/pkg_name/node_name```. Any changes to this code will require you to redo <b>Steps 4 and 5</b> to see these changes. 

### Adding Multiple Executable Files
Additionally, any new files should be put in the ```~/yahboomcar_ros2_ws/yahboomcar_ws/src/pkg_name/pkg_name``` folder. In order to run any new file, it should be added to the <b>setup.py</b> file within the <b>console_scripts</b> list. It will look similar to this: \
![image](https://github.com/ChristianaMH/REU24/assets/106120377/0695657a-f518-4ed1-bf68-97ac9c0e35a3)

* my_node = the executable name to run the file in <b>Step 7</b> (replaces node_name)
* my_py_pkg.my_node = the location of the file to execute (located in pkg folder; only need to include the folder and any sub-route to get to the file name)
* :main = the name of the starting function (should be main)

For example, lets say we created a new file in the ... /pkg_test/pkg_test folder called test.py that includes a main function. To add this file to our setup, we would add to the console_scripts: ```'test_exec = pkg_test.test:main```. After building this package and sourcing the setup file, we can execute this file by typing ```ros2 run pkg_test test_exec```. 



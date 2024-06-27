## Python Function Packages
### Overview
Function packages are used to organize, manage, and distribute sets of related functionality, facilitating the development of robotic applications. These packages contain nodes, libraries, configuration files, and other resources necessary for specific tasks or functionalities within a robotic system. ROS2 packages allow developers to break down complex robotic applications into smaller, manageable, and reusable components. ROS2 packages can be easily shared and distributed within the ROS2 community, enabling developers to leverage existing solutions and contribute their own. Packages help manage namespaces and avoid conflicts by encapsulating related functionalities within a distinct package namespace.

---
### ROS2 Package Structure
ROS2 packages includes several files & folders:
* package.xml - file containing meta information about the package
* setup.py - containing instructions for how to install the package
* setup.cfg - required when a package has executables, so ```ros2 run``` can find them
* /<package_name> - a directory with the same name as your package, used by ROS 2 tools to find your package, contains __init__.py

When a new package is built, the file structure will look like this:
  hjkl


Function packages can be written in either C or Python. In this tutorial, we will be creating a package in Python. \ 

# Bandwidth_Usage
This project aims to develop a standalone software application using Python that measure and categorizes network bandwidth usage across various services and applications on a host machine.. The primary objective is to provide end-users with clear, actionable insights into where their network data is being consumed.

Display all the processes that use data connection, sent and received per PID/Application
This requires administrators priviledges 


## CORE OBJECTIVES
**Real-time Tracking:** Monitors upload and download metrics<br>
**Categorization:** Attribute data usage to specific application names (e.g. Chrome, Mail)  

**Transparency:** Highlight “hidden” background processes that may be consuming data.<br>
<br>
<br>
## TECHNICAL ARCHITECTURE
The application is built using Python3.x and leverages the python libraries:<br>
psutil
time
os
ctypes
collections


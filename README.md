# Bandwidth_Usage
This project aims to develop a standalone software application using Python that measure and categorizes network bandwidth usage across various services and applications on a host machine.. The primary objective is to provide end-users with clear, actionable insights into where their network data is being consumed.

Display all the processes that use data connection, sent and received per PID/Application
This requires administrators priviledges 


## CORE OBJECTIVES
**Real-time Tracking:** Monitors upload and download metrics  
**Categorization:** Attribute data usage to specific application names (e.g. Chrome, Mail)  
**Transparency:** Highlight “hidden” background processes that may be consuming data.  
  
  
## TECHNICAL ARCHITECTURE
The application is built using Python3.x and leverages the python libraries:  
&emsp;***psutil***  
&emsp;***time***  
&emsp;***os***  
&emsp;***ctypes***  
&emsp;***collections***  


## INSTALLATION AND REQUIREMENTS
Ensure that the following requirements are met before running the application:  
&emsp; **System Requirements**  
&emsp; &emsp; **Operating System:*** Windows 10/11, Linux, or MacOS  
&emsp; &emsp; **Permissions:** Administrative/Sudo privileges are required for effective results  
&emsp; **Dependencies**  
&emsp; &emsp; Install the required library via pip:  
&emsp; &emsp; ***pip install psutil***  


## SOFTWARE USAGE
1-	Open your terminal or Command Prompt as Administrator  
2-	Navigate to the script directory  
3-	Execute the script:  
&emsp; ***python BandwidthUsageApp.py***  

**Interface Guide**  

**PID>>**	The unique process identifier assigned by the operating system.  
**Application>>**	The name of the executable file (e.g., Chrome.exe, MSword.exe).  
**Sent (MB)>>**	Total megabytes uploaded since monitoring started.  
**Received (MB)>>**	Total megabytes downloaded since monitoring started.  


## LOGIC FLOW
**Initialization:** The application captures the current read_bytes and write_bytes of all running apps.  
**The loop:** Every 1 second (Refresh rate), the application re-scans active connections.  
**Display:** The user interface clears and repaints the table, sorting applications by the highest “Received” data  

## LIMITATIONS
**I/O vs Network:** On windows operating system, the application tracks total I/O (Disk + Network). For network heavy apps, this is highly accurate, but it may include local file writes.  
**Persistence:** Usage data is stored in a volatile memory, closing the application, it resets the session totals.  

** - - - Enjoy The App - - - **

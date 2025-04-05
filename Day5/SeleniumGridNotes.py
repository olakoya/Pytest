'''
Selenium Grid
-------------
- We can run our test cases on multiple machines
- Allow testing on different browser instances
- Enable cross platform testing
- Parallel testing

Selenium Grid allows the execution of WebDriver scripts on remote machines by routing commands sent by the client to remote browser instances.

selenium grid works on hub and node concept
Hub will be in clinet machine

Hub (From where we have written test cases, executing test cases, controlling entire setup)
Node (Remote machine from where we want to execute our Test Cases on which browser and OS)

Hub is setup in the client machine itself.
Through grid setup we can attach all Nodes to hub.From hub each and evey node will be controlled.
Entire Grid should be connected to single network.In real time in companies we will have one single network where we will setup all..
When we run test cases from the hub in the hub itself we will specify which OS and Browser we want to run our Test Cases.
Based on that Hub will identify the node with that configuration and sends that test cases.

nodes
	vm
	Docker Images

Setup selenium grid
-------------------
Prerequite
----------
	java

Standalone setup (single machine acting as a hub and Node)
----------------------------------------------------------
Download selenium-server-4.xx.x.jar and place it somewhere.
Run below command to start Selenium Grid
	java -jar selenium-server-4.xx.x.jar standalone
URL to see sessions:  http://localhost:4444/


Distributed setup (Hub and Node setup) (Multiple machines acting as a hub and Nodes)
--------------------------------------------------------------------------------------
Download selenium-server-4.xx.x.jar and place it somewhere in both (hub & node) the machines.
Run below command to make machine as hub
	java -jar selenium-server-4.xx.x.jar hub
Run below command to make machine as node
	java -jar selenium-server-4.xx.x.jar node --hub http://<hub-ip>:4444
Example
	java -jar '/home/kmr/Desktop/selenium-server-4.25.0.jar' node --hub 		http://192.168.1.6:4444 --selenium-manager true
URL to see sessions:  http://localhost:4444/


Concurrency is parallelism..


hub_url
----------
URL of IP ADDRESS OF HUB MACHINE + HUB PORT +/wd/hub


http://172.20.64.1:4444/wd/hub

'''
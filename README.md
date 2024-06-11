# Performance Comparison of Deadlock Solution Algorithms

This project simulates various deadlock resolution algorithms in an operating system context. The script generates random resource allocation scenarios and evaluates the performance of different algorithms for handling deadlocks.

--------------------------------------------------

# Description
* The script simulates different deadlock resolution algorithms and compares their performance in terms of average resolution time. The algorithms included are:

* Banker's Algorithm
* Preallocation
* Timeout
* Wait-Die
* Wound-Wait
* The script uses random resource allocation and different distribution methods (uniform, normal, custom) to simulate various scenarios.

------------------------------------------------------------

# Prerequisites
* Python 3.x
* Matplotlib
* Time module (included in Python standard library)
* Random module (included in Python standard library)

---------------------------------------

# Installation
* Ensure you have Python 3 installed on your system. You can download it from python.org.
* Install Matplotlib if you don't have it already:
* pip install matplotlib

------------------------------

# Usage
* Clone the repository or download the DEADLOCK.py file.
* Run the script using Python:
* python DEADLOCK.py
* Follow the prompt to input the number of resources.
* The script will display the results of the deadlock resolution algorithms and plot the performance comparison. 

-----------------------------------------

# Algorithms
* Banker's Algorithm
A resource allocation and deadlock avoidance algorithm that tests for the safety of a state by simulating the allocation for predetermined maximum possible amounts of all resources, and then makes an "s-state" check to test for possible activities before deciding whether allocation should be allowed to continue.

* Preallocation
Allocates resources to processes in advance based on their maximum requirements to avoid deadlock situations.

* Timeout
If a process is unable to obtain the resources it needs within a certain time frame, it is assumed to be in a deadlock and its resources are released.

* Wait-Die
A preemptive scheme where older processes wait for younger ones to release resources, while younger processes are aborted and restarted if they request resources held by older processes.

* Wound-Wait
A preemptive scheme where older processes can preempt younger processes by forcing them to release resources and restart.

----------------------------------------------

# Simulation
* The script runs simulations for different numbers of processes and for each of the deadlock resolution algorithms. It measures the average time taken to resolve * deadlocks under different distributions of resource requests:

* Uniform Distribution: Resources are requested uniformly across the range.
* Normal Distribution: Resources are requested based on a normal distribution with a mean and standard deviation.
* Custom Distribution: Resources are requested based on a custom distribution defined by the user.

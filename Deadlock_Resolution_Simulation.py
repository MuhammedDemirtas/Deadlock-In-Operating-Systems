# Deadlock Resolution Simulation
# Developer: M. Demirtaş
# Description: A Python program to simulate deadlock resolution algorithms with various resource distributions.
# License: [Specify License, e.g., MIT, GPL, or any custom license]


import random
import matplotlib.pyplot as plt
import time

# Prompt the user to input the number of resources
resource_count = int(input("Enter the number of resources: "))

# Define the number of processes
process_counts = [20, 30, 50, 80, 100]

# Maximum resources each process can request initially
max_resources = []
for _ in range(resource_count):
    max_resources.append(random.randint(1, resource_count))

print("Maximum Resources: ", max_resources)
print("*****")

# Initial available resources for each process
available_resources = []
for i in range(resource_count):
    available_resources.append(random.randint(1, max_resources[i]))

print("Available Resources: ", available_resources)
print("*****")

# Process class
class Process:
    def __init__(self, process_id):
        # Initialize process attributes
        self.process_id = process_id
        self.request = []

        for i in range(resource_count):
            self.request.append(random.randint(1, max_resources[i]))

        # Initialize the resources held by the process as 0
        self.held_resources = [0] * resource_count

# Generate distributions for resource allocation
def random_distribution(resource_count, distribution_type):
    if distribution_type == "uniform":
        uniform = []
        for i in range(resource_count):
            uniform.append(random.randint(1, resource_count))
        return uniform

    elif distribution_type == "normal":
        normal = []
        for i in range(resource_count):
            mean = resource_count / 2
            std_dev = resource_count / 6
            normal.append(max(1, round(random.gauss(mean, std_dev))))
        return normal

    elif distribution_type == "custom":
        # Define custom ranges based on resource count
        ranges = [i + 1 for i in range(resource_count)]
        custom = []
        for i in range(resource_count):
            custom.append(random.choice(ranges))
        return custom

print("Uniform Distribution: ", random_distribution(resource_count, "uniform"))
print("Normal Distribution: ", random_distribution(resource_count, "normal"))
print("Custom Distribution: ", random_distribution(resource_count, "custom"))
print("*****")

# Create a deadlock scenario
def create_deadlock(processes, distribution_type):
    process = random.choice(processes)
    request = random_distribution(resource_count, distribution_type)

    for i in range(resource_count):
        available_resources[i] -= request[i]
        process.held_resources[i] += request[i]

# Preallocation algorithm
def preallocation(processes):
    for process in processes:
        if sum(process.held_resources) == sum(process.request):
            for i in range(resource_count):
                available_resources[i] += process.held_resources[i]
            process.held_resources = [0] * resource_count

# Timeout handling
def timeout(processes):
    for process in processes:
        if sum(process.held_resources) == sum(process.request):
            for i in range(resource_count):
                available_resources[i] += process.held_resources[i]
            process.held_resources = [0] * resource_count
        else:
            process.held_resources = [0] * resource_count

# Wait-Die algorithm
def wait_die(processes):
    for process in processes:
        if sum(process.held_resources) == sum(process.request):
            for i in range(resource_count):
                available_resources[i] += process.held_resources[i]
            process.held_resources = [0] * resource_count
        else:
            if check_process_youth(process):
                for i in range(resource_count):
                    available_resources[i] += process.held_resources[i]
                process.held_resources = [0] * resource_count

# Wound-Wait algorithm
def wound_wait(processes):
    for process in processes:
        if sum(process.held_resources) == sum(process.request):
            for i in range(resource_count):
                available_resources[i] += process.held_resources[i]
            process.held_resources = [0] * resource_count
        else:
            if check_process_youth(process):
                for i in range(resource_count):
                    available_resources[i] += process.held_resources[i] // 2
                    process.held_resources[i] = process.held_resources[i] // 2

# Process youth check
def check_process_youth(process):
    return process.process_id % 2 == 0

# Banker's algorithm
def bankers(processes):
    temp_available = available_resources.copy()
    temp_held = [process.held_resources.copy() for process in processes]

    for process in processes:
        for i in range(resource_count):
            if temp_available[i] >= process.request[i] - temp_held[process.process_id][i]:
                for j in range(resource_count):
                    temp_available[j] += temp_held[process.process_id][j]
                    temp_held[process.process_id][j] = 0
            else:
                process.held_resources = temp_held[process.process_id]

# Run simulation for algorithms and return average execution time
def run_simulation(algorithm, process_count, distribution_type, iterations=100):
    total_time = 0.0
    processes = []

    for iteration in range(iterations):
        for process_id in range(process_count):
            processes.append(Process(process_id))
            create_deadlock(processes, distribution_type)
            start_time = time.time()
            algorithm(processes)
            end_time = time.time()
            total_time += end_time - start_time

    return total_time / iterations

algorithms = [bankers, preallocation, timeout, wound_wait, wait_die]
distribution_types = ['uniform', 'normal', 'custom']

plt.figure(figsize=(15, 15 * len(distribution_types)))

for idx, distribution_type in enumerate(distribution_types, 1):
    plt.subplot(len(distribution_types), 1, idx)
    results = {}

    for algorithm in algorithms:
        execution_times = []
        for process_count in process_counts:
            avg_time = run_simulation(algorithm, process_count, distribution_type=distribution_type)
            execution_times.append(avg_time)
            print(f"{algorithm.__name__} - {process_count} Processes - {distribution_type.capitalize()} Distribution: Avg Time {avg_time:.6f} seconds")

        results[f"{algorithm.__name__}"] = execution_times
        plt.plot(process_counts, execution_times, label=f"{algorithm.__name__}")

    plt.title(f"Performance Comparison of Deadlock Resolution Algorithms - {distribution_type.capitalize()} Distribution")
    plt.xlabel("Number of Processes")
    plt.ylabel("Average Execution Time (seconds)")
    plt.legend()

plt.tight_layout()
plt.show()

# Part 2: Python Script
# Author: Saquib Ahmed Khan - 100949697
# Below is a Python script simulating auto-scaling based on traffic data. This code includes data generation, scaling logic, and visualization.

import random
import matplotlib.pyplot as plt

# Constants for auto-scaling behavior
MIN_INSTANCES = 1  # Minimum number of instances
MAX_INSTANCES = 10  # Maximum number of instances
SCALE_UP_THRESHOLD = 70  # CPU usage (%) to scale up
SCALE_DOWN_THRESHOLD = 30  # CPU usage (%) to scale down
TRAFFIC_SAMPLES = 50  # Number of traffic data points to simulate

# Function to generate simulated traffic data
def generate_traffic_data(num_samples):
    """
    Generates random traffic data representing CPU usage (%).
    Args:
        num_samples (int): Number of traffic samples to generate.
    Returns:
        list: A list of random CPU usage values between 10% and 100%.
    """
    return [random.randint(10, 100) for _ in range(num_samples)]

# Function to implement auto-scaling logic
def simulate_auto_scaling(traffic_data):
    """
    Simulates the behavior of an auto-scaling system based on traffic data.
    Args:
        traffic_data (list): List of traffic (CPU usage) values.
    Returns:
        list: History of instance counts at each time step.
    """
    current_instances = MIN_INSTANCES
    instance_history = []

    # Process each traffic value to adjust instances
    for cpu_usage in traffic_data:
        if cpu_usage > SCALE_UP_THRESHOLD and current_instances < MAX_INSTANCES:
            current_instances += 1  # Scale up by adding an instance
            print(f"Traffic: {cpu_usage}% - Scaling up to {current_instances} instances.")
        elif cpu_usage < SCALE_DOWN_THRESHOLD and current_instances > MIN_INSTANCES:
            current_instances -= 1  # Scale down by removing an instance
            print(f"Traffic: {cpu_usage}% - Scaling down to {current_instances} instances.")
        else:
            print(f"Traffic: {cpu_usage}% - No scaling action needed. Instances: {current_instances}")
        
        instance_history.append(current_instances)  # Record the current instance count

    return instance_history

# Function to visualize the results
def plot_auto_scaling(traffic_data, instance_history):
    """
    Plots the traffic data and instance count over time.
    Args:
        traffic_data (list): List of traffic (CPU usage) values.
        instance_history (list): List of instance counts over time.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(traffic_data, label='Traffic (CPU %)', marker='o', color='blue')
    plt.plot(instance_history, label='Instances', marker='x', color='orange')
    plt.axhline(SCALE_UP_THRESHOLD, color='green', linestyle='--', label='Scale Up Threshold')
    plt.axhline(SCALE_DOWN_THRESHOLD, color='red', linestyle='--', label='Scale Down Threshold')
    plt.title('Auto-Scaling Simulation')
    plt.xlabel('Time Steps')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.show()

# Main function to orchestrate the simulation
def main():
    """
    Main function to simulate traffic and auto-scaling behavior.
    """
    print("Starting auto-scaling simulation...")
    traffic_data = generate_traffic_data(TRAFFIC_SAMPLES)  # Generate traffic
    instance_history = simulate_auto_scaling(traffic_data)  # Simulate auto-scaling
    plot_auto_scaling(traffic_data, instance_history)  # Visualize the results

# Entry point of the script
if __name__ == "__main__":
    main()

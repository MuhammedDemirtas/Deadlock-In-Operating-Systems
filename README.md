# Deadlock Resolution Simulation

This Python-based program simulates deadlock scenarios and evaluates different algorithms to resolve them. It provides a comparative analysis of various algorithms' performance in handling deadlocks under different resource allocation strategies.

---

## Features

### Simulation Overview
- Simulates multiple processes competing for shared resources.
- Generates resource allocation requests using different distributions (Uniform, Normal, Custom).
- Implements several deadlock resolution algorithms.

### Deadlock Resolution Algorithms
- **Banker's Algorithm**: Checks for a safe state by simulating allocation requests.
- **Preallocation**: Frees resources preemptively based on process completion.
- **Timeout**: Releases resources if a process exceeds a set time limit.
- **Wait-Die**: Older processes wait while younger ones release resources.
- **Wound-Wait**: Older processes preempt resources from younger ones.

### Visualization
- Uses Matplotlib to plot the performance comparison of algorithms under various distributions and process counts.
- Clear, comparative graphs showing average resolution times.

---

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.8 or higher
- Required Python libraries: Matplotlib, Random

### Clone the Repository
```bash
git clone https://github.com/MDemirtas/Deadlock-Resolution-Simulator.git
cd Deadlock-Resolution-Simulator
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

---

## Running the Simulation

1. Run the main script to execute the simulation:
```bash
python main.py
```

2. Input the required parameters when prompted, such as:
   - Number of resources.
   - Number of processes.
   - Distribution type (Uniform, Normal, or Custom).

3. View the simulation results and performance graphs.

---

## File Structure

- **`main.py`**: Entry point of the simulation.
- **`deadlock.py`**: Contains logic for deadlock generation and resolution.
- **`visualize.py`**: Handles performance graphing.
- **`requirements.txt`**: Lists required Python libraries.

---

## Example Usage

### Input Example
- **Resource Count**: 5
- **Process Count**: 50
- **Distribution**: Normal

### Output
- Average resolution time for each algorithm under the specified settings.
- Visualization of algorithm performance as line plots.

---

## Results
The program generates plots comparing the average resolution times of different algorithms under various conditions. For example:

- Banker's Algorithm performs well under balanced allocations.
- Timeout is faster for fewer processes but less efficient for high loads.
- Wait-Die and Wound-Wait demonstrate variable efficiency based on resource contention.

---

## Contributing
Contributions are welcome! Please:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request for review.

---

## Author
**M. Demirtaş**

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.


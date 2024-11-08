# Serial Device Control Project

This project enables communication and control of devices via a serial interface, supporting various commands and protocols. It includes scripts for reading data, managing serial commands, and working with specific device firmware. Ideal for use in environments where direct communication with hardware is needed, such as robotics or IoT projects.

## Project Structure

- **camara.py** - Script for handling camera-related functionality (e.g., capturing images or managing video streams).
- **firmware/** - Directory containing firmware files for specific device configurations (might not be needed).
- **mpy.py** - A module for managing microcontroller interactions.
- **read.py** - Basic script to read data from connected devices.
- **requrements.txt** - File containing required Python libraries for the project.
- **seral.py** - Core script for sending and managing commands via serial communication. Handles bytecode commands for device control (e.g., how to control your robot).
- **bleak.py** - Utility script with auxiliary functions for device interactions (experimental).
- **test_ble.py** - Script for testing BLE (Bluetooth Low Energy) functionality.

## Getting Started

### Prerequisites

To run this project, ensure you have Python installed.

### Setting Up the Conda Development Environment

1. **Create the Conda environment**:
   Navigate to the project directory and create a new Conda environment named `hackathon3` with Python 3.x (replace `x` with your desired version, e.g., 3.8):

   ```bash
   conda create -n hackathon3 python=3.x
   ```

2. **Activate the environment**:
   Activate the newly created environment:

   ```bash
   conda activate hackathon3
   ```

3. **Install dependencies**:
   With the environment active, install the required libraries from `requrements.txt`:

   ```bash
   pip install -r requrements.txt
   ```

### Usage

1. **Serial Communication**:
   - Run `seral.py` to control connected devices via serial commands. This script manages motor and servo movements with a specific byte command format.
   - Example usage:

     ```bash
     python seral.py
     ```

2. **Reading Device Data**:
   - Use `read.py` to read incoming data from the connected device.
   
3. **Testing BLE Functionality**:
   - Use `test_ble.py` to initiate and test Bluetooth communication with devices that support BLE.

4. **Camera Operations**:
   - Use `camara.py` to manage camera functions, such as image capturing or streaming.

## Additional Resources

- **Makeblock-Libraries-master.zip**: Contains additional libraries for extended functionality with Makeblock devices

## License

This project is licensed under MIT.

## Acknowledgments

Thanks to the open-source libraries and firmware that support this project’s capabilities.

---

For more detailed information, refer to each script's inline documentation.

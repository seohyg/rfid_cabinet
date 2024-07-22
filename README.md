# Project BOM and Setup Guide

## Bill of Materials (BOM)

| Item                  | Quantity |
|-----------------------|----------|
| BOM 12-200 PSU        | 1        |
| Raspberry Pi 5        | 1        |
| SRD-03VDC-SL-C Relay  | 1        |
| 1K Resistor           | 1        |
| Breadboard            | 1        |
| Solenoid              | 1        |

## Instructions

![Api_test](https://github.com/user-attachments/assets/e0354c22-a273-45de-8216-2d9fddf6db78)

The project is divided into sections for solenoid operation test and API test. 
Assemble the BOM as shown in the diagram below. Note that the diagram may show different components such as an SSR and a 12V PSU. 
It is important to install a pull-down resistor in front of the solenoid.


## Enabling SSH on Raspberry Pi 5

1. Open the terminal on your Raspberry Pi.
2. Execute the following command to enable SSH:
   ```bash
   sudo raspi-config
   ```
Navigate to Interfacing Options and select SSH.
Choose Enable and exit the configuration tool.
Connecting to Raspberry Pi 5 using VSCode
Install the Remote - SSH extension in VSCode.
Open the command palette in VSCode (Ctrl+Shift+P or Cmd+Shift+P).
Click Remote-SSH: Open SSH Configuration File...
Add the following configuration to your SSH config file (~/.ssh/config):

   ```config
Host [host name]
    HostName [raspberry_pi_ip]
    User [pi_name]
    Port 22
   ```

If prompted, enter the password for the pi user.
You should now be connected to your Raspberry Pi through VSCode.

## sol_api_test Description

sol_api_test is a code for testing the operation of the solenoid. This helps to verify if the wiring is correct. It includes a section to test API communication. After ensuring the interpreter is correct, sol_api_test runs in the Raspberry Pi environment, and client runs in an external environment to communicate.

### Setup Instructions

1. Set up and activate the virtual environment:
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```
Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```
Run the API code:
   ```bash   
   python3 sol_api_test.py
   ```

Run client.py in the external environment:
   ```bash
   python3 client.py
   ```
After this, the solenoid will operate for 10 seconds.

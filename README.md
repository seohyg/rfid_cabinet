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

![스크린샷 2024-07-22 140056](https://github.com/user-attachments/assets/eaf1a9d2-d90c-4a1e-a8d4-9b33ac9564cf)

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


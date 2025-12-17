# Firmware Extraction Using Two Microcontrollers
 
This project demonstrates how to use python and arduino IDE and arduino ISP to use an arduino with the example ISP code to copy and analyze the firmware from a microcontroller device under testing. 
 
## Table of Contents
* [Requirements](#requirements)
* [Implementation](#implementation)
* [Error Handling](#error-handling)
* [References](#references)


## Requirements

This project requires numpy, pyserial, time, subprocess, and intelhex. It was developed using Python 3.12

Use 'pip install -r requirements.txt' to install the following dependencies:

```python
contourpy==1.3.3
cycler==0.12.1
fonttools==4.59.2
joblib==1.5.2
kiwisolver==1.4.9
matplotlib==3.10.6
numpy==2.3.3
packaging==25.0
pandas==2.3.2
pillow==11.3.0
pyparsing==3.2.3
python-dateutil==2.9.0.post0
pytz==2025.2
scikit-learn==1.7.2
scipy==1.16.1
seaborn==0.13.2
six==1.17.0
threadpoolctl==3.6.0
tzdata==2025.2


```
## Description

This project demonstrates how the nonvolatile memory of the Arduino microcontollers can be affected without using the standard serial port.  This in fact can directly affect the second serial bus of the device.  This script takes advantage of the ArduinoISP example script provided with the IDE.  The Arduino is able to process AVR with its avrdude function (language) and can directly write a script to the microcontroller.  This takes advantage of a different connection scheme as described in project one.  For this application, we make use of the SPI pins on the head of the board.  We can connect to MOSI, MISO, and CLk and are able to send commands to the device to execute.  Additionally the device is connected to a breadboard with indicator LEDs to describe current behavior
## Implementation

This program can be run through main.py

There are two classes that main.py calls: ClassOne and ClassTwo.  Both classes allow outside function calls to add, clear, and get array values. ClassOne takes no input at initialization. ClassTwo takes an array at initialization.


## References


This repo does not  have any references, but if using materials such as tutorials, websites, publications, etc. this is where they should be added in IEEE format.



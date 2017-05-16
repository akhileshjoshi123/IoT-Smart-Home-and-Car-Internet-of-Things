# IoT-Smart-Home-and-Car-Internet-of-Things
simple IoT application using MQTT on raspberry PI 3

Component Details

Breadboard
The breadboard is a way of connecting electronic components to each other without having to solder them together. They are often used to test a circuit design before creating a Printed Circuit Board (PCB).

LED
A Red LED stands for Light Emitting Diode, and glows when electricity is passed through it. The longer leg (known as the ‘anode’), is always connected to the positive supply of the circuit. The shorter leg (known as the ‘cathode’) is connected to the negative side of the power supply, known as ‘ground’. LEDs will only work if power is supplied the correct way around (i.e. if the ‘polarity’ is correct).

Resistors
We require 220 Ohm Resistor. We must always use resistors to connect LEDs up to the GPIO pins of the Raspberry Pi. The Raspberry Pi can only supply a small current (about 60mA). The LEDs will want to draw more, and if allowed to, they will burn out the Raspberry Pi. Therefore, putting the resistors in the circuit will ensure that only this small current will flow and the Pi will not be damaged. The value of a resistor is marked with colored bands along the length of the resistor body. The value of resistance can be determined the color bands on the resistor.

Connecting Wires
Connecting wires are used on breadboards to ‘jump’ from one connection to another.  The end with the ‘pin’ will go into the Breadboard. The end with the piece of plastic with a hole in it will go onto the Raspberry Pi’s GPIO pins.

General Purpose Input/output (GPIO)
–	Pins can be configured to be input/output
–	Reading from various environmental sensors
–	Ex: IR, video, temperature, 3‐axis orientation, acceleration
–	Writing output to dc motors, LEDs for status

Power Consumption 
–	microUSB power connector – 2.5W

AWS Iaas
Ec2 instance. This is used to send instructions to Raspberry Pi to switch on LED under specified conditions.
HDMI
–	Digital signal
–	Video and audio signal
–	DVI cannot carry audio signal
–	Up to 1920x1200 resolution

Other Software Components:
–	MQTT message broker: To communicate messages from EC2 to Raspberry PI and from Raspberry PI to EC2. 
–	geopy library to convert location to coordinates and decrement coordinates by one per second. These coordinates are sent to EC2 and EC2 send information to Raspberry PI to switch on LED light if location information received is equal to Home Longitude -1 .

/*****************************************************************************
* | File      	:   Readme_EN.txt
* | Author      :   Waveshare team
* | Function    :   Help with use
* | Info        :
*----------------
* |	This version:   V1.0
* | Date        :   2019-09-24
* | Info        :   Here is an English version of the documentation for your quick use.
******************************************************************************/
This file is to help you use this Demo.
A brief description of the use of this project is here:

1. Basic information:
This routine has been verified on the Raspberry Pi 3B+;
This routine has been verified using the 2-CH RS485 HAT module. 
You can view the corresponding test routines in the examples\ of the project.

2. Pin connection:
Pin connections can be viewed in \lib\waveshare_2_CH_RS485_HAT\TSL2591.py and will be repeated here:
2-CH_RS485_HAT      =>    RPI(BCM)
VCC                 ->    3.3V/5V
GND                 ->    GND
SCLK                ->    SCLK (11)
MISO                ->    MISO (9)
MOSI                ->    MOSI (10)
CS                  ->    8
IRQ                 ->    25
EN1                 ->    27
EN2                 ->    22

3.Installation library
    sudo apt-get update
    sudo apt-get install python-pip
    sudo apt-get install python-pil
    sudo pip install RPi.GPIO
    sudo pip install spidev

or
    sudo apt-get update
    sudo apt-get install python3-pip
    sudo apt-get install python3-pil
    sudo pip3 install RPi.GPIO
    sudo apt-get install python3-serial
    sudo pip3 install spidev

4. Basic use:
Test the program in the examples\ directory:
The routine main.py ends the receive string for channel 1 with '\n' and then sends the received string.
The routine test.py sends data to each other on channel 1 and channel 2.
python2
    sudo python main.py

python3
    sudo python3 main.py
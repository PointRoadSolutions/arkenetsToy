# Radar Toy for Demo
This is a toy device designed to repersent a radar node.

## Overview
The toy is comprised of a Raspi Zero W with a Pimoroni Scroll Phat HD on top. This phat gives the raspi a 17x7 array of white leds to light. The raspi should control the lights in a way to evoke the a radar pulse.

## Connecting
On local network, the raspi has a reserved IP address of ###.###.##.250

## rc.local
'/etc/rc.local' has been modifed to start 'pulse.py' on boot.
 
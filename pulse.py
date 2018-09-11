#!/usr/bin/env python

import time
import math

import scrollphathd

print("""
Scroll pHAT HD: Pulse
Displays a demo evocative of a radar pulse
Press Ctrl+C to exit
""")

def swirl(x, y, step):
    x -= (scrollphathd.DISPLAY_WIDTH/2.0)
    y -= (scrollphathd.DISPLAY_HEIGHT/2.0)

    dist = math.sqrt(pow(x, 2) + pow(y, 2))

    angle = (step / 10.0) + dist / 1.5

    s = math.sin(angle)
    c = math.cos(angle)

    xs = x * c - y * s
    ys = x * s + y * c

    r = abs(xs + ys)

    return max(0.0, 0.7 - min(1.0, r/8.0))

scrollphathd.set_brightness(0.8)

sphd.write_string('arkenets        ')

while True:
    sphd.show()
    sphd.scroll(1)
    time.sleep(0.05)
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# adapted and expanded upon by Mews-Byte aka Meow aka MacMeowMeowMeowMeowMeowMeow

# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel

pixie = 0
wanderingpixie = 30

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 60

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def rainbow_cycle(wait):
    pixels.fill((0,0,0))
    pixels.show()
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)
        pixels.fill((0,0,0))
        pixels.show()

def rainbow_cycleB(wait):
    pixels.fill((0,0,0))
    pixels.show()
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 156 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 215)
        pixels.show()
        time.sleep(wait)
        pixels.fill((0,0,0))
        pixels.show()

def blinkToRight():
    global pixie
    for x in range(0,60):
        pixels[pixie] = (0, 0, 0)
        pixels.show()
        time.sleep(0.1)
        pixie = pixie + 1
        resetpixie = pixie
        print(pixie)
        pixels[resetpixie] = (255, 0, 0)
        pixels.show()
        time.sleep(0.1)

def sweepRightSingleRed():

    for x in range(0,60): # sweep right, single pix


            pixels[x] = (255, 0, 0)
            pixels.show()
            time.sleep(0.01) # was 0.2
            pixels[x] = (0, 0, 0)
            pixels.show()

def sweepLeftSingleRed():

    for x in range(59,0,-1): # sweep left, single pix


            pixels[x] = (255, 0, 0)
            pixels.show()
            time.sleep(0.01)
            pixels[x] = (0, 0, 0)
            pixels.show()

def goLeftSingleRed():
    global wanderingpixie

    while True:
        

        pixels[wanderingpixie + 1] = (255, 0, 0)
        pixels.show()
        time.sleep(0.2)
        pixels[wanderingpixie + 1] = (0, 0, 0)
        pixels.show()
        wanderingpixie = wanderingpixie + 1

        if wanderingpixie == 59:
            wanderingpixie = 0
        return wanderingpixie

def goRightSingleRed():
    global wanderingpixie
    while True:

        pixels[wanderingpixie - 1] = (255, 0, 0)
        pixels.show()
        time.sleep(0.2)
        pixels[wanderingpixie - 1] = (0, 0, 0)
        pixels.show()
        wanderingpixie = wanderingpixie -1 
        if wanderingpixie == 0:
            wanderingpixie = 59
        return wanderingpixie



def loopLeftSingleRed():
    try:

        global wanderingpixie

            
        pixels.fill((0,0,0))
        pixels.show()
        pixels[wanderingpixie + 1] = (255, 0, 0)
        pixels.show()
        time.sleep(0.1)
        pixels.fill((0,0,0))
        #pixels[wanderingpixie + 1] = (0, 0, 0)
        pixels.show()
        wanderingpixie = wanderingpixie + 1

        if wanderingpixie == 59:
            wanderingpixie = 0
    except:
        IndexError
        
def loopRightSingleRed():
    global wanderingpixie
    try:

        pixels.fill((0,0,0))
        pixels.show()
        pixels[wanderingpixie - 1] = (255, 0, 0)
        pixels.show()
        time.sleep(0.1)
        pixels.fill((0,0,0))
        
        #pixels[wanderingpixie - 1] = (0, 0, 0)
        pixels.show()
        wanderingpixie = wanderingpixie -1 
        if wanderingpixie == 0:
            wanderingpixie = 59
    except:
        IndexError        
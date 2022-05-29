FPS = 30

import time
import board
from adafruit_matrixportal.matrixportal import MatrixPortal
from adafruit_portalbase.graphics import GraphicsBase

mp = MatrixPortal( status_neopixel=board.NEOPIXEL )
disp = mp.display
gb = GraphicsBase( disp )

frameIdx = 0
frames = [ 'frames/frame 000.bmp',
           'frames/frame 003.bmp',
           'frames/frame 006.bmp',
           'frames/frame 009.bmp',
           'frames/frame 012.bmp',
           'frames/frame 015.bmp',
           'frames/frame 018.bmp',
           'frames/frame 021.bmp',
           'frames/frame 024.bmp',
           'frames/frame 027.bmp',
           'frames/frame 030.bmp',
           'frames/frame 033.bmp',
           'frames/frame 036.bmp',
           'frames/frame 039.bmp',
           'frames/frame 042.bmp',
           'frames/frame 045.bmp',
           'frames/frame 048.bmp',
           'frames/frame 051.bmp',
           'frames/frame 054.bmp',
           'frames/frame 057.bmp',
           'frames/frame 060.bmp',
           'frames/frame 063.bmp',
           'frames/frame 066.bmp' ]

disp.brightness = 0.05

while True:
    gb.set_background( frames[ frameIdx ] )
    time.sleep(1/FPS)
    frameIdx = ( frameIdx + 1 ) % len( frames )

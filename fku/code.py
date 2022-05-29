from adafruit_matrixportal.matrixportal import MatrixPortal
import board
from displayio import Group, TileGrid, Bitmap, Palette
from time import sleep

from adafruit_display_text.label import Label
import terminalio

from definitions import *
from meteorShower import *

display = MatrixPortal( status_neopixel=board.NEOPIXEL ).display
disp_group = Group()

p = Palette( 3 )
p[ WHITE ] = 0xFFFFFF
p[ GRAY ] = 0x555555
p.make_transparent( TRANSPARENT )

surface = Bitmap( W, H, NUM_COLORS )
disp_group.append( TileGrid( surface, pixel_shader = p ) )

text = Label( terminalio.FONT,
              text = "fku",
              color = 0xFFFFFF,
              anchor_point = ( 0.5, 0.5 ),
              anchored_position = ( W >> 1, H >> 1 ) )
disp_group.append( text )

ms = MeteorShower()

display.show( disp_group )
while True:

    ms.update()

    surface.fill( TRANSPARENT )
    ms.draw( surface )
    surface.dirty()

    sleep( dt )
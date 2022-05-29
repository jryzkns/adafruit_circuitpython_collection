from definitions import *

from random import randint

class Star:
    def __init__( self, x, y=0, speed = 1 ):
        self.render_buffer, self.alive = {}, True
        self.x, self.y = x, y
        self.twinkle_period = 10
        self.fast = randint( 0, 1 ) == 1
        if self.fast:
            self.twinkle_period = 5
            speed *= 2
        self.xvel, self.yvel = -speed, speed
        self.twinkle_counter = randint( 0, self.twinkle_period )

    def update( self ):

        self.twinkle_counter = ( self.twinkle_counter + 1 ) % self.twinkle_period

        self.x += self.xvel
        self.y += self.yvel

        self.render_buffer, self.alive = {}, False

        self.render_buffer[ ( self.x, self.y ) ] = WHITE
        for disp in range( self.yvel * 2 ):
            xval, yval = self.x + disp, self.y - disp
            # still alive if it has at least 1 valid pixel to render
            self.alive = ( xval > 0 ) and ( yval < H )
            self.render_buffer[ ( xval, yval ) ] = GRAY

        if self.twinkle_counter == 0:
            self.render_buffer[ ( self.x, self.y + 1 ) ] = WHITE
            self.render_buffer[ ( self.x, self.y - 1 ) ] = WHITE
            self.render_buffer[ ( self.x - 1, self.y ) ] = WHITE
            self.render_buffer[ ( self.x + 1, self.y ) ] = WHITE
            if self.fast:
                self.render_buffer[ ( self.x, self.y + 2 ) ] = GRAY
                self.render_buffer[ ( self.x, self.y - 2 ) ] = GRAY
                self.render_buffer[ ( self.x - 2, self.y ) ] = GRAY
                self.render_buffer[ ( self.x + 2, self.y ) ] = GRAY

    def draw( self, surf ):
        for pos, color in self.render_buffer.items(): 
            if inBound( *pos ):
                surf[ pos ] = color

class MeteorShower( list ):
    def __init__( self, maxStars = 30 ):
        self.maxStars = maxStars
        self.nextStarTimer = self.getNextStarTimer()

    def getNextStarTimer( self ):
        return randint( 1, 4 )

    def makeNewStar( self ):
        self += Star( randint( W // 6, 3 * W // 2 - 1 ) ),

    def update( self ):
        self.nextStarTimer -= 1
        if self.nextStarTimer <= 0:
            if len( self ) < self.maxStars:
                self.makeNewStar()
            self.nextStarTimer = self.getNextStarTimer()
        for idx, star in enumerate( self ):
            star.update( )
            if not star.alive:
                self.pop( idx )

    def draw( self, surf ):
        for star in self:
            star.draw( surf )
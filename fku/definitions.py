W, H = 64, 32

NUM_COLORS = 3

TRANSPARENT = 0
WHITE = 1
GRAY = 2

FPS = 30
dt = 1 / FPS

inBound = lambda x, y : ( 0 <= x < W ) and ( 0 <= y < H )
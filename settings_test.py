WIDTH = 800
HEIGHT = 600
PLAYER_ACC = 2
PLAYER_FRICTION = -0.12
PLAYER_JUMP = 20
PLAYER_GRAV = 0.8
MOB_ACC = 2
MOB_FRICTION = -0.12
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
RED = (255, 50, 50)
GREEN = (50,255,50)
ORANGE = (255,165,0)
GRAY = (100,100,100)
FPS = 60 
RUNNING = True
SCORE = 0
PAUSED = False

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, ORANGE, "danger"),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20, GRAY, "normal"),
                 (125, HEIGHT - 350, 100, 5, GREEN, "disappearing "),
                 (350, 200, 100, 20, GREEN, "normal"),
                 (175, 100, 50, 20, GREEN, "normal")]
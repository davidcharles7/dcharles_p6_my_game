WIDTH = 800
HEIGHT = 600
PLAYER_ACC = 0.8
PLAYER_FRICTION = -0.12
PLAYER_JUMP = 15
PLAYER_GRAV = 0.8
MOB_ACC = 1
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
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 450, ORANGE, "danger"),
                 (0, HEIGHT * 3 / 4, 100, 20, GRAY, "normal"),
                 (150, 330 , 100, 20, GREEN, "bouncey"),
                 (700, HEIGHT * 3 / 4, 100, 20, GRAY, "normal"),
                 (500, HEIGHT * 3 / 4, 100, 20, GRAY, "normal"),
                 (350, 200, 100, 20, GRAY, "normal"),
                 (175, 100, 50, 20, GRAY, "normal"),
                ]
# Author: Samir Kabra
# This program runs a GUI that gives the user the option to launch various games made in python.

import numpy as np
import pygame
import pygame.locals
import random
import time
import tkinter as tk
from tkinter import messagebox
import turtle


def snake():
    """
    This function creates a snake game in python using the pygame library.
    """
    # From a tutorial at https://www.geeksforgeeks.org/snake-game-in-python-using-pygame-module/

    snake_speed = 15

    # Window size
    window_x = 720
    window_y = 480

    # defining colors
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)

    backgroundColor = black
    notBlack = white

    # Initialising pygame
    pygame.init()

    # Initialise game window
    pygame.display.set_caption('πthon the game')
    game_window = pygame.display.set_mode((window_x, window_y))

    # FPS (frames per second) controller
    fps = pygame.time.Clock()

    # defining snake default position
    snake_position = [100, 50]

    # defining first 4 blocks of snake body
    snake_body = [[100, 50],
                  [90, 50],
                  [80, 50],
                  [70, 50]
                  ]
    # fruit position
    fruit_position = [random.randrange(1, (window_x//10)) * 10,
                      random.randrange(1, (window_y//10)) * 10]

    fruit_spawn = True

    # setting default snake direction towards
    # right
    direction = 'RIGHT'
    change_to = direction

    # initial score
    score = 0

    # displaying Score function
    def show_score(choice, color, font, size):
        """
        This function displays the score accumulated by the user, it is updated as it increases.
        """
        # creating font object score_font
        score_font = pygame.font.SysFont(font, size)

        # create the display surface object
        # score_surface
        score_surface = score_font.render('Score : ' + str(score), True, color)

        # create a rectangular object for the text
        # surface object
        score_rect = score_surface.get_rect()

        # displaying text
        game_window.blit(score_surface, score_rect)

    # game over function
    def game_over():
        """
        This function displays the final score at the end of the game, and calls appropriate functions to show the 
        play again prompt.
        """
        # creating font object my_font
        my_font = pygame.font.SysFont('times new roman', 50)

        # creating a text surface on which text
        # will be drawn
        game_over_surface = my_font.render(
            'Your Score is : ' + str(score), True, red)

        # create a rectangular object for the text
        # surface object
        game_over_rect = game_over_surface.get_rect()

        # setting position of the text
        game_over_rect.midtop = (window_x/2, window_y/4)

        # blit will draw the text on screen
        game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()

        # Play again?
        playAgain("snake")

        # after 2 seconds we will quit the program
        time.sleep(2)

        # deactivating pygame library
        pygame.quit()

    # Main Function
    playing = True
    while playing:

        # handling key events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'
                if event.key == pygame.K_d:
                    if backgroundColor == black and notBlack == white:
                        backgroundColor = white
                        notBlack = black
                    else:
                        backgroundColor = black
                        notBlack = white

        # If two keys are pressed simultaneously
        # we don't want snake to move into two
        # directions simultaneously
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Moving the snake
        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10

        # Snake body growing mechanism
        # if fruits and snakes collide then scores
        # will be incremented by 10
        snake_body.insert(0, list(snake_position))
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 10
            fruit_spawn = False
        else:
            snake_body.pop()

        if not fruit_spawn:
            fruit_position = [random.randrange(1, (window_x//10)) * 10,
                              random.randrange(1, (window_y//10)) * 10]

        fruit_spawn = True
        game_window.fill(backgroundColor)

        for pos in snake_body:
            pygame.draw.rect(game_window, green,
                             pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(game_window, notBlack, pygame.Rect(
            fruit_position[0], fruit_position[1], 10, 10))

        # Game Over conditions
        if snake_position[0] < 0 or snake_position[0] > window_x-10:
            game_over()
        if snake_position[1] < 0 or snake_position[1] > window_y-10:
            game_over()

        # Touching the snake body
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over()

        # displaying score countinuously
        show_score(1, notBlack, 'times new roman', 20)

        # Refresh game screen
        pygame.display.update()

        # Frame Per Second /Refresh Rate
        fps.tick(snake_speed)


def spaceInvaders():
    """
    This function launches the space invaders game. 
    """
    # Author: russs123, Modified by: Samir Kabra
    # Source: https://github.com/russs123/space_invaders/blob/main/main.py

    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.mixer.init()
    pygame.init()

    # define fps
    clock = pygame.time.Clock()
    fps = 60

    screen_width = 600
    screen_height = 800

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Space Invanders')

    # define fonts
    font30 = pygame.font.SysFont('Constantia', 30)
    font40 = pygame.font.SysFont('Constantia', 40)

    # load sounds
    explosion_fx = pygame.mixer.Sound("img/explosion.wav")
    explosion_fx.set_volume(0.25)

    explosion2_fx = pygame.mixer.Sound("img/explosion2.wav")
    explosion2_fx.set_volume(0.25)

    laser_fx = pygame.mixer.Sound("img/laser.wav")
    laser_fx.set_volume(0.25)

    # define game variables
    rows = 5
    cols = 5
    alien_cooldown = 1000  # bullet cooldown in milliseconds
    last_alien_shot = pygame.time.get_ticks()
    countdown = 3
    last_count = pygame.time.get_ticks()
    game_over = 0  # 0 is no game over, 1 means player has won, -1 means player has lost

    # define colours
    red = (255, 0, 0)
    green = (0, 255, 0)
    white = (255, 255, 255)

    # load image
    bg = pygame.image.load("img/bg.png")

    def draw_bg():
        screen.blit(bg, (0, 0))

    # define function for creating text

    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    # create spaceship class

    class Spaceship(pygame.sprite.Sprite):
        """
        The Spaceship class is a template for a spaceship object.
        """

        def __init__(self, x, y, health):
            """
            The constructor initializes the position, health and image for a Spaceship object.
            """
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("img/spaceship.png")
            self.rect = self.image.get_rect()
            self.rect.center = [x, y]
            self.health_start = health
            self.health_remaining = health
            self.last_shot = pygame.time.get_ticks()

        def update(self):
            """
            The update function updates the position of Spaceship objects based on key press, 
            the location of bullets and draws a health bar and updates it as well.
            """
            # set movement speed
            speed = 8
            # set a cooldown variable
            cooldown = 500  # milliseconds
            game_over = 0

            # get key press
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT] and self.rect.left > 0:
                self.rect.x -= speed
            if key[pygame.K_RIGHT] and self.rect.right < screen_width:
                self.rect.x += speed

            # record current time
            time_now = pygame.time.get_ticks()
            # shoot
            if key[pygame.K_SPACE] and time_now - self.last_shot > cooldown:
                laser_fx.play()
                bullet = Bullets(self.rect.centerx, self.rect.top)
                bullet_group.add(bullet)
                self.last_shot = time_now

            # update mask
            self.mask = pygame.mask.from_surface(self.image)

            # draw health bar
            pygame.draw.rect(
                screen, red, (self.rect.x, (self.rect.bottom + 10), self.rect.width, 15))
            if self.health_remaining > 0:
                pygame.draw.rect(screen, green, (self.rect.x, (self.rect.bottom + 10), int(
                    self.rect.width * (self.health_remaining / self.health_start)), 15))
            elif self.health_remaining <= 0:
                explosion = Explosion(self.rect.centerx, self.rect.centery, 3)
                explosion_group.add(explosion)
                self.kill()
                game_over = -1
            return game_over

    # create Bullets class

    class Bullets(pygame.sprite.Sprite):
        """
        The Bullets class is a template for Bullets objects.
        """

        def __init__(self, x, y):
            """
            The constructor sets initial values for image and position of bullets objects.
            """
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("img/bullet.png")
            self.rect = self.image.get_rect()
            self.rect.center = [x, y]

        def update(self):
            """
            The update function updates the position of the bullets objects and plays appropriate sounds.
            """
            self.rect.y -= 5
            if self.rect.bottom < 0:
                self.kill()
            if pygame.sprite.spritecollide(self, alien_group, True):
                self.kill()
                explosion_fx.play()
                explosion = Explosion(self.rect.centerx, self.rect.centery, 2)
                explosion_group.add(explosion)

    # create Aliens class

    class Aliens(pygame.sprite.Sprite):
        """
        The Aliens class is a template for aliens objects.
        """

        def __init__(self, x, y):
            """
            The constructor sets initial values for the image of aliens objects and their position.
            """
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load(
                "img/alien" + str(random.randint(1, 5)) + ".png")
            self.rect = self.image.get_rect()
            self.rect.center = [x, y]
            self.move_counter = 0
            self.move_direction = 1

        def update(self):
            """
            The update function updates the position of aliens objects. 
            """
            self.rect.x += self.move_direction
            self.move_counter += 1
            if abs(self.move_counter) > 75:
                self.move_direction *= -1
                self.move_counter *= self.move_direction

    # create Alien Bullets class

    class Alien_Bullets(pygame.sprite.Sprite):
        """
        The Alien_Bullets class is a template for Alien_Bullets objects.
        """

        def __init__(self, x, y):
            """
            The constructor initializes the image and position of alien bullets objects.
            """
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("img/alien_bullet.png")
            self.rect = self.image.get_rect()
            self.rect.center = [x, y]

        def update(self):
            """
            The update function updates the position of Alien Bullets objects and 
            sets actions if the bullet hits another object.
            """
            self.rect.y += 2
            if self.rect.top > screen_height:
                self.kill()
            if pygame.sprite.spritecollide(self, spaceship_group, False, pygame.sprite.collide_mask):
                self.kill()
                explosion2_fx.play()
                # reduce spaceship health
                spaceship.health_remaining -= 1
                explosion = Explosion(self.rect.centerx, self.rect.centery, 1)
                explosion_group.add(explosion)

    # create Explosion class

    class Explosion(pygame.sprite.Sprite):
        """
        The Explosion class is a template for Explosion objects.
        """

        def __init__(self, x, y, size):
            """
            The constructor sets the initial values for animation (image) of the explosion objects.
            """
            pygame.sprite.Sprite.__init__(self)
            self.images = []
            for num in range(1, 6):
                img = pygame.image.load(f"img/exp{num}.png")
                if size == 1:
                    img = pygame.transform.scale(img, (20, 20))
                if size == 2:
                    img = pygame.transform.scale(img, (40, 40))
                if size == 3:
                    img = pygame.transform.scale(img, (160, 160))
                # add the image to the list
                self.images.append(img)
            self.index = 0
            self.image = self.images[self.index]
            self.rect = self.image.get_rect()
            self.rect.center = [x, y]
            self.counter = 0

        def update(self):
            """
            The update function updates the position of explosion objects 
            based on duration of animation.
            """
            explosion_speed = 3
            # update explosion animation
            self.counter += 1

            if self.counter >= explosion_speed and self.index < len(self.images) - 1:
                self.counter = 0
                self.index += 1
                self.image = self.images[self.index]

            # if the animation is complete, delete explosion
            if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
                self.kill()

    # create sprite groups
    spaceship_group = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()
    alien_group = pygame.sprite.Group()
    alien_bullet_group = pygame.sprite.Group()
    explosion_group = pygame.sprite.Group()

    def create_aliens():
        """
        The create aliens function generates a grid of aliens.
        """
        # generate aliens
        for row in range(rows):
            for item in range(cols):
                alien = Aliens(100 + item * 100, 100 + row * 70)
                alien_group.add(alien)

    create_aliens()

    # create player
    spaceship = Spaceship(int(screen_width / 2), screen_height - 100, 3)
    spaceship_group.add(spaceship)

    run = True
    while run:

        clock.tick(fps)

        # draw background
        draw_bg()

        if countdown == 0:
            # create random alien bullets
            # record current time
            time_now = pygame.time.get_ticks()
            # shoot
            if time_now - last_alien_shot > alien_cooldown and len(alien_bullet_group) < 5 and len(alien_group) > 0:
                attacking_alien = random.choice(alien_group.sprites())
                alien_bullet = Alien_Bullets(
                    attacking_alien.rect.centerx, attacking_alien.rect.bottom)
                alien_bullet_group.add(alien_bullet)
                last_alien_shot = time_now

            # check if all the aliens have been killed
            if len(alien_group) == 0:
                game_over = 1

            if game_over == 0:
                # update spaceship
                game_over = spaceship.update()

                # update sprite groups
                bullet_group.update()
                alien_group.update()
                alien_bullet_group.update()
            else:
                if game_over == -1:
                    draw_text('GAME OVER!', font40, white, int(
                        screen_width / 2 - 100), int(screen_height / 2 + 50))
                    pygame.display.update()
                    time.sleep(3)
                    playAgain("spaceInvaders")
                    pygame.quit()
                if game_over == 1:
                    global userName
                    textToDraw = "YOU WIN, " + userName + "!"
                    draw_text(textToDraw, font40, white, int(
                        screen_width / 2 - 100), int(screen_height / 2 + 50))
                    pygame.display.update()
                    time.sleep(3)
                    playAgain("spaceInvaders")
                    pygame.quit()

        if countdown > 0:
            draw_text('GET READY!', font40, white, int(
                screen_width / 2 - 110), int(screen_height / 2 + 50))
            draw_text(str(countdown), font40, white, int(
                screen_width / 2 - 10), int(screen_height / 2 + 100))
            count_timer = pygame.time.get_ticks()
            if count_timer - last_count > 1000:
                countdown -= 1
                last_count = count_timer

        # update explosion group
        explosion_group.update()

        # draw sprite groups
        spaceship_group.draw(screen)
        bullet_group.draw(screen)
        alien_group.draw(screen)
        alien_bullet_group.draw(screen)
        explosion_group.draw(screen)

        # event handlers
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()


def pong():
    """
    The pong function launches an instance of a pong game.
    """
    # From a tutorial at https://www.geeksforgeeks.org/create-pong-game-using-python-turtle/

    # Create screen
    sc = turtle.Screen()
    sc.title("Pong game")
    sc.bgcolor("white")
    sc.setup(width=1000, height=600)

    # Left paddle
    left_pad = turtle.Turtle()
    left_pad.speed(0)
    left_pad.shape("square")
    left_pad.color("red")
    left_pad.shapesize(stretch_wid=6, stretch_len=2)
    left_pad.penup()
    left_pad.goto(-400, 0)

    # Right paddle
    right_pad = turtle.Turtle()
    right_pad.speed(0)
    right_pad.shape("square")
    right_pad.color("green")
    right_pad.shapesize(stretch_wid=6, stretch_len=2)
    right_pad.penup()
    right_pad.goto(400, 0)

    # Ball of circle shape
    hit_ball = turtle.Turtle()
    hit_ball.speed(40)
    hit_ball.shape("circle")
    hit_ball.color("blue")
    hit_ball.penup()
    hit_ball.goto(0, 0)
    hit_ball.dx = 5
    hit_ball.dy = -5

    # Initialize the score
    Red = 0
    Green = 0

    # Displays the score
    sketch = turtle.Turtle()
    sketch.speed(0)
    sketch.color("blue")
    sketch.penup()
    sketch.hideturtle()
    sketch.goto(0, 260)
    sketch.write("Red : 0    Green: 0",
                 align="center", font=("Courier", 24, "normal"))

    def darkMode():
        """
        The darkmode function toggles dark/light mode on keypress.
        """
        if sc.bgcolor() == "white":
            sc.bgcolor("black")
            hit_ball.color("white")
        else:
            sc.bgcolor("white")
            hit_ball.color("black")

    # Functions to move paddle vertically

    def paddleaup():
        """
        The paddleaup function moves the paddle A up.
        """
        y = left_pad.ycor()
        y += 20
        left_pad.sety(y)

    def paddleadown():
        """
        The paddleadown function moves the paddle A down.
        """
        y = left_pad.ycor()
        y -= 20
        left_pad.sety(y)

    def paddlebup():
        """
        The paddlebup function moves the paddle B up.
        """
        y = right_pad.ycor()
        y += 20
        right_pad.sety(y)

    def paddlebdown():
        """
        The paddlebdown function moves the paddle B down.
        """
        y = right_pad.ycor()
        y -= 20
        right_pad.sety(y)

    # Keyboard bindings
    sc.listen()
    sc.onkeypress(paddleaup, "w")
    sc.onkeypress(paddleadown, "s")
    sc.onkeypress(paddlebup, "Up")
    sc.onkeypress(paddlebdown, "Down")
    sc.onkeypress(darkMode, "d")

    playing = True
    while playing:
        sc.update()

        hit_ball.setx(hit_ball.xcor()+hit_ball.dx)
        hit_ball.sety(hit_ball.ycor()+hit_ball.dy)

        # Checking borders
        if hit_ball.ycor() > 280:
            hit_ball.sety(280)
            hit_ball.dy *= -1

        if hit_ball.ycor() < -280:
            hit_ball.sety(-280)
            hit_ball.dy *= -1

        if hit_ball.xcor() > 500:
            hit_ball.goto(0, 0)
            hit_ball.dy *= -1
            Red += 1
            sketch.clear()
            sketch.write("Red : {}    Green: {}".format(
                Red, Green), align="center",
                font=("Courier", 24, "normal"))

        if hit_ball.xcor() < -500:
            hit_ball.goto(0, 0)
            hit_ball.dy *= -1
            Green += 1
            sketch.clear()
            sketch.write("Red : {}    Green: {}".format(
                Red, Green), align="center",
                font=("Courier", 24, "normal"))

        # Paddle ball collision
        if (hit_ball.xcor() > 360 and
            hit_ball.xcor() < 370) and (hit_ball.ycor() < right_pad.ycor()+40 and
                                        hit_ball.ycor() > right_pad.ycor()-40):
            hit_ball.setx(360)
            hit_ball.dx *= -1

        if (hit_ball.xcor() < -360 and
            hit_ball.xcor() > -370) and (hit_ball.ycor() < left_pad.ycor()+40 and
                                         hit_ball.ycor() > left_pad.ycor()-40):
            hit_ball.setx(-360)
            hit_ball.dx *= -1

        # Win/Loss
        if abs(Green - Red) >= 5:
            hit_ball.goto(0, 0)
            # sketch.clear()
            sketch.goto(10, 260)
            if Green > Red:
                sketch.write("Green wins by {}".format(Green-Red),
                             align="center", font=("Rockwell", 30, "bold"))
                time.sleep(3)
                playing = False
            else:
                sketch.write("Red wins by {}".format(Red-Green),
                             align="center", font=("Rockwell", 30, "bold"))
                time.sleep(3)
                playing = False

    if playing == False:
        sketch.clear()
        right_pad.clear()
        left_pad.clear()
        hit_ball.clear()
        playAgain("pong")
        sc.bye()


def ticTacToe():
    """
    The ticTacToe function launches an instance of the ticTacToe game.
    """
    # From a tutorial at https://pythonguides.com/create-a-game-using-python-pygame/

    pygame.init()

    WIDTH = 600
    HEIGHT = 600
    LINE_WIDTH = 15
    WIN_LINE_WIDTH = 15
    BOARD_ROWS = 3
    BOARD_COLS = 3
    SQUARE_SIZE = 200
    CIRCLE_RADIUS = 60
    CIRCLE_WIDTH = 15
    CROSS_WIDTH = 25
    SPACE = 55

    RED = (255, 0, 0)
    BG_COLOR = "black"  # (20, 200, 160)
    LINE_COLOR = "white"  # (23, 145, 135)
    CIRCLE_COLOR = "#d42d2d"  # (239, 231, 200)
    CROSS_COLOR = "#2dd4d4"  # (66, 66, 66)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('TIC TAC TOE')
    screen.fill(BG_COLOR)

    board = np.zeros((BOARD_ROWS, BOARD_COLS))

    def draw_lines():
        """
        The draw_lines function draws the grid lines for the game.
        """
        pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE),
                         (WIDTH, SQUARE_SIZE), LINE_WIDTH)

        pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE),
                         (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)

        pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0),
                         (SQUARE_SIZE, HEIGHT), LINE_WIDTH)

        pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0),
                         (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

    def draw_figures():
        """
        The draw_figures function draws the figures for the game.
        """
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] == 1:
                    pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE//2), int(
                        row * SQUARE_SIZE + SQUARE_SIZE//2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
                elif board[row][col] == 2:
                    pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE -
                                     SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                    pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                     (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)

    def mark_square(row, col, player):
        """
        The mark_square function marks the square the player is in.
        """
        board[row][col] = player

    def available_square(row, col):
        """
        The available_square function checks the number of squares that are available.
        """
        return board[row][col] == 0

    def is_board_full():
        """
        The is_board_full function checks if the board is full.
        """
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] == 0:
                    return False

        return True

    def check_win(player):
        """
        The check_win function checks if a player has won the game.
        """
        for col in range(BOARD_COLS):
            if board[0][col] == player and board[1][col] == player and board[2][col] == player:
                draw_vertical_winning_line(col, player)
                return True

        for row in range(BOARD_ROWS):
            if board[row][0] == player and board[row][1] == player and board[row][2] == player:
                draw_horizontal_winning_line(row, player)
                return True

        if board[2][0] == player and board[1][1] == player and board[0][2] == player:
            draw_asc_diagonal(player)
            return True

        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            draw_desc_diagonal(player)
            return True

        return False

    def draw_vertical_winning_line(col, player):
        """
        The draw_vertical_winning_line function draws a line on the winning pattern.
        """
        posX = col * SQUARE_SIZE + SQUARE_SIZE//2

        if player == 1:
            color = CIRCLE_COLOR
        elif player == 2:
            color = CROSS_COLOR

        pygame.draw.line(screen, color, (posX, 15),
                         (posX, HEIGHT - 15), LINE_WIDTH)

    def draw_horizontal_winning_line(row, player):
        """
        The draw_horizontal_winning_line function draws a line on the winning pattern.
        """
        posY = row * SQUARE_SIZE + SQUARE_SIZE//2

        if player == 1:
            color = CIRCLE_COLOR
        elif player == 2:
            color = CROSS_COLOR

        pygame.draw.line(screen, color, (15, posY),
                         (WIDTH - 15, posY), WIN_LINE_WIDTH)

    def draw_asc_diagonal(player):
        """
        The draw_asc_diagonal function draws a line on the winning pattern.
        """
        if player == 1:
            color = CIRCLE_COLOR
        elif player == 2:
            color = CROSS_COLOR

        pygame.draw.line(screen, color, (15, HEIGHT - 15),
                         (WIDTH - 15, 15), WIN_LINE_WIDTH)

    def draw_desc_diagonal(player):
        """
        The draw_desc_diagonal function draws a line on the winning pattern.
        """
        if player == 1:
            color = CIRCLE_COLOR
        elif player == 2:
            color = CROSS_COLOR

        pygame.draw.line(screen, color, (15, 15),
                         (WIDTH - 15, HEIGHT - 15), WIN_LINE_WIDTH)

    def restart():
        """
        The restart function restarts the game by resetting the grid.
        """
        screen.fill(BG_COLOR)
        draw_lines()
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                board[row][col] = 0

    draw_lines()

    player = 1
    game_over = False

    playing = True
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

                mouseX = event.pos[0]
                mouseY = event.pos[1]

                clicked_row = int(mouseY // SQUARE_SIZE)
                clicked_col = int(mouseX // SQUARE_SIZE)

                if available_square(clicked_row, clicked_col):

                    mark_square(clicked_row, clicked_col, player)
                    if check_win(player):
                        game_over = True
                    player = player % 2 + 1

                    draw_figures()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart()
                    player = 1
                    game_over = False

                if event.key == pygame.K_d:
                    if BG_COLOR == "black":
                        BG_COLOR = "white"
                        LINE_COLOR = "black"
                    else:
                        BG_COLOR = "black"
                        LINE_COLOR = "white"

        pygame.display.update()
        if game_over == True:
            time.sleep(1)
            global root
            if player == 1:
                player = "X"
            else:
                player = "O"
            win = "Player " + str(player) + " has won!"
            messagebox.showinfo(title="Winner", message=win)
            playAgain("tictactoe")
            pygame.quit()


def playAgain(game=""):
    """
    The playAgain function shows the user a prompt if they want to play the game again or not.
    """
    global root

    def runGame(game):
        if game == "snake":
            snake()
        elif game == "pong":
            pong()
        elif game == "spaceInvaders":
            spaceInvaders()
        else:
            ticTacToe()

    global userName
    messageToDisplay = "Do you want to play again, " + userName + "?"
    if messagebox.askyesno(title="Play Again?", message=messageToDisplay):
        runGame(game)


def main():
    """
    This is the main function, it implements GUI using Tkinter and launches games as requested by the user.
    """
    # Creating the background of the Base GUI
    global root
    root = tk.Tk()

    # Setting the title of the GUI window
    root.title("Arcade Games")

    # Images
    # Background image from unsplash.com
    bg = tk.PhotoImage(file="img/background.png")
    snakePic = tk.PhotoImage(file="img/snake.png")
    pongPic = tk.PhotoImage(file="img/pong.png")
    spaceInvadersPic = tk.PhotoImage(file="img/spaceInvaders.png")
    ticTacToePic = tk.PhotoImage(file="img/tictactoe.png")

    # Setting size of the canvas
    canvas = tk.Canvas(root, height="800", width="1385")  # Height

    # Fix size of window
    root.minsize(1385, 800)
    root.maxsize(1385, 800)

    canvas.pack(fill='both', expand=True)

    def askName():
        """
        This function asks the user for their name and returns a message to be displayed 
        based on whether the name entered was valid.
        """
        invalid = True
        while invalid:
            nameDialog = tk.simpledialog.askstring(
                "Input", "What is your name? (10 Characters max)")
            global userName
            userName = str(nameDialog)
            if len(userName) > 10 or len(userName.strip(" ")) == 0:
                tk.messagebox.showerror(
                    "Invalid Name", "The name you entered was invalid.")
                if tk.messagebox.askyesno(message="Retry?"):
                    continue
                else:
                    stringToDisplay = "Play a game!"
                    return stringToDisplay
            else:
                stringToDisplay = "Hello " + userName + ", " + "Play a game!"
                return stringToDisplay

    # Functions to show instructions for the games
    def snakeInstructions():
        """
        The snakeInstructions function shows the instructions for the snake game in a prompt and asks the user if they want to play.
        """
        snakeGameInstructions = "Instructions\n" + "1. Use Arrow keys to move the snake" + "\n" + "2. The snake should not cross or touch the edges of the window." + \
            "\n" + "\n\n\n\n\n" + "Would you like to play?"
        if tk.messagebox.askyesno(title="Snake game", message=snakeGameInstructions):
            snake()

    def spaceInstructions():
        """
        The spaceInvadersInstructions function shows the instructions for the spaceInvaders game in a prompt and asks the user if they want to play.
        """
        spaceInvadersInstructions = "Instructions\n" + "1. Use left and right arrow keys to move the space-ship.\n" + \
            "2. Press spacebar to fire on the invaders.\n" + \
            "3. Dodge invader attacks and keep an eye on your health bar.\n" + \
            "\n\n\n\n\n" + "Would you like to play?"
        if tk.messagebox.askyesno(title="Space Invaders Game", message=spaceInvadersInstructions):
            spaceInvaders()

    def pongInstructions():
        """
        The pongInstructions function shows the instructions for the pong game in a prompt and asks the user if they want to play.
        """

        pongGameInstructions = "Instructions\n" + "1. Use W an S keys to move the red paddle.\n" + "2. Use Up and Down arrow keys to move the green paddle.\n" + \
            "3. Each side must try to stop the ball from crossing in.\n" + \
            "4. Ball cannot be hit if paddle is in motion.\n" + "5. Press d key to toggle dark mode.\n" + \
            "6. Whoever has a lead of 5 points on the other side wins." + \
            "\n\n\n\n\n" + "Would you like to play?"
        if tk.messagebox.askyesno(title="Pong Game", message=pongGameInstructions):
            pong()

    def ticTacToeInstructions():
        """
        The ticTacToeInstructions function shows the instructions for the ticTacToe game in a prompt and asks the user if they want to play.
        """
        ticTacToeGameInstructions = "Instructions\n" + "1. Click on empty places in the grid in turns to place Xs and Os\n" + \
            "2. Whoever forms a 3 x 3 grid (Xs or Os) wins.\n" + \
            "3. Press r + d to alternate between light and dark modes" + \
            "\n\n\n\n\n" + "Would you like to play?"
        if tk.messagebox.askyesno(title="Tic Tac Toe Game", message=ticTacToeGameInstructions):
            ticTacToe()

    # Display image
    canvas.create_image(0, 0, image=bg, anchor="nw")

    # Add welcome greeting
    canvas.create_text(692.5, 50, text=askName(),
                       font="Rockwell 45", width=1250, fill="#FFF5EE")

    # Create Buttons for games
    snake_button = tk.Button(canvas, command=snakeInstructions, bd="5", relief="ridge",
                             activebackground="#C3313c", activeforeground="#2596be", image=snakePic)

    spaceinvaders_button = tk.Button(canvas, command=spaceInstructions, bd="5", relief="ridge",
                                     activebackground="#C3313c", activeforeground="#2596be", image=spaceInvadersPic)

    pong_button = tk.Button(canvas, command=pongInstructions, bd="5", relief="ridge",
                            activebackground="#C3313c", activeforeground="#2596be", image=pongPic)

    ticTacToe_button = tk.Button(canvas, command=ticTacToeInstructions, bd="5", relief="ridge",
                                 activebackground="#C3313c", activeforeground="#2596be", image=ticTacToePic)

    exit_button = tk.Button(canvas, command=root.destroy, bd="5", relief="ridge",
                            activebackground="#C3313c", activeforeground="#2596be", text="Exit")

    # Display Buttons
    # First row
    snake_canvas = canvas.create_window(100, 110,
                                        anchor="nw",
                                        window=snake_button, height=300, width=550)

    spaceInvaders_canvas = canvas.create_window(725, 110,
                                                anchor="nw",
                                                window=spaceinvaders_button, height=300, width=550)

    # Exit button
    exitButton_canvas = canvas.create_window(
        650, 410, anchor="nw", window=exit_button, height=65, width=75)

    # Second row
    pong_canvas = canvas.create_window(100, 475,
                                       anchor="nw",
                                       window=pong_button, height=300, width=550)

    ticTacToe_canvas = canvas.create_window(725, 475,
                                            anchor="nw",
                                            window=ticTacToe_button, height=300, width=550)

    # Execute tkinter
    root.mainloop()


if __name__ == "__main__":
    main()

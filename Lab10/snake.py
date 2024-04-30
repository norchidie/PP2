import pygame
import random
import psycopg2

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Snake and food
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randrange(1, (SCREEN_WIDTH//GRID_SIZE)) * GRID_SIZE,
            random.randrange(1, (SCREEN_HEIGHT//GRID_SIZE)) * GRID_SIZE]
food_spawn = True

# Direction
direction = 'RIGHT'
change_to = direction

# Score
score = 0

# Database connection
conn = psycopg2.connect("dbname=your_db_name user=your_db_user password=your_db_password")

def create_user(username):
    cur = conn.cursor()
    cur.execute("INSERT INTO users (username) VALUES (%s)", (username,))
    conn.commit()
    cur.close()

def get_user_level(username):
    cur = conn.cursor()
    cur.execute("SELECT level_completed FROM user_scores JOIN users ON user_scores.user_id = users.user_id WHERE username = %s ORDER BY date_played DESC LIMIT 1", (username,))
    level_completed = cur.fetchone()
    cur.close()
    if level_completed:
        return level_completed[0]
    else:
        return 1  # Default to level 1 if user has no scores

def save_game_state(username, score, level_completed):
    cur = conn.cursor()
    cur.execute("SELECT user_id FROM users WHERE username = %s", (username,))
    user_id = cur.fetchone()[0]  # Assuming username is unique
    cur.execute("INSERT INTO user_scores (user_id, score, level_completed) VALUES (%s, %s, %s)", (user_id, score, level_completed))
    conn.commit()
    cur.close()

# Function to show score on the screen
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score: ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (SCREEN_WIDTH/10, 15)
    else:
        score_rect.midtop = (SCREEN_WIDTH/2, SCREEN_HEIGHT/1.25)
    screen.blit(score_surface, score_rect)

# Game over function
def game_over():
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, RED)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (SCREEN_WIDTH/2, SCREEN_HEIGHT/4)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    pygame.time.wait(5000)
    pygame.quit()
    quit()

# Main Function
def main():
    global direction, change_to, score, food_spawn
    username = input("Enter your username: ")
    # Check if user exists, if not, create new user
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username = %s", (username,))
    if not cur.fetchone():
        create_user(username)
    level = get_user_level(username)
    print("Current level:", level)

    # Game variables
    game_over_var = False
    run = True

    # Main logic of the game
    while run:
        while game_over_var:
            screen.fill(BLACK)
            game_over()
            save_game_state(username, score, level)
            run = False

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    # Pause functionality
                    paused = True
                    while paused:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_p:
                                    paused = False
                                    break

                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'
                elif event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'
                elif event.key == pygame.K_ESCAPE:
                    # Quit the game
                    run = False

        # Making sure the snake cannot move in the opposite direction instantaneously
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'

        # Moving the snake
        if direction == 'LEFT':
            snake_pos[0] -= GRID_SIZE
        if direction == 'RIGHT':
            snake_pos[0] += GRID_SIZE
        if direction == 'UP':
            snake_pos[1] -= GRID_SIZE
        if direction == 'DOWN':
            snake_pos[1] += GRID_SIZE

        # Snake body growing mechanism
        # If the snake eats the food
        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
            score += 10
            food_spawn = False
        else:
            snake_body.pop()

        # Spawning food on the screen
        if not food_spawn:
            food_pos = [random.randrange(1, (SCREEN_WIDTH//GRID_SIZE)) * GRID_SIZE,
                        random.randrange(1, (SCREEN_HEIGHT//GRID_SIZE)) * GRID_SIZE]
        food_spawn = True

        # GFX
        screen.fill(BLACK)
        for pos in snake_body:
            # Snake body
            # .draw.rect(play_surface, color, xy-coordinate)
            # xy-coordinate -> .Rect(x, y, size_x, size_y)
            pygame.draw.rect(screen, BLUE, pygame.Rect(pos[0], pos[1], GRID_SIZE, GRID_SIZE))

        # Snake food
        pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], GRID_SIZE, GRID_SIZE))

        # Game Over conditions
        # Getting out of bounds
        if snake_pos[0] < 0 or snake_pos[0] > SCREEN_WIDTH - GRID_SIZE:
            game_over_var = True
        if snake_pos[1] < 0 or snake_pos[1] > SCREEN_HEIGHT - GRID_SIZE:
            game_over_var = True
        # Touching the snake body
        for block in snake_body[1:]:
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                game_over_var = True

        show_score(1, WHITE, 'times', 20)
        pygame.display.update()
        pygame.display.flip()
        pygame.time.Clock().tick(15)  # 15 FPS

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()

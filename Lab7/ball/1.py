import pygame as pg

pg.init()

icon = pg.image.load("ball.png")
pg.display.set_icon(icon)
WIDTH, HEIGHT = 500, 500
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Red Bouncing Ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

radius = 25
x = WIDTH // 2
y = HEIGHT // 2

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                if y - 20 >= radius:
                    y -= 20
            elif event.key == pg.K_DOWN:
                if y + 20 <= HEIGHT - radius:
                    y += 20
            elif event.key == pg.K_LEFT:
                if x - 20 >= radius:
                    x -= 20
            elif event.key == pg.K_RIGHT:
                if x + 20 <= WIDTH - radius:
                    x += 20

    screen.fill(WHITE)
    pg.draw.circle(screen, RED, (x, y), radius)
    pg.display.flip()
    pg.time.Clock().tick(60)

pg.quit()

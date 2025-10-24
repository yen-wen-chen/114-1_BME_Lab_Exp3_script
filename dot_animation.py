import pygame
import sys
import time
import random

DURATION = 20  # 秒數
WIDTH, HEIGHT = 600, 400

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dot Animation")
clock = pygame.time.Clock()
dot_color = (255, 0, 0)
dot_radius = 10
dot_pos = [
    random.randint(dot_radius, WIDTH - dot_radius),
    random.randint(dot_radius, HEIGHT - dot_radius),
]
pattern = random.choice([(2, 3), (3, 2)])  # 兩種上限模式
speed = [
    random.randint(1, pattern[0]) * random.choice([-1, 1]),
    random.randint(1, pattern[1]) * random.choice([-1, 1]),
]

start_time = time.time()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 若超過 DURATION 秒自動關閉
    if time.time() - start_time > DURATION:
        pygame.quit()
        sys.exit()

    # 移動與反彈
    dot_pos[0] += speed[0]
    dot_pos[1] += speed[1]
    if dot_pos[0] < dot_radius or dot_pos[0] > WIDTH - dot_radius:
        speed[0] = -speed[0]
    if dot_pos[1] < dot_radius or dot_pos[1] > HEIGHT - dot_radius:
        speed[1] = -speed[1]

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, dot_color, dot_pos, dot_radius)
    pygame.display.flip()
    clock.tick(60)

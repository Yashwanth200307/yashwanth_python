import pygame
import random

# Initialize
pygame.init()
WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Block")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
SKY = (135, 206, 235)
GREEN = (0, 200, 0)
RED = (255, 0, 0)

# Bird
bird = pygame.Rect(100, HEIGHT // 2, 30, 30)
bird_speed = 0
gravity = 0.5
flap_strength = -10

# Pipes
pipe_width = 70
pipe_gap = 200
pipes = []
pipe_timer = 0
score = 0
font = pygame.font.SysFont("Arial", 36)

def add_pipe():
    gap_y = random.randint(150, HEIGHT - 150)
    top = pygame.Rect(WIDTH, 0, pipe_width, gap_y - pipe_gap // 2)
    bottom = pygame.Rect(WIDTH, gap_y + pipe_gap // 2, pipe_width, HEIGHT)
    pipes.append((top, bottom))

def move_pipes():
    global score
    for pipe_pair in pipes:
        pipe_pair[0].x -= 4
        pipe_pair[1].x -= 4
    if pipes and pipes[0][0].x + pipe_width < 0:
        pipes.pop(0)
        score += 1

def draw_pipes():
    for top, bottom in pipes:
        pygame.draw.rect(screen, GREEN, top)
        pygame.draw.rect(screen, GREEN, bottom)

def check_collision():
    for top, bottom in pipes:
        if bird.colliderect(top) or bird.colliderect(bottom):
            return True
    if bird.top < 0 or bird.bottom > HEIGHT:
        return True
    return False

def draw_score():
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

running = True
while running:
    clock.tick(60)
    screen.fill(SKY)

    # Gravity
    bird_speed += gravity
    bird.y += int(bird_speed)

    # Pipe logic
    pipe_timer += 1
    if pipe_timer > 90:
        add_pipe()
        pipe_timer = 0

    move_pipes()
    draw_pipes()
    draw_score()
    pygame.draw.rect(screen, RED, bird)

    pygame.display.update()

    # Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird_speed = flap_strength

    if check_collision():
        print("Game Over! Final Score:", score)
        running = False

pygame.quit()

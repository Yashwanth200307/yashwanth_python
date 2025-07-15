import pygame
import math
import random

# Pygame setup
pygame.init()
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # For fullscreen: pygame.FULLSCREEN
pygame.display.set_caption("Iron Man Core Interface")
clock = pygame.time.Clock()

center = (WIDTH // 2, HEIGHT // 2)
angle = 0
pulse_radius = 100
pulse_dir = 1
sparks = []

class Spark:
    def __init__(self):
        self.angle = random.uniform(0, 2 * math.pi)
        self.length = random.randint(50, 100)
        self.speed = random.uniform(2, 5)
        self.fade = 255
        self.pos = list(center)

    def update(self):
        self.pos[0] += math.cos(self.angle) * self.speed
        self.pos[1] += math.sin(self.angle) * self.speed
        self.fade -= 5

    def draw(self, surface):
        if self.fade > 0:
            pygame.draw.circle(surface, (0, 255, 255), (int(self.pos[0]), int(self.pos[1])), 2)

def draw_arc_reactor():
    # Central pulsing core
    global pulse_radius, pulse_dir
    pulse_radius += pulse_dir * 0.5
    if pulse_radius >= 110 or pulse_radius <= 90:
        pulse_dir *= -1

    pygame.draw.circle(screen, (0, 255, 255), center, int(pulse_radius), 3)
    for r in range(1, 4):
        pygame.draw.circle(screen, (0, 150, 255), center, int(pulse_radius) + r * 20, 1)
    pygame.draw.circle(screen, (0, 100, 255), center, 6)

def draw_orbiting_particles(angle):
    for i in range(6):
        r = 120
        a = angle + i * 60
        x = center[0] + r * math.cos(math.radians(a))
        y = center[1] + r * math.sin(math.radians(a))
        pygame.draw.circle(screen, (0, 255, 255), (int(x), int(y)), 5)

def draw_radar_sweep(angle):
    r = 250
    x = center[0] + r * math.cos(math.radians(angle))
    y = center[1] + r * math.sin(math.radians(angle))
    pygame.draw.line(screen, (0, 255, 0), center, (x, y), 2)

def draw_sparks():
    if random.randint(0, 5) == 0:
        sparks.append(Spark())
    for spark in sparks[:]:
        spark.update()
        spark.draw(screen)
        if spark.fade <= 0:
            sparks.remove(spark)

running = True
while running:
    clock.tick(60)
    angle = (angle + 1) % 360
    screen.fill((0, 0, 0))

    # Layered animation
    draw_arc_reactor()
    draw_sparks()
    draw_orbiting_particles(angle)
    draw_radar_sweep(angle)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

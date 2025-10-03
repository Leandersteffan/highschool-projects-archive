import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Collision")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Ensure player stays within the screen
        self.rect.clamp_ip(screen.get_rect())

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        self.speed = random.randint(1, 4)
        self.direction = random.choice([-1, 1])

    def update(self):
        self.rect.x += self.speed * self.direction
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.direction *= -1
        self.rect.y += self.speed * self.direction
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.direction *= -1

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for _ in range(15):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

running = True
clock = pygame.time.Clock()
while running:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Check for collisions
    hits = pygame.sprite.spritecollide(player, enemies, True)
    for hit in hits:
        for _ in range(2):
            enemy = Enemy()
            all_sprites.add(enemy)
            enemies.add(enemy)
        print("Kollidiert")

    # Draw
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()

    # frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()

import pygame
import random
pygame.init()
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter 🚀")
player_img = pygame.image.load("player.png")
enemy_img = pygame.image.load("enemy.png")
bullet_img = pygame.image.load("bullet.png")
player_img = pygame.transform.scale(player_img, (50, 50))
enemy_img = pygame.transform.scale(enemy_img, (50, 50))
bullet_img = pygame.transform.scale(bullet_img, (10, 20))
player_x, player_y = WIDTH // 2, HEIGHT - 70
player_speed = 5
bullets = []
enemies = []
enemy_speed = 2
score = 0
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 50:
        player_x += player_speed
    if keys[pygame.K_SPACE]:
        bullets.append([player_x + 20, player_y])  
    for bullet in bullets:
        bullet[1] -= 5
        if bullet[1] < 0:
            bullets.remove(bullet)
    if random.randint(1, 50) == 1:
        enemies.append([random.randint(0, WIDTH - 50), -50])
    for enemy in enemies:
        enemy[1] += enemy_speed
        if enemy[1] > HEIGHT:
            enemies.remove(enemy)
    for bullet in bullets:
        for enemy in enemies:
            if (enemy[0] < bullet[0] < enemy[0] + 50) and (enemy[1] < bullet[1] < enemy[1] + 50):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 10
    screen.blit(player_img, (player_x, player_y))
    for bullet in bullets:
        screen.blit(bullet_img, (bullet[0], bullet[1]))
    for enemy in enemies:
        screen.blit(enemy_img, (enemy[0], enemy[1]))
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    pygame.display.update()
    clock.tick(60)
pygame.quit()

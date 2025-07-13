import pygame
import random
pygame.init()
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter 🚀")
background_img = pygame.image.load("background.jpg")
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
player_img = pygame.image.load("player.png")
enemy1_img = pygame.image.load("enemy1.png")
enemy2_img = pygame.image.load("enemy.png")
boss_img = pygame.image.load("boss.png")
bullet_img = pygame.image.load("bullet.png")
powerup_img = pygame.image.load("powerup.png")
player_img = pygame.transform.scale(player_img, (50, 50))
enemy1_img = pygame.transform.scale(enemy1_img, (50, 50))
enemy2_img = pygame.transform.scale(enemy2_img, (50, 50))
boss_img = pygame.transform.scale(boss_img, (80, 80))
bullet_img = pygame.transform.scale(bullet_img, (10, 20))
powerup_img = pygame.transform.scale(powerup_img, (30, 30))
player_x, player_y = WIDTH // 2, HEIGHT - 70
player_speed = 5
bullets = []
enemies = []
powerups = []
enemy_speed = 2
score = 0
health = 3
game_over = False
clock = pygame.time.Clock()
def restart_game():
    global player_x, player_y, bullets, enemies, powerups, score, health, game_over
    player_x, player_y = WIDTH // 2, HEIGHT - 70
    bullets = []
    enemies = []
    powerups = []
    score = 0
    health = 3
    game_over = False
while True:
    screen.blit(background_img, (0, 0)) 
    if game_over:
        font = pygame.font.Font(None, 72)
        text = font.render("GAME OVER", True, RED)
        screen.blit(text, (WIDTH // 2 - 150, HEIGHT // 2 - 50))
        font = pygame.font.Font(None, 36)
        restart_text = font.render("Press R to Restart", True, WHITE)
        screen.blit(restart_text, (WIDTH // 2 - 100, HEIGHT // 2 + 30))
        pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            restart_game()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        continue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
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
        enemy_type = random.choice(["normal", "fast", "boss"])
        if enemy_type == "normal":
            enemies.append([random.randint(0, WIDTH - 50), -50, 2, enemy1_img])
        elif enemy_type == "fast":
            enemies.append([random.randint(0, WIDTH - 50), -50, 4, enemy2_img])
        elif enemy_type == "boss":
            enemies.append([random.randint(0, WIDTH - 80), -80, 1, boss_img])
    for enemy in enemies:
        enemy[1] += enemy[2]
        if enemy[1] > HEIGHT:
            enemies.remove(enemy)
            health -= 1
            if health <= 0:
                game_over = True
    if random.randint(1, 300) == 1:
        powerups.append([random.randint(0, WIDTH - 30), -30])
    for powerup in powerups:
        powerup[1] += 3
        if powerup[1] > HEIGHT:
            powerups.remove(powerup)
    for powerup in powerups:
        if player_x < powerup[0] < player_x + 50 and player_y < powerup[1] < player_y + 50:
            powerups.remove(powerup)
            player_speed += 1 
            health += 1  
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
        screen.blit(enemy[3], (enemy[0], enemy[1]))
    for powerup in powerups:
        screen.blit(powerup_img, (powerup[0], powerup[1]))
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    health_text = font.render(f"Health: {health}", True, GREEN)
    screen.blit(score_text, (10, 10))
    screen.blit(health_text, (10, 40))
    pygame.display.update()
    clock.tick(60)

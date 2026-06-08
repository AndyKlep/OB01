import pygame
import random

# -------------------------------
# Настройки игры
# -------------------------------
WIDTH = 800
HEIGHT = 600
FPS = 60

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 30
PLAYER_SPEED = 6

PIXEL_SIZE = 12
PIXEL_SPEED_MIN = 3
PIXEL_SPEED_MAX = 7
SPAWN_DELAY = 250  # миллисекунды между появлениями пикселей

GAME_DURATION = 20  # длительность одной игровой сессии в секундах

BG_COLOR = (20, 20, 30)
PLAYER_COLOR = (80, 220, 120)
PIXEL_COLOR = (255, 80, 80)
TEXT_COLOR = (240, 240, 240)

# -------------------------------
# Инициализация
# -------------------------------
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Bullet Hell")
clock = pygame.time.Clock()

font_big = pygame.font.SysFont("arial", 36)
font_small = pygame.font.SysFont("arial", 24)

# -------------------------------
# Игровые данные
# -------------------------------
player = pygame.Rect(
    WIDTH // 2 - PLAYER_WIDTH // 2,
    HEIGHT - 70,
    PLAYER_WIDTH,
    PLAYER_HEIGHT
)

pixels = []

game_state = "start"   # start, playing, game_over
hits = 0
session_time = 0.0
start_ticks = 0
last_spawn_time = 0


def reset_game():
    global player, pixels, hits, session_time, start_ticks, last_spawn_time, game_state

    player.x = WIDTH // 2 - PLAYER_WIDTH // 2
    player.y = HEIGHT - 70

    pixels = []
    hits = 0
    session_time = 0.0

    start_ticks = pygame.time.get_ticks()
    last_spawn_time = start_ticks
    game_state = "playing"


def spawn_pixel():
    x = random.randint(0, WIDTH - PIXEL_SIZE)
    y = -PIXEL_SIZE
    speed = random.randint(PIXEL_SPEED_MIN, PIXEL_SPEED_MAX)

    pixel_rect = pygame.Rect(x, y, PIXEL_SIZE, PIXEL_SIZE)
    pixels.append({
        "rect": pixel_rect,
        "speed": speed,
        "hit": False
    })


def draw_text_center(text, font, color, y):
    surface = font.render(text, True, color)
    rect = surface.get_rect(center=(WIDTH // 2, y))
    screen.blit(surface, rect)


running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if game_state in ("start", "game_over"):
                    reset_game()

    # -------------------------------
    # Логика игры
    # -------------------------------
    if game_state == "playing":
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player.left > 0:
            player.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and player.right < WIDTH:
            player.x += PLAYER_SPEED

        current_ticks = pygame.time.get_ticks()

        # Спавн падающих пикселей
        if current_ticks - last_spawn_time >= SPAWN_DELAY:
            spawn_pixel()
            last_spawn_time = current_ticks

        # Движение пикселей и проверка столкновений
        for pixel in pixels:
            pixel["rect"].y += pixel["speed"]

            if pixel["rect"].colliderect(player) and not pixel["hit"]:
                hits += 1
                pixel["hit"] = True

        # Удаляем пиксели, которые улетели вниз
        pixels = [p for p in pixels if p["rect"].top <= HEIGHT]

        # Считаем время сессии
        session_time = (current_ticks - start_ticks) / 1000

        # Конец игры по таймеру
        if session_time >= GAME_DURATION:
            game_state = "game_over"

    # -------------------------------
    # Отрисовка
    # -------------------------------
    screen.fill(BG_COLOR)

    if game_state == "start":
        draw_text_center("Simple Bullet Hell", font_big, TEXT_COLOR, 200)
        draw_text_center("Нажми Enter, чтобы начать", font_small, TEXT_COLOR, 270)
        draw_text_center("Стрелки влево/вправо — движение", font_small, TEXT_COLOR, 320)

    elif game_state == "playing":
        # Игрок
        pygame.draw.rect(screen, PLAYER_COLOR, player)

        # Падающие пиксели
        for pixel in pixels:
            pygame.draw.rect(screen, PIXEL_COLOR, pixel["rect"])

        # HUD
        time_text = font_small.render(f"Time: {session_time:.1f}", True, TEXT_COLOR)
        hits_text = font_small.render(f"Hits: {hits}", True, TEXT_COLOR)

        screen.blit(time_text, (20, 20))
        screen.blit(hits_text, (20, 50))

    elif game_state == "game_over":
        draw_text_center("Игра окончена", font_big, TEXT_COLOR, 180)
        draw_text_center(f"Длительность сессии: {session_time:.1f} сек", font_small, TEXT_COLOR, 260)
        draw_text_center(f"Попаданий по игроку: {hits}", font_small, TEXT_COLOR, 300)
        draw_text_center("Нажми Enter, чтобы сыграть снова", font_small, TEXT_COLOR, 360)

    pygame.display.flip()

pygame.quit()
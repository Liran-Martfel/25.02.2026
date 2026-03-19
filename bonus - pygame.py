import pygame
import random
import sys

# אתחול
pygame.init()

# הגדרות מסך
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flag Painter Quiz - No Images Needed")

# פלטת צבעים
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (218, 18, 26)
BLUE = (0, 35, 149)
GREEN = (0, 146, 70)
YELLOW = (255, 204, 0)
GOLD = (255, 204, 0)

# פונטים
font_q = pygame.font.SysFont("Arial", 35, bold=True)
font_ui = pygame.font.SysFont("Arial", 25)

# נתונים מבוססים על הרשימה שלך
quiz_data = [
    {"country": "France", "options": ["Paris", "Lyon", "Marseille", "Nice"], "ans": 1},
    {"country": "Italy", "options": ["Milan", "Venice", "Rome", "Naples"], "ans": 3},
    {"country": "Spain", "options": ["Barcelona", "Seville", "Madrid", "Valencia"], "ans": 3},
    {"country": "Japan", "options": ["Osaka", "Tokyo", "Kyoto", "Hiroshima"], "ans": 2},
    {"country": "Netherlands", "options": ["Rotterdam", "Utrecht", "Eindhoven", "Amsterdam"], "ans": 4},
    {"country": "Germany", "options": ["Berlin", "Munich", "Hamburg", "Frankfurt"], "ans": 1},
    {"country": "Israel", "options": ["Tel Aviv", "Haifa", "Jerusalem", "Eilat"], "ans": 3}
]


def draw_flag(country, x, y):
    """מציירת דגל גיאומטרי לפי שם המדינה"""
    w, h = 300, 180
    flag_surf = pygame.Surface((w, h))
    flag_surf.fill(WHITE)

    if country == "France":
        pygame.draw.rect(flag_surf, (0, 38, 84), (0, 0, w // 3, h))
        pygame.draw.rect(flag_surf, WHITE, (w // 3, 0, w // 3, h))
        pygame.draw.rect(flag_surf, (237, 41, 57), (2 * w // 3, 0, w // 3, h))

    elif country == "Italy":
        pygame.draw.rect(flag_surf, (0, 146, 70), (0, 0, w // 3, h))
        pygame.draw.rect(flag_surf, WHITE, (w // 3, 0, w // 3, h))
        pygame.draw.rect(flag_surf, (206, 43, 55), (2 * w // 3, 0, w // 3, h))

    elif country == "Netherlands":
        pygame.draw.rect(flag_surf, (174, 28, 40), (0, 0, w, h // 3))
        pygame.draw.rect(flag_surf, WHITE, (0, h // 3, w, h // 3))
        pygame.draw.rect(flag_surf, (33, 70, 139), (0, 2 * h // 3, w, h // 3))

    elif country == "Germany":
        pygame.draw.rect(flag_surf, BLACK, (0, 0, w, h // 3))
        pygame.draw.rect(flag_surf, (221, 0, 0), (0, h // 3, w, h // 3))
        pygame.draw.rect(flag_surf, (255, 206, 0), (0, 2 * h // 3, w, h // 3))

    elif country == "Japan":
        flag_surf.fill(WHITE)
        pygame.draw.circle(flag_surf, (188, 0, 45), (w // 2, h // 2), 55)

    elif country == "Spain":
        pygame.draw.rect(flag_surf, (170, 21, 27), (0, 0, w, h // 4))
        pygame.draw.rect(flag_surf, (255, 196, 0), (0, h // 4, w, h // 2))
        pygame.draw.rect(flag_surf, (170, 21, 27), (0, 3 * h // 4, w, h // 4))
        # סמל קטן (עיגול) כדי לסמל את ספרד
        pygame.draw.circle(flag_surf, (170, 21, 27), (w // 4, h // 2), 20, 2)

    elif country == "Israel":
        flag_surf.fill(WHITE)
        pygame.draw.rect(flag_surf, (0, 56, 184), (0, 25, w, 25))
        pygame.draw.rect(flag_surf, (0, 56, 184), (0, h - 50, w, 25))
        # מגן דוד פשוט משני משולשים
        p1 = [(w // 2, h // 2 - 35), (w // 2 - 30, h // 2 + 20), (w // 2 + 30, h // 2 + 20)]
        p2 = [(w // 2, h // 2 + 35), (w // 2 - 30, h // 2 - 20), (w // 2 + 30, h // 2 - 20)]
        pygame.draw.polygon(flag_surf, (0, 56, 184), p1, 3)
        pygame.draw.polygon(flag_surf, (0, 56, 184), p2, 3)

    # מסגרת שחורה דקה סביב הדגל
    pygame.draw.rect(flag_surf, BLACK, (0, 0, w, h), 2)
    screen.blit(flag_surf, (x, y))


# משתני משחק
score, miss = 0, 0
current_q = random.choice(quiz_data)
game_over = False

clock = pygame.time.Clock()

while True:
    screen.fill((245, 245, 245))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if not game_over and event.type == pygame.KEYDOWN:
            val = 0
            if event.key == pygame.K_1:
                val = 1
            elif event.key == pygame.K_2:
                val = 2
            elif event.key == pygame.K_3:
                val = 3
            elif event.key == pygame.K_4:
                val = 4

            if val > 0:
                if val == current_q["ans"]:
                    score += 1
                else:
                    miss += 1

                quiz_data.remove(current_q)
                if score >= 5 or miss >= 3 or not quiz_data:
                    game_over = True
                else:
                    current_q = random.choice(quiz_data)

    if not game_over:
        # טקסט שאלה
        title = font_q.render(f"What is the capital of {current_q['country']}?", True, BLACK)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))

        # ציור הדגל
        draw_flag(current_q["country"], WIDTH // 2 - 150, 130)

        # אפשרויות
        for i, opt in enumerate(current_q["options"]):
            opt_txt = font_ui.render(f"{i + 1}. {opt}", True, BLUE)
            screen.blit(opt_txt, (WIDTH // 2 - 100, 350 + (i * 45)))

        # ניקוד
        status = font_ui.render(f"Score: {score}/5 | Misses: {miss}/3", True, BLACK)
        screen.blit(status, (20, 20))
    else:
        # סיום
        res = "WINNER !!!" if score >= 5 else "GAME OVER !!!"
        col = (0, 150, 0) if score >= 5 else (200, 0, 0)
        screen.blit(font_q.render(res, True, col), (WIDTH // 2 - 100, HEIGHT // 2))

    pygame.display.flip()
    clock.tick(60)
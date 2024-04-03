import pygame

# Inicializace Pygame
pygame.init()

# Nastavení velikosti okna
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Geometrické tvary")

# Hlavní smyčka
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255, 0, 0), (100, 100, 100, 400))
    pygame.draw.circle(window, (0, 255, 0), (400, 300), 100)
    pygame.draw.polygon(window, (0, 0, 255), [(350, 150), (450, 150), (400, 50)])
    pygame.display.update()

pygame.quit()
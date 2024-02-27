import pygame
pygame.init()

screen = pygame.display.set_mode([500,500])
default_font = pygame.font.Font(None, 32)
test_cap = 'hello world me'

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # window creaated
    screen.fill((255,255,255))

    # need to switch out test_cap for the input in threes and update each time
    text_surface = default_font.render(test_cap, True, (00,00,00))
    text_rec = text_surface.get_rect(center=(250,250))
    screen.blit(text_surface, text_rec)

    pygame.display.flip()
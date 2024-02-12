import pygame

a = int(input())
b = int(input())

if a <= 0 and b <= 0:
    print('Неправильный формат ввода')
else:
    pygame.init()
    win = pygame.display.set_mode((a, b))
    pygame.display.set_caption('Крест')

    win.fill((0, 0, 0))

    pygame.draw.line(win, (0, 255, 255), (0, 0), (a, b), 5)
    pygame.draw.line(win, (0, 255, 255), (a, 0), (0, b), 5)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               exit()
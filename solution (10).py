import pygame
import requests

map_file = 'map.png'


def gm(ln, lt, m):
    global map_file
    map_request = "http://static-maps.yandex.ru/1.x/?ll=37.530887,55.703118&spn=0.002,0.002&l=map" \
        f"?ll={ln},{lt}&spn={m},{str(float(m) / 2)}&size=500,450&l={mod}"
    response = requests.get(map_request)
    if str(response) != '<Response [404]>':
        print('OK')
        with open(map_file, 'wb') as file:
            file.write(response.content)
    else:
        print('Error')


pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Maps ip')
running = True
lnn = input('ВВедите долготу')
ltt = input('ВВедите широту')
mm = input('Введите масштаб 0-17')
mod = 'map'
perem = 0
gm(lnn, ltt, mm)

screen.blit(pygame.image.load(map_file), (0, 0))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOW:
            if event.key == pygame.K_UP and (float(ltt) + float(mm) > 90):
                ltt = (str(float(ltt)) - 0.5 * float(mm))
                gm(lnn, ltt, mm)
                screen.blit(pygame.image.load(map_file), (0, 0))

            if event.key == pygame.K_DOWN and (float(ltt) - float(mm) > -90):
                ltt = (str(float(ltt)) - 0.5 * float(mm))
                gm(lnn, ltt, mm)
                screen.blit(pygame.image.load(map_file), (0, 0))

            if event.key == pygame.K_LEFT and (float(ltt) + float(mm) < 180):
                ltt = (str(float(ltt)) + 0.5 * float(mm))
                gm(lnn, ltt, mm)
                screen.blit(pygame.image.load(map_file), (0, 0))

            if event.key == pygame.K_RIGHT and (float(ltt) - float(mm) < -180):
                ltt = (str(float(ltt)) - 0.5 * float(mm))
                gm(lnn, ltt, mm)
                screen.blit(pygame.image.load(map_file), (0, 0))

            if event.key == pygame.K_PAGEUP and (float(mm) < 175):
                mm = str(float(mm) + 5)
                gm(lnn, ltt, mm)
                screen.blit(pygame.image.load(map_file), (0, 0))

            if event.key == pygame.K_PAGEDOWN and (float(mm) < 175):
                mm = str(float(mm) - 5)
                gm(lnn, ltt, mm)
                screen.blit(pygame.image.load(map_file), (0, 0))

            if event.key == pygame.K_k:
                if perem == 0:
                    mod = 'sat'
                    perem = perem + 1
                    screen.blit(pygame.image.load(map_file), (0, 0))
                if perem == 1:
                    mod = 'sat,skl'
                    perem = perem + 1
                    screen.blit(pygame.image.load(map_file), (0, 0))
                if perem == 2:
                    mod = 'map'
                    perem = 0
                    screen.blit(pygame.image.load(map_file), (0, 0))




    pygame.quit()
    pygame.display.flip()


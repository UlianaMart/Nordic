import pygame
import os
import sys

def music():
    pygame.mixer.music.load("data/музыка на фон.mp3")
    pygame.mixer.music.play(-1)

def conflict():
    conflict = pygame.mixer.Sound("data/души.mp3")
    conflict.play()

def end():
    end = pygame.mixer.Sound("data/выигрыш.mp3")
    end.play()

ri = [[449, 550, 0], [499, 550, 0], [50, 549, 1], [100, 549, 1], [150, 549, 1], [200, 549, 1], [250, 549, 1],
      [300, 549, 1], [350, 549, 1], [400, 549, 1], [500, 549, 1],
      [0, 149, 1], [0, 199, 1], [49, 50, 0], [49, 100, 0], [49, 200, 0], [49, 250, 0], [49, 300, 0], [49, 350, 0],
      [49, 400, 0], [49, 450, 0], [49, 500, 0],
      [50, 49, 1], [100, 49, 1], [150, 49, 1], [200, 49, 1], [250, 49, 1], [300, 49, 1], [350, 49, 1], [400, 49, 1],
      [450, 49, 1], [500, 49, 1],
      [549, 50, 0], [549, 100, 0], [549, 150, 0], [549, 200, 0], [549, 250, 0], [549, 300, 0], [549, 350, 0],
      [549, 400, 0], [549, 450, 0], [549, 500, 0],
      [199, 500, 0], [249, 500, 0], [99, 450, 0], [299, 450, 0], [399, 450, 0], [499, 450, 0],
      [99, 400, 0], [149, 400, 0], [199, 400, 0], [349, 400, 0], [449, 400, 0], [149, 350, 0], [299, 350, 0], [399, 350, 0],
      [99, 300, 0], [149, 300, 0], [199, 300, 0], [249, 300, 0], [449, 300, 0], [499, 300, 0],
      [199, 250, 0], [249, 250, 0], [499, 250, 0], [199, 200, 0],
      [99, 150, 0], [149, 150, 0], [199, 150, 0], [249, 150, 0], [499, 150, 0],
      [99, 100, 0], [199, 100, 0], [399, 100, 0], [249, 50, 0], [349, 50, 0],
      [150, 499, 1], [250, 499, 1], [300, 499, 1], [350, 499, 1], [150, 449, 1], [350, 449, 1], [450, 449, 1],
      [50, 399, 1], [200, 399, 1], [250, 399, 1], [350, 399, 1], [450, 399, 1], [500, 399, 1],
      [250, 349, 1], [400, 349, 1], [100, 299, 1], [300, 299, 1], [350, 299, 1], [400, 299, 1],
      [50, 249, 1], [100, 249, 1], [150, 249, 1], [250, 249, 1], [300, 249, 1], [350, 249, 1], [400, 249, 1],
      [450, 249, 1], [500, 249, 1],
      [100, 199, 1], [200, 199, 1], [300, 199, 1], [350, 199, 1], [400, 199, 1], [450, 199, 1],
      [250, 149, 1], [300, 149, 1], [350, 149, 1], [400, 149, 1], [450, 149, 1],
      [50, 99, 1], [150, 99, 1], [250, 99, 1], [450, 99, 1], [500, 99, 1]]

riri = [[49, 550, 0], [99, 550, 0], [450, 549, 1], [100, 549, 1], [150, 549, 1], [200, 549, 1], [250, 549, 1],
      [300, 549, 1], [350, 549, 1], [400, 549, 1], [500, 549, 1],
      [49, 150, 0], [49, 50, 0], [49, 100, 0], [49, 200, 0], [49, 250, 0], [49, 300, 0], [49, 350, 0],
      [49, 400, 0], [49, 450, 0], [49, 500, 0],
      [50, 49, 1], [100, 49, 1], [150, 49, 1], [200, 49, 1], [250, 49, 1], [300, 49, 1], [350, 49, 1], [400, 49, 1],
      [450, 49, 1], [500, 49, 1],
      [549, 50, 0], [549, 100, 0], [550, 149, 1], [550, 199, 1], [549, 200, 0], [549, 250, 0], [549, 300, 0], [549, 350, 0],
      [549, 400, 0], [549, 450, 0], [549, 500, 0],
      [99, 500, 0], [249, 500, 0], [149, 450, 0], [199, 450, 0], [249, 450, 0], [299, 450, 0], [399, 450, 0], [449, 450, 0],
      [99, 400, 0], [249, 400, 0], [449, 400, 0], [499, 400, 0], [249, 350, 0], [299, 350, 0], [449, 350, 0],
      [199, 300, 0], [249, 300, 0], [299, 300, 0], [349, 300, 0], [449, 300, 0], [99, 250, 0], [249, 250, 0], [399, 250, 0], [449, 250, 0],
      [449, 200, 0], [399, 200, 0], [199, 200, 0], [99, 200, 0], [199, 150, 0], [249, 150, 0], [399, 150, 0], [449, 150, 0],
      [99, 100, 0], [199, 100, 0], [299, 100, 0], [349, 100, 0], [399, 100, 0], [99, 50, 0], [299, 50, 0],
      [100, 499, 1], [200, 499, 1], [300, 499, 1], [350, 499, 1], [450, 499, 1], [50, 449, 1], [250, 449, 1], [350, 449, 1], [500, 449, 1],
      [100, 399, 1], [150, 399, 1], [300, 399, 1], [350, 399, 1], [400, 399, 1],
      [50, 349, 1], [100, 349, 1], [150, 349, 1], [350, 349, 1], [450, 349, 1], [100, 299, 1], [150, 299, 1], [300, 299, 1], [500, 299, 1],
      [150, 249, 1], [200, 249, 1], [250, 249, 1], [300, 249, 1], [350, 249, 1], [450, 249, 1], [100, 199, 1], [250, 199, 1], [350, 199, 1],
      [100, 149, 1], [250, 149, 1], [300, 149, 1], [450, 149, 1], [500, 149, 1],
      [150, 99, 1], [200, 99, 1], [400, 99, 1], [450, 99, 1]]

ririri = [[299, 550, 0], [349, 550, 0], [450, 549, 1], [100, 549, 1], [150, 549, 1], [200, 549, 1], [250, 549, 1],
      [50, 549, 1], [350, 549, 1], [400, 549, 1], [500, 549, 1],
      [49, 150, 0], [49, 50, 0], [49, 100, 0], [49, 200, 0], [49, 250, 0], [49, 300, 0], [49, 350, 0],
      [49, 400, 0], [49, 450, 0], [49, 500, 0],
      [50, 49, 1], [100, 49, 1], [150, 49, 1], [200, 49, 1], [249, 0, 0], [299, 0, 0], [300, 49, 1], [350, 49, 1], [400, 49, 1],
      [450, 49, 1], [500, 49, 1],
      [549, 50, 0], [549, 100, 0], [549, 150, 0], [549, 200, 0], [549, 250, 0], [549, 300, 0], [549, 350, 0],
      [549, 400, 0], [549, 450, 0], [549, 500, 0],
      [149, 500, 0], [299, 500, 0], [349, 500, 0], [99, 450, 0], [199, 450, 0], [249, 450, 0], [349, 450, 0], [399, 450, 0], [449, 450, 0], [499, 450, 0],
      [149, 400, 0], [249, 400, 0], [449, 400, 0], [499, 400, 0], [99, 350, 0], [149, 350, 0], [199, 350, 0], [399, 350, 0], [449, 350, 0], [499, 350, 0],
      [99, 300, 0], [199, 300, 0], [299, 300, 0], [399, 300, 0], [449, 300, 0], [499, 300, 0], [99, 250, 0], [149, 250, 0], [249, 250, 0], [349, 250, 0], [449, 250, 0],
      [99, 200, 0], [199, 200, 0], [299, 200, 0], [399, 200, 0], [499, 200, 0], [199, 150, 0], [299, 150, 0], [399, 150, 0], [449, 150, 0], [499, 150, 0],
      [99, 100, 0], [199, 100, 0], [249, 100, 0], [399, 100, 0], [449, 100, 0], [349, 50, 0], [449, 50, 0],
      [250, 499, 1], [450, 499, 1], [100, 449, 1], [150, 449, 1], [350, 449, 1],
      [150, 399, 1], [250, 399, 1], [300, 399, 1], [350, 399, 1], [400, 399, 1], [450, 399, 1],
      [100, 349, 1], [200, 349, 1], [300, 349, 1], [150, 299, 1], [250, 299, 1], [350, 299, 1],
      [200, 249, 1], [300, 249, 1], [450, 249, 1], [400, 249, 1], [100, 199, 1], [150, 199, 1], [250, 199, 1], [350, 199, 1],
      [100, 149, 1], [150, 149, 1], [200, 149, 1], [100, 99, 1], [250, 99, 1], [300, 99, 1], [450, 99, 1]]


def load_image(name, colorkey=-1):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

fireth = [[160, 510, 'B', 3, 1], [360, 510, 'R', 4, 1], [60, 60, 'R', 10, 0], [210, 60, 'R', 2, 0], [260, 110, 'R', 3, 1], [260, 460, 'B', 2, 1]]
firet = [[410, 110, 'B', 6, 0], [60, 160, 'R', 3, 1], [60, 360, 'R', 4, 1], [260, 510, 'R', 6, 1], [310, 410, 'B', 2, 0], [510, 310, 'B', 3, 0]]
fire = [[360, 60, 'B', 4, 1], [110, 60, 'R', 3, 0], [260, 160, 'R', 2, 0], [260, 310, 'B', 4, 1], [410, 360, 'B', 3, 1], [110, 310, 'B', 5, 0]]


class Blueg(pygame.sprite.Sprite):
    im = pygame.transform.scale(load_image("Синий.png"), (30, 30))

    def __init__(self, group, x, y, n):
        super().__init__(group)
        self.image = Blueg.im
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.s = 1
        self.sc = [x - 10, (x + n * 50) - 40]


    def update(self):
        if self.rect.x <= self.sc[1] and self.rect.x >= self.sc[0]:
            pass
        else:
            self.s *= -1
        self.rect.x += self.s


class Bluev(pygame.sprite.Sprite):
    im = pygame.transform.scale(load_image("Синий.png"), (30, 30))

    def __init__(self, group, x, y, n):
        super().__init__(group)
        self.image = Bluev.im
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.s = 1
        self.sc = [y - 10, (y + n * 50) - 40]

    def update(self):
        if self.rect.y <= self.sc[1] and self.rect.y >= self.sc[0]:
            pass
        else:
            self.s *= -1
        self.rect.y += self.s


class Redg(pygame.sprite.Sprite):
    im = pygame.transform.scale(load_image("Красный.png"), (30, 30))

    def __init__(self, group, x, y, n):
        super().__init__(group)
        self.image = Redg.im
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.s = 1
        self.sc = [x - 10, (x + n * 50) - 40]

    def update(self):
        if self.rect.x <= self.sc[1] and self.rect.x >= self.sc[0]:
            pass
        else:
            self.s *= -1
        self.rect.x += self.s


class Redv(pygame.sprite.Sprite):
    im = pygame.transform.scale(load_image("Красный.png"), (30, 30))

    def __init__(self, group, x, y, n):
        super().__init__(group)
        self.image = Redv.im
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.s = 1
        self.sc = [y - 10, (y + n * 50) - 40]

    def update(self):
        if self.rect.y <= self.sc[1] and self.rect.y >= self.sc[0]:
            pass
        else:
            self.s *= -1
        self.rect.y += self.s

class Hel(pygame.sprite.Sprite):
    im = pygame.transform.scale(load_image("Хель1.png"), (48, 48))
    im2 = pygame.transform.scale(load_image("Хель2.png"), (48, 48))
    im3 = pygame.transform.scale(load_image("Хель3.png"), (48, 48))
    im4 = pygame.transform.scale(load_image("Хель4.png"), (48, 48))

    def __init__(self, group):
        super().__init__(group)
        self.image = Hel.im
        self.rect = self.image.get_rect()
        self.rect.x = 451
        self.rect.y = 551
        self.fl = True
        self.play = True
        self.n = 100
        self.na = [451, 551]
        self.plazo, self.plazt, self.plazth = True, False, False
        self.sten = walo
        self.firr = firesro
        self.firb = firesbo

    def update(self, n, t=0):
        if self.plazo:
            self.sten = walo
            self.firr = firesro
            self.firb = firesbo
        elif self.plazt:
            self.sten = walt
            self.firr = firesrt
            self.firb = firesbt
        elif self.plazth:
            self.sten = walth
            self.firr = firesrth
            self.firb = firesbth
        if t == 1 and self.plazt:
            self.fl = True
            self.rect.x = 51
            self.rect.y = 551
            self.na = [51, 551]
        elif t == 2 and self.plazth:
            self.fl = True
            self.rect.x = 301
            self.rect.y = 551
            self.na = [301, 551]
        elif t == 0:
            '''выигрыш 1, 2'''
            if (self.rect.x <= 1 and self.rect.y == 151):
                self.fl = False
                self.plazo = False
                screen.fill((0, 0, 0))
                win.draw(screen)
                self.image = self.im
                self.plazt = True
            elif (self.rect.x >= 549 and self.rect.y == 151):
                self.fl = False
                self.plazt = False
                screen.fill((0, 0, 0))
                win.draw(screen)
                self.image = self.im
                self.plazth = True
            elif self.rect.x == 251 and self.rect.y <= 1:
                self.fl = False
                screen.fill((0, 0, 0))
                winwin.draw(screen)
                end()
            else:
                for i in range(50):
                    if not pygame.sprite.spritecollideany(self, self.sten) and self.rect.x >= 1 and self.rect.x <= 600 and self.rect.y >= 1 and self.rect.y <= 610:
                        if n == 1:
                            if self.fl:
                                self.rect.x += 1
                                self.image = self.im4
                        elif n == 2:
                            if self.fl:
                                self.rect.x -= 1
                                self.image = self.im3
                        elif n == 3:
                            self.image = self.im2
                            if self.fl:
                                self.rect.y -= 1
                            else:
                                self.fl = True
                                break
                        elif n == 4:
                            if self.fl:
                                self.image = self.im
                                self.rect.y += 1
                        if self.fl:
                            screen.fill((0, 0, 0))
                            all_sprites.draw(screen)
                            self.sten.draw(screen)
                    else:
                        self.fl = False
                        screen.fill((0, 0, 0))
                        over.draw(screen)
                        self.rect.x = self.na[0]
                        self.rect.y = self.na[1]
                        self.n = 100
                        break
                if pygame.sprite.spritecollideany(self, self.firb):
                    self.n -= 15
                    text = font.render(f"{self.n} xp", True, ('Green'))
                    text_x = 530
                    text_y = 15
                    screen.blit(text, (text_x, text_y))
                    conflict()
                if pygame.sprite.spritecollideany(self, self.firr):
                    self.n -= 50
                    text = font.render(f"{self.n} xp", True, ('Green'))
                    text_x = 530
                    text_y = 15
                    screen.blit(text, (text_x, text_y))
                    conflict()
                if self.n <= 0:
                    self.fl = False
                    screen.fill((0, 0, 0))
                    over.draw(screen)
                    self.rect.x = self.na[0]
                    self.rect.y = self.na[1]
                    self.n = 100

    def fir(self):
        if self.fl:
            screen.fill((0, 0, 0))
            self.firr.draw(screen)
            self.firr.update()
            self.firb.draw(screen)
            self.firb.update()
            all_sprites.draw(screen)
            self.sten.draw(screen)
            text = font.render(f"{self.n} xp", True, ('Green'))
            text_x = 530
            text_y = 15
            screen.blit(text, (text_x, text_y))


class Walg(pygame.sprite.Sprite):
    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = pygame.Surface((50, 2))
        self.image.fill(('White'))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Walv(pygame.sprite.Sprite):
    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = pygame.Surface((2, 50))
        self.image.fill(('White'))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Nordic')
    size = width, height = 600, 600
    screen = pygame.display.set_mode(size)
    music()

    font = pygame.font.Font(None, 30)
    all_sprites = pygame.sprite.Group()
    first = pygame.sprite.Group()
    walo = pygame.sprite.Group()
    walt = pygame.sprite.Group()
    walth = pygame.sprite.Group()
    over = pygame.sprite.Group()
    win = pygame.sprite.Group()
    winwin = pygame.sprite.Group()
    firesro = pygame.sprite.Group()
    firesbo = pygame.sprite.Group()
    firesrt = pygame.sprite.Group()
    firesbt = pygame.sprite.Group()
    firesrth = pygame.sprite.Group()
    firesbth = pygame.sprite.Group()
    rules = pygame.sprite.Group()
    sprite = pygame.sprite.Sprite()
    sprite.image = pygame.transform.scale(load_image("Проигрыш.png"), (600, 600))
    sprite.rect = sprite.image.get_rect()
    over.add(sprite)
    sprite = pygame.sprite.Sprite()
    sprite.image = pygame.transform.scale(load_image("Победа.png"), (600, 600))
    sprite.rect = sprite.image.get_rect()
    win.add(sprite)
    sprite = pygame.sprite.Sprite()
    sprite.image = pygame.transform.scale(load_image("Привет.png"), (600, 600))
    sprite.rect = sprite.image.get_rect()
    first.add(sprite)
    first.draw(screen)
    sprite.image = pygame.transform.scale(load_image("Правила.png"), (600, 600))
    sprite.rect = sprite.image.get_rect()
    rules.add(sprite)
    sprite = pygame.sprite.Sprite()
    sprite.image = pygame.transform.scale(load_image("Конец.png"), (600, 600))
    sprite.rect = sprite.image.get_rect()
    winwin.add(sprite)

    a = Hel(all_sprites)
    nacht = False
    nacho = False
    for i in ri:
        if i[2] == 0:
            Walv(walo, i[0], i[1])
        else:
            Walg(walo, i[0], i[1])
    for i in riri:
        if i[2] == 0:
            Walv(walt, i[0], i[1])
        else:
            Walg(walt, i[0], i[1])
    for i in ririri:
        if i[2] == 0:
            Walv(walth, i[0], i[1])
        else:
            Walg(walth, i[0], i[1])
    for i in fire:
        if i[2] == 'B':
            if i[4] == 0:
                Bluev(firesbo, i[0], i[1], i[3])
            else:
                Blueg(firesbo, i[0], i[1], i[3])
        else:
            if i[4] == 0:
                Redv(firesro, i[0], i[1], i[3])
            else:
                Redg(firesro, i[0], i[1], i[3])
    for i in firet:
        if i[2] == 'B':
            if i[4] == 0:
                Bluev(firesbt, i[0], i[1], i[3])
            else:
                Blueg(firesbt, i[0], i[1], i[3])
        else:
            if i[4] == 0:
                Redv(firesrt, i[0], i[1], i[3])
            else:
                Redg(firesrt, i[0], i[1], i[3])
    for i in fireth:
        if i[2] == 'B':
            if i[4] == 0:
                Bluev(firesbth, i[0], i[1], i[3])
            else:
                Blueg(firesbth, i[0], i[1], i[3])
        else:
            if i[4] == 0:
                Redv(firesrth, i[0], i[1], i[3])
            else:
                Redg(firesrth, i[0], i[1], i[3])
    n = 0
    clock = pygame.time.Clock()
    running = True
    nachth = False
    nachf = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_RETURN]:
                    n += 1
                    if n == 1:
                        nacho = True
                    elif n == 2:
                        nacht = True
                    elif n == 3:
                        nachth = True
                    elif n == 4:
                        nachf = True
                if nacho:
                    rules.draw(screen)
                if nacht:
                    nacho = False
                    if pygame.key.get_pressed()[pygame.K_RIGHT]:
                        all_sprites.update(1)
                    if pygame.key.get_pressed()[pygame.K_LEFT]:
                        all_sprites.update(2)
                    if pygame.key.get_pressed()[pygame.K_UP]:
                        all_sprites.update(3)
                    if pygame.key.get_pressed()[pygame.K_DOWN]:
                        all_sprites.update(4)
                if nachth:
                    if nacht:
                        all_sprites.update(1, 1)
                    nacht = False
                    if pygame.key.get_pressed()[pygame.K_RIGHT]:
                        all_sprites.update(1)
                    if pygame.key.get_pressed()[pygame.K_LEFT]:
                        all_sprites.update(2)
                    if pygame.key.get_pressed()[pygame.K_UP]:
                        all_sprites.update(3)
                    if pygame.key.get_pressed()[pygame.K_DOWN]:
                        all_sprites.update(4)
                if nachf:
                    if nachth:
                        all_sprites.update(1, 2)
                    nachth = False
                    if pygame.key.get_pressed()[pygame.K_RIGHT]:
                        all_sprites.update(1)
                    if pygame.key.get_pressed()[pygame.K_LEFT]:
                        all_sprites.update(2)
                    if pygame.key.get_pressed()[pygame.K_UP]:
                        all_sprites.update(3)
                    if pygame.key.get_pressed()[pygame.K_DOWN]:
                        all_sprites.update(4)
        if nacht or nachth or nachf:
            a.fir()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
#Создай собственный Шутер!
from pygame import *
import random
import time as time2

#pic_card/

def give(rand_card):
    rand = random.randint(1, 52) - 1
    return list(cards.keys())[rand]

def create(name_card, num_card):
    return GameSprite(name_card + ".jpg", 120 + num_card * 70 , 280, 130, 170)

def create2(name_card, num_card2):
    return GameSprite(name_card + ".jpg", 120 + num_card2 * 70 , 15, 130, 170)

class GameSprite(sprite.Sprite):
    def __init__(self, images, x, y, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(images), [size_x, size_y])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y))

class Card(GameSprite):
    def give(rand_card):
        rand = random.randint(1, 52) - 1
        return list(cards.keys())[rand]

but = GameSprite("rectangle.png", 10, 420, 100, 80)
but2 = GameSprite("rectangle.png",100, 420, 100, 80)
#создай окно игры
window_size = [700, 500]
window = display.set_mode(window_size)
display.set_caption("21")
#задай фон сцены
background = transform.scale(image.load("fon.jpg"), window_size)

#???

#обработай событие «клик по кнопке "Закрыть окно"»

clock = time.Clock()
FPS = 60
game = True
point1 = 0
point2 = 0
players = sprite.Group()
dealers = sprite.Group()
name_card = " "
num_card = 0
num_card2 = 0
cards = {
    "Туз Пик": 11, "2 Пик": 2, "3 Пик": 3, "4 Пик": 4, "5 Пик": 5,
    "6 Пик": 6, "7 Пик": 7, "8 Пик":8, "9 Пик": 9, "10 Пик": 10, "Валет Пик": 10,
    "Дама Пик": 10, "Король Пик": 10,
    "Туз Черви": 11, "2 Черви": 2, "3 Черви": 3, "4 Черви": 4, "5 Черви": 5,
    "6 Черви": 6, "7 Черви": 7, "8 Черви":8, "9 Черви": 9, "10 Черви": 10, "Валет Черви": 10,
    "Дама Черви": 10, "Король Черви": 10,
    "Туз Бубни": 11, "2 Бубни": 2, "3 Бубни": 3, "4 Бубни": 4, "5 Бубни": 5,
    "6 Бубни": 6, "7 Бубни": 7, "8 Бубни":8, "9 Бубни": 9, "10 Бубни": 10, "Валет Бубни": 10,
    "Дама Бубни": 10, "Король Бубни": 10,
    "Туз Крести": 11, "2 Крести": 2, "3 Крести": 3, "4 Крести": 4, "5 Крести": 5,
    "6 Крести": 6, "7 Крести": 7, "8 Крести":8, "9 Крести": 9, "10 Крести": 10, "Валет Крести": 10,
    "Дама Крести": 10, "Король Крести": 10
    }

#

font.init()
fontmy = font.SysFont('Arial', 40)
fontmy2 = font.SysFont('Arial', 70)
keys = fontmy.render("1 - Hold / 2 - Hit", 1, (255,255,255))

lose = fontmy2.render("ВЫ ПРОИГРАЛИ!",1, (255, 0, 0))

#2 НАЧАЛЬНЫЕ КАРТЫ ИГРОКА
name_card = give(name_card)
point1 += cards[name_card]
num_card += 1
create(name_card, num_card).add(players)
name_card = give(name_card)
point1 += cards[name_card]
num_card += 1
create(name_card, num_card).add(players)


#2 НАЧАЛЬНЫЕ КАРТЫ ДИЛЕРА
name_card = give(name_card)
point2 += cards[name_card]
num_card2 += 1
create2(name_card, num_card2).add(dealers)
name_card = give(name_card)
point2 += cards[name_card]
num_card2 += 1
create2(name_card, num_card2).add(dealers)


while game:
    for e in event.get():
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            x, y = e.pos
            if but.rect.collidepoint(x, y):
                print("Hold")
            if but2.rect.collidepoint(x, y) and point1 <= 21:
                name_card = give(name_card)
                point1 += cards[name_card]
                num_card += 1
                create(name_card, num_card).add(players)

        if e.type == QUIT:
            game = False

    card_point1 = fontmy.render(str(point1), 1, (255, 255,255))
    card_point2 = fontmy.render(str(point2), 1, (255, 255,255))


    window.blit(background, (0,0))
    window.blit(card_point1, (310, 450))
    window.blit(card_point2, (310, 180))


    but.reset()
    but2.reset()
    players.draw(background)
    dealers.draw(background)

    display.update()
    clock.tick(FPS)

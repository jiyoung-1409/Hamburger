import pygame
import datetime as dt
import random

from images import *

pygame.init()

screen_w = 640
screen_h = 480
screen = pygame.display.set_mode((screen_w, screen_h))

pygame.display.set_caption('hamburger')

clock = pygame.time.Clock()

bg_rect = BG.get_rect()
bg_h = bg_rect[3]
bg_w = bg_rect[2]

font = pygame.font.Font('./image/arial.ttf', 15)

LOC = "bg_1"

def draw_bg():
    x = 0
    y = 0

    global LOC, bg_h

    if LOC == "bg_2":
        y = -(bg_h - 480)    
    elif LOC == "bg_3":
        x = -(bg_w - 640)
        y = -(bg_h - 480)  
    elif LOC == 'bg_4':
        x = -(bg_w - 640)

    screen.blit(BG, (x, y))

class Button():
    def __init__(self, x, y, image, screen):
        width = image.get_width()
        height = image.get_height()
        self.screen = screen
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
		#get mouse position
        pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

		#draw button on screen
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

        return action


def draw_arrow():
    global LOC

    if LOC == "bg_1":

        down_btn = Button(screen_w/2 - 25, screen_h - 30, pygame.transform.flip(ARROW_UD, False, True), screen)
        if down_btn.draw(screen):
            LOC = "bg_2"

        right_btn = Button(screen_w - 30, screen_h/2 - 25, ARROW_RL, screen)
        if right_btn.draw(screen):
            LOC = "bg_4"

    elif LOC == "bg_2":

        up_btn = Button(screen_w/2 - 25, 0, ARROW_UD, screen)
        if up_btn.draw(screen):
            LOC = "bg_1"

        right_btn = Button(screen_w - 30, screen_h/2 - 25, ARROW_RL, screen)
        if right_btn.draw(screen):
            LOC = "bg_3"

    elif LOC == "bg_3":

        up_btn = Button(screen_w/2 - 25, 0, ARROW_UD, screen)
        if up_btn.draw(screen):
            LOC = "bg_4"

        left_btn = Button(0, screen_h/2 - 25, pygame.transform.flip(ARROW_RL, True, False), screen)
        if left_btn.draw(screen):
            LOC = "bg_2"

    elif LOC == "bg_4":

        down_btn = Button(screen_w/2 - 25, screen_h - 30, pygame.transform.flip(ARROW_UD, False, True), screen)
        if down_btn.draw(screen):
            LOC = "bg_3"

        left_btn = Button(0, screen_h/2 - 25, pygame.transform.flip(ARROW_RL, True, False), screen)
        if left_btn.draw(screen):
            LOC = "bg_1"


def tell(str):
    if str == 'tomato_icon':
        return TOMATO_ICON
    elif str == 'pickle_icon':
        return PICKLE_ICON
    elif str == 'onion_icon':
        return ONION_ICON
    elif str == 'romain_icon':
        return ROMAIN_ICON
    elif str == 'cheess_icon':
        return CHEESE_ICON
    elif str == 'patty_row_icon':
        return PATTY_ROW_ICON
    elif str == 'patty_cheese':
        return PATTY_CHEESE
    elif str == 'none':
        pass

ingre_lst = ['tomato_icon', 'onion_icon', 'pickle_icon', 'patty_icon', 'romain_icon', 'cheese_icon']
order_lst = []

for i in range(5):
    order_lst.append(random.choice(ingre_lst))
    order_lst[i] = order_lst[i][:-5]

order_text = ''
for i in range(5):
    if order_lst.count(order_lst[i]) > 1:
        if str(order_lst[i]) not in order_text:
            order_text += '{0} {1} ' .format(order_lst.count(order_lst[i]), order_lst[i])
    else:
        order_text += '1 {0} ' .format(order_lst[i])
order_text += 'please.'

in_mouse = ['none']
burger = ['bread']

temp = 0
ding = None

grill_on = 0
second = []

served = False

def draw_ingre():

    global bread, tomato, pickle, onion, burger, temp, ding, served

    global LOC

    if LOC == 'bg_1':

        if ding == True:

            screen.blit(BREAD, (300, 280))

            if len(burger) > 1 and burger[1] != None:
                screen.blit(tell(burger[1]), (300, (280 - 10)))
                if len(burger) > 2 and burger[2] != None:
                    screen.blit(tell(burger[2]), (300, (280  - 20)))
                    if len(burger) > 3 and burger[3] != None:
                        screen.blit(tell(burger[3]), (300, (280  - 30)))
                        if len(burger) > 4 and burger[4] != None:
                            screen.blit(tell(burger[4]), (300, (280  - 40)))
                            if len(burger) > 5 and burger[5] != None:
                                screen.blit(tell(burger[5]), (300, (280  - 50)))

            screen.blit(BREAD_TOP, (300, 280 - temp * 10))

            served = True

    elif LOC == 'bg_2':

        bread = Button(450, 300, BREAD, screen)
        if bread.draw(screen):
            if in_mouse[0] != 'none' and len(burger) <= 5:
                burger.append(in_mouse[0])
                # burger = list(dict.fromkeys(burger))
                in_mouse[0] = 'none'

        bell = Button(550, 180, BELL, screen)
        if bell.draw(screen):
            ding = True
            temp = int(len(burger))

        tomato = Button(170, 180, TOMATO, screen)
        if tomato.draw(screen):
            in_mouse[0] = 'tomato_icon'

        pickle = Button(170, 290, PICKLE, screen)
        if pickle.draw(screen):
            in_mouse[0] = 'pickle_icon'

        onion = Button(2, 290, ONION, screen)
        if onion.draw(screen):
            in_mouse[0] = 'onion_icon'

        if in_mouse[0] == 'none':
            pass
        else:
            if len(burger) <= 5:
                screen.blit(tell(in_mouse[0]), (mouse_pos[0]-20, mouse_pos[1]-20))
        
        if len(burger) > 1 and burger[1] != None and served == False:
            screen.blit(tell(burger[1]), (450, (300 - 10)))
            if len(burger) > 2 and burger[2] != None:
                screen.blit(tell(burger[2]), (450, (300  - 20)))
                if len(burger) > 3 and burger[3] != None:
                    screen.blit(tell(burger[3]), (450, (300  - 30)))
                    if len(burger) > 4 and burger[4] != None:
                        screen.blit(tell(burger[4]), (450, (300  - 40)))
                        if len(burger) > 5 and burger[5] != None:
                            screen.blit(tell(burger[5]), (450, (300  - 50)))

        if ding == True and served == False:
            screen.blit(BREAD_TOP, (450, 310 - temp * 10))

    global grill_on, second

    if LOC == 'bg_3' or LOC == 'bg_4':

        if LOC != 'bg_4':

            cheess = Button(150, -20, CHEESE, screen)
            if cheess.draw(screen):
                in_mouse[0] = 'cheess_icon'

            patty = Button(300, -20, PATTY, screen)
            if patty.draw(screen):
                in_mouse[0] = 'patty_row_icon'

            grill = Button(128, 160, GRILL, screen)
            if grill.draw(screen):
                if in_mouse[0] == 'patty_row_icon':
                    grill_on = 1
                

            if grill_on == 1:
                screen.blit(PATTY_ROW_ICON, (220, 240))
                in_mouse[0] = 'none' 

                now = dt.datetime.now()
                second.append(now.strftime("%S"))

                if int(second[0]) + 2 == int(dt.datetime.now().strftime('%S')):
                    print('cooked')
                    grill_on = 2

            elif grill_on == 2:
                cooked_patty = Button(220, 240, PATTY_ICON, screen)
                if cooked_patty.draw(screen):
                    if in_mouse[0] == 'cheess_icon':
                        in_mouse[0] = 'none'
                        grill_on = 3

            elif grill_on == 3:
                patty_cheese = Button(220, 240, PATTY_CHEESE, screen)
                if patty_cheese.draw(screen):
                    in_mouse[0] = 'patty_cheese'
                    grill_on = 0

            elif grill_on == 0:
                pass


        if LOC != 'bg_3':

            romain = Button(150, 150, ROMAIN, screen)
            if romain.draw(screen):
                in_mouse[0] = 'romain_icon'

            cheess = Button(150, 275, CHEESE, screen)
            if cheess.draw(screen):
                in_mouse[0] = 'cheess_icon'

            patty = Button(300, 275, PATTY, screen)
            if patty.draw(screen):
                in_mouse[0] = 'patty_row_icon'

        if in_mouse[0] == 'none':
            pass
        else:
            screen.blit(tell(in_mouse[0]), (mouse_pos[0]-20, mouse_pos[1]-20)) 

    order_icon = Button(10, 10, ORDER_ICON, screen)
    if order_icon.draw(screen):
        screen.blit(ORDER, (10, 10))
    
    return burger

acc = None

def customer():

    global acc, order_text, ding

    if ding == True:
        for factor in order_lst:
            if factor not in draw_ingre():
                acc = False
        
    if LOC == 'bg_1':
        if acc == True:
            order_text = 'thank you!'
        elif acc == False:
            order_text = 'no..'
        order_msg = font.render(order_text, True, (0, 0, 0))
        msg_rect = order_msg.get_rect(center = (390, 120))
        screen.blit(order_msg, msg_rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            pass

        if event.type == pygame.KEYUP:
            pass
    
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    draw_bg()

    draw_ingre()
    draw_arrow()

    customer()

    pygame.display.update()

pygame.quit()

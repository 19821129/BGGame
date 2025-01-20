import sys
import random
import pygame

pygame.init() 
size = 27
queue = 30
game_lis = []  
background_color = (255, 239, 213)  
Dividingline_color = (255, 222, 173)  
Dividingline_width = 0

score_height = 120  
score_width = 140  
score_color = (205, 193, 180)  
font1 = pygame.font.SysFont('SimHei', 50) 
font_pos_x = Dividingline_width  
font_pos_y = int(font1.size('分数')[1])  
score = 0  

font3 = pygame.font.Font(None, 15) 
black = (0, 0, 0)  

screen_height = (((size + Dividingline_width) * queue) + score_height + Dividingline_width * 2)  
screen_width = (((size + Dividingline_width) * queue) + Dividingline_width)  

colors = {0: (205, 193, 180),  
          2: (238, 228, 218),
          4: (237, 224, 200),
          8: (242, 177, 121),
          16: (245, 149, 99),
          32: (246, 124, 95),
          64: (246, 94, 59),
          128: (237, 207, 114),
          256: (237, 204, 98),
          512: (237, 200, 80),
          1024: (237, 197, 63),
          2048: (225, 187, 0),
          4096: (115, 223, 10),
          8192: (0, 222, 11),
          16384: (19, 29, 149),
          32768: (193, 200, 10),
          65536: (100, 139, 0),
          131072: (100, 139, 40),
          262144: (220, 139, 40),}



def _draw_background(screen):
    screen.fill(background_color)
    Dividingline_width_half = int(Dividingline_width / 2)
    Difference = score_height + Dividingline_width + int(Dividingline_width / 2)

    for i in range(queue + 1):  
        pygame.draw.line(screen, Dividingline_color,
                         (0, i * (size + Dividingline_width) + Difference),
                         (screen_height, i * (size + Dividingline_width) + Difference),
                         Dividingline_width)

    for j in range(queue + 1):  
        pygame.draw.line(screen, Dividingline_color,
                         (Dividingline_width_half + j * (size + Dividingline_width), Difference),
                         (Dividingline_width_half + j * (size + Dividingline_width), screen_height),
                         Dividingline_width)



def _draw_score(screen, font, pos_x, pos_y):
    global score
    print_text(screen, font, pos_x, 10, f'得分')
    print_text(screen, font, pos_x, pos_y + 6, f'{score}')



def print_text(screen, font, x, y, text):
    imgText = font.render(text, True, score_color)
    screen.blit(imgText, (x, y))


def _game_list():
    for i in range(queue): 
        lis = []
        for j in range(queue):
            lis.append(0)
        game_lis.append(lis)



def _show_game(screen):
    for i in range(queue):
        for j in range(queue):
            rect_color = colors[game_lis[i][j]]  
            rect_position = [(j + 1) * Dividingline_width + j * size, 
                             Dividingline_width * (i + 2) + size * i + score_height]
            pygame.draw.rect(screen, rect_color, (rect_position, (size, size)), 0)  

            if game_lis[i][j] != 0:  
                textSurfaceObj = font3.render(str(game_lis[i][j]), True, black)
                textRectObj = textSurfaceObj.get_rect()
                rect_position = [(j + 1) * Dividingline_width + (j + 0.5) * size,  
                                 Dividingline_width * (i + 2) + size * (i + 0.5) + score_height]
                textRectObj.center = tuple(rect_position)
                screen.blit(textSurfaceObj, textRectObj)



def _random():
    random_num = 5  
    num = pow(2, random_num)
    random_pos_x = random.randint(0, queue - 1)  
    random_pos_y = random.randint(0, queue - 1)  
    if game_lis[random_pos_x][random_pos_y] == 0:
        game_lis[random_pos_x][random_pos_y] = num
    else:
        _random()



def _LEFT():
    global score
    for i in range(queue):
        while 0 in game_lis[i]:
            game_lis[i].remove(0)
        for j in range(len(game_lis[i]) - 1):
            if game_lis[i][j] == game_lis[i][j + 1]:
                game_lis[i][j] = game_lis[i][j] + game_lis[i][j + 1]
                score = score + game_lis[i][j]
                game_lis[i][j + 1] = 0
        while 0 in game_lis[i]:
            game_lis[i].remove(0)
        lis = []
        for j in range(queue - len(game_lis[i])):
            lis.append(0)
        game_lis[i] = game_lis[i] + lis


def _RIGHT():
    global score
    for i in range(queue):
        while 0 in game_lis[i]:
            game_lis[i].remove(0)
        for j in range(len(game_lis[i]) - 1, 0, -1):
            if game_lis[i][j] == game_lis[i][j - 1]:
                game_lis[i][j] = game_lis[i][j] + game_lis[i][j - 1]
                score = score + game_lis[i][j]
                game_lis[i][j - 1] = 0
        while 0 in game_lis[i]:
            game_lis[i].remove(0)
        lis = []
        for j in range(queue - len(game_lis[i])):
            lis.append(0)
        game_lis[i] = lis + game_lis[i]



def _UP():
    global score
    lis = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for i in range(queue):  
        for j in range(queue):
            lis[i][j] = game_lis[queue - 1 - j][i]

    for i in range(queue):
        while 0 in lis[i]:
            lis[i].remove(0)
        for j in range(len(lis[i]) - 1, 0, -1):
            if lis[i][j] == lis[i][j - 1]:
                lis[i][j] = lis[i][j] + lis[i][j - 1]
                score = score + lis[i][j]
                lis[i][j - 1] = 0
        while 0 in lis[i]:
            lis[i].remove(0)
        list1 = []
        for j in range(queue - len(lis[i])):
            list1.append(0)
        lis[i] = list1 + lis[i]

    for i in range(queue): 
        for j in range(queue):
            game_lis[i][j] = lis[j][queue - 1 - i]



def _DOWN():
    global score
    lis = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    for i in range(queue):  
        for j in range(queue):
            lis[i][j] = game_lis[queue - 1 - j][i]

    for i in range(queue):
        while 0 in lis[i]:
            lis[i].remove(0)
        for j in range(len(lis[i]) - 1):
            if lis[i][j] == lis[i][j + 1]:
                lis[i][j] = lis[i][j] + lis[i][j + 1]
                score = score + lis[i][j]
                lis[i][j + 1] = 0
        while 0 in lis[i]:
            lis[i].remove(0)
        list1 = []
        for j in range(queue - len(lis[i])):
            list1.append(0)
        lis[i] = lis[i] + list1

    for i in range(queue):  
        for j in range(queue):
            game_lis[i][j] = lis[j][queue - 1 - i]



def main():
    screen = pygame.display.set_mode((screen_width, screen_height))  
    pygame.display.set_caption('2048')  

    _draw_background(screen)  
    _game_list()
    _show_game(screen)  
    _draw_score(screen, font1, font_pos_x, font_pos_y)


    _random()  
    pygame.display.flip()  
    _show_game(screen) 
    _draw_score(screen, font1, font_pos_x, font_pos_y)  


    while True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:  
                pygame.quit()
                sys.exit()  

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: 
                    _LEFT()
                elif event.key == pygame.K_RIGHT: 
                    _RIGHT()
                elif event.key == pygame.K_UP:  
                    _UP()
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s: 
                    _DOWN()
                else:
                    _DOWN()
                pygame.display.flip()  
                _draw_background(screen)  
                _random() 
                _show_game(screen) 
                _draw_score(screen, font1, font_pos_x, font_pos_y)  


if __name__ == '__main__':
    main()

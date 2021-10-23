import pygame,subprocess
import sys
import pygame.freetype
import time
outputfile_activation_trains = "./data/activation_trains.txt"
activation_trains_write = open(outputfile_activation_trains, mode='w', encoding='latin_1')
activation_trains_write.write(str(True))
activation_trains_write.close()
import Create_string
import Creat_trains
import Calculation
import math
from Create_string import stations, score_stations, score_clock
from importlib import reload
from pygame import gfxdraw
from  PIL import Image


inputfile_activation_trains = "./data/activation_trains.txt"
activation_trains = str(open(inputfile_activation_trains, mode = 'r', encoding = 'latin_1').read().splitlines()[0])

#input = <insert input>
#process = subprocess.Popen(["python","<popup filename>"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=False)
#output = process.communicate(input)[0]

pygame.init()
black = [0, 0 ,0]
white = [255, 255, 255]
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
grey =[128, 128, 128]
maroon = [128, 0, 0]
unvis = [255, 0, 255]
olive = [128, 128, 0]
inputfile_display = "./data/display_x.txt"
max_x = int(str(open(inputfile_display, mode = 'r', encoding = 'latin_1').read().splitlines()[0]))
inputfile_display = "./data/display_y.txt"
max_y = int(str(open(inputfile_display, mode = 'r', encoding = 'latin_1').read().splitlines()[0]))
#max_x = 1500
#max_y = 750
kf_screen_v = max_y/1080
kf_screen_g = max_x/1920
kf_screen_g_2 = (max_x-450)/(1920-450)
screen = pygame.display.set_mode((max_x, max_y), pygame.FULLSCREEN)
#screen = pygame.display.set_mode((max_x, max_y), pygame.RESIZABLE) #RESIZABLE - функция для возможности изменения размеров окна
pygame.display.set_caption("Clever_shedule")

GAME_FONT = pygame.freetype.SysFont("Tahoma", 22)
FONT_trains = pygame.freetype.SysFont("Tahoma", 16)
FONT_tabl_1 = pygame.freetype.SysFont("Tahoma", 18)
FONT_tabl_2 = pygame.freetype.SysFont("Tahoma", 10)
FONT_trains_numbers = pygame.freetype.SysFont("Tahoma", 70)
FONT_grid = pygame.freetype.SysFont("Tahoma", 70)
#screen.fill(white)

def func_screen ():
    pygame.init()
    screen_1 = pygame.display.set_mode((200, 200), pygame.RESIZABLE)
    pygame.display.set_caption("Крутая игра")
z = 1
activation_F = False
activation_R = False

use_draw_stringsP = False
use_draw_stringsG = False

kf_1 = 4 * 6 / score_clock
print("kf_1 =", int(kf_1))
kf_2 = 200
kf_3 = 100/kf_screen_g_2
x = 1
timesP_1 = []
gorizontal = []
vertycal = [150, 300, 450, 600, 750]
#print("trains = ", trains)
def k_screen_vertycal(t):
    for u in range (0, len(t), 1):
        t[u] = int(t[u]) * kf_screen_v
    #print("vert = ", t)
def k_screen_gorizontal(t):
    for u in range(0, len(t), 1):
        t[u] = int(t[u]) * kf_screen_g_2
    #print("vert = ", t)
def k_screen_trains(t):
    for u in range (1, len(t), 4):
        t[u] = int(t[u]) * kf_screen_g_2
    #print("vert_tra = ", t)
k_screen_vertycal(vertycal)
k_screen_vertycal(stations)


for u in range(0, score_clock + 1, 1 ):
    gorizontal.append(kf_3)
    kf_3 += kf_1 * 60
k_screen_gorizontal(gorizontal)
gorizontal_tab = [5, 5+70, 5+115, 5+180, 5+245, 5+330]
#gorizontal_tab_calc = [0, gorizontal[len(gorizontal)-1]-int(1200*kf_screen_g)-200, gorizontal[len(gorizontal)-1]-int(
#    1200*kf_screen_g)-100, gorizontal[len(gorizontal)-1]-int(1200*kf_screen_g)]
gorizontal_tab_calc = [0, 130, 230, 330]
vertycal_tab_calc = [0, 60, 100, 140, 160]
#for u in range (0, len(gorizontal), 1):
#    gorizontal[u] += kf_2

""""Координаты для кнопок. x1G, y1G - ширина и высота кнопки для грузовых. x2G, y2G - координаты верхнего левого угла кнопки """
x_yG = [100, 40, 100, vertycal[4]+80]
x_yP = [100, 40, 220, vertycal[4]+80]
x_yR = [100, 40, 340, vertycal[4]+80]
x_yN = [100, 40, 100, vertycal[4]+140]
x_yAr = [100, 40, 220, vertycal[4]+140]
x_yDep = [100, 40, 340, vertycal[4]+140]
x_ySel = [250, 20, 460, vertycal[4]+80]
x_ySel4 = [250, 3*16, 460, vertycal[4]+80+20]
x_y_act_TF = [120, 40, 730, vertycal[4]+80]
x_y_act_TR = [120, 40, 730, vertycal[4]+140]

"""======================Layers================="""
grid_surf = pygame.Surface((gorizontal[len(gorizontal) - 1]+20, vertycal[4] + 80))
grid_surf.fill(black)

if activation_trains == str(True):
    from Creat_trains import trains
    score_trains = len(trains) // 4
    vertycal_tab = [30]
    for i in range(0, score_trains + 1, 1):
        vertycal_tab.append(70 + i * 20)
    #tabl_surf = pygame.Surface((gorizontal_tab[len(gorizontal_tab) - 1] + 10, vertycal_tab[len(vertycal_tab) - 1] + 80))
    tabl_surf = pygame.Surface((gorizontal_tab[len(gorizontal_tab) - 1] + 10, int(max_y*600/760) - 120))
    tabl_surf.fill(black)
elif activation_trains == str(False):
    from input_trains import trains_GID
    trains = trains_GID
    score_trains = len(trains) // 4
    vertycal_tab = [30]
    for i in range(0, score_trains + 1, 1):
        vertycal_tab.append(70 + i * 20)
    #tabl_surf = pygame.Surface((gorizontal_tab[len(gorizontal_tab) - 1] + 10, vertycal_tab[len(vertycal_tab) - 1] + 80))
    tabl_surf = pygame.Surface((gorizontal_tab[len(gorizontal_tab) - 1] + 10, int(max_y * 600 / 760) - 120))
    tabl_surf.fill(black)
else:
    tabl_surf = pygame.Surface((0, 0))
    tabl_surf.fill(black)

buttons_surf = pygame.Surface((max_x, max_y))
buttons_surf.fill(black)
surf = pygame.Surface((gorizontal[len(gorizontal)-1]-gorizontal[0], vertycal[4]- vertycal[0]))
surf.fill(black)
surf.set_colorkey(grey)
surf_trains = pygame.Surface((gorizontal[len(gorizontal)-1]-gorizontal[0]+10, vertycal[4]- vertycal[0]+190))
surf_trains.fill(black)
surf_trains.set_colorkey(black)
surf_trains_select = pygame.Surface((gorizontal[len(gorizontal)-1]-gorizontal[0]+10, vertycal[4]- vertycal[0]+190))
surf_trains_select.fill(black)
surf_trains_select.set_colorkey(black)
mouse_surf = pygame.Surface((60, 20))
mouse_surf.fill(black)
select_surf = pygame.Surface((gorizontal[len(gorizontal)-1], 20))
select_surf.fill(black)

#surf_tabl_calc = pygame.Surface((gorizontal[len(gorizontal)-1]-int(1200*kf_screen_g)+2, vertycal_tab_calc[len(vertycal_tab_calc)-1]+2))
surf_tabl_calc = pygame.Surface((330+2, vertycal_tab_calc[len(vertycal_tab_calc)-1]+2))
surf_tabl_calc.fill(black)
surf_tabl_calc.set_colorkey(black)
#select_surf.set_colorkey(black)

"""=================Download images=================="""

Red_col1 = pygame.image.load('./images/Red.bmp')
Red_col22 = pygame.image.load('./images/Red2.bmp')
Red_col1.set_colorkey(black)
Red_col = pygame.transform.smoothscale(Red_col1, (4, 4))
Red_col2 = pygame.transform.smoothscale(Red_col22, (1, 1))
arrow1 = pygame.image.load('./images/arrow.jpg')
arrow = pygame.transform.smoothscale(arrow1, (20, 50))
arrow2 = pygame.transform.smoothscale(arrow1, (30, 75))
arrow.set_colorkey(black)

def draw_text (y, color,text):
    global surf_text_image_2
    surf_text_image = pygame.Surface((len(text)*70, 70))
    surf_text_image.fill(black)
    surf_text_image.set_colorkey(black)
    FONT_grid.render_to(surf_text_image, (1, 1), text, color)
    surf_text_image_2 = pygame.transform.smoothscale(surf_text_image, (len(text)*y, y))

def draw_shedule_grid():
    """Draw shedule grid"""
    inputfile_activation_trains = "./data/activation_trains.txt"
    activation_trains = str(open(inputfile_activation_trains, mode='r', encoding='latin_1').read().splitlines()[0])
    if activation_trains == str(True):
        from Creat_trains import trains
    elif activation_trains == str(False):
        from input_trains import trains_GID
        trains = trains_GID
        #print("!!!!!!! = ", len(trains_GID) // 4)
    score_trains = len(trains) // 4
    #print("!!! = ", score_trains)
    vertycal_tab = [30]
    global surf_text_image_2
    for i in range(0, score_trains + 1, 1):
        vertycal_tab.append(70 + i * 20)
    """Draw gorizontal line"""
    for u in range(0, score_clock, 1):
        for u1 in range (0, 5, 1):
            pygame.draw.line(grid_surf, grey, [int(gorizontal[u]), int(vertycal[u1])], [int(gorizontal[u + 1]) , int(vertycal[u1])], 2)
    """Draw text"""
    for u in range(0, score_clock + 1, 1):
        draw_text(20, red, str(u))
        grid_surf.blit(surf_text_image_2, (int(gorizontal[u]), int(vertycal[0])-30))
        #GAME_FONT.render_to(grid_surf, (int(gorizontal[u]), int(vertycal[0])-30), str(u), red)
    for u in range (0, 5, 1):
        draw_text(18, red, "Station " + str(u))
        grid_surf.blit(surf_text_image_2, (15, int(vertycal[u])-10))
        #GAME_FONT.render_to(grid_surf, (15, int(vertycal[u])), "Station" + str(u), red)
    """Draw vertical line"""
    for u in range(0, score_clock + 1, 1):
        for u1 in range (0, 4, 1):
            pygame.draw.line(grid_surf, grey, [int(gorizontal[u]), int(vertycal[u1])], [int(gorizontal[u]) , int(vertycal[u1+1])], 2)

    for u in range(0, score_clock , 1):
        for i in range (1, 6, 1):
            punktir_line(20, 40, int(gorizontal[u])+int(i*((int(gorizontal[1])-int(gorizontal[0])) // 6)),
                         int(vertycal[0]),
                         int(gorizontal[u])+int(i*((int(gorizontal[1])-int(gorizontal[0])) // 6)),
                         int(vertycal[len(vertycal)-1]), grid_surf, grey, 1)

    for u in range(0, score_clock, 1):
        for u1 in range (0, 4, 1):
            pygame.draw.line(grid_surf, grey, [int(gorizontal[u]) + (int(gorizontal[1])-int(gorizontal[0])) // 2, int(vertycal[u1])],
                             [int(gorizontal[u]) + (int(gorizontal[1])-int(gorizontal[0])) // 2, int(vertycal[u1 + 1])], 1)

    """Draw tabl for trains"""
    for u in range(0, len(gorizontal_tab), 1):
        pygame.draw.line(tabl_surf, grey, [int(gorizontal_tab[u]), int(vertycal_tab[0])],
                             [int(gorizontal_tab[u]) , int(vertycal_tab[len(vertycal_tab)-1])], 2)
    for u in range(0, len(vertycal_tab), 1):
        pygame.draw.line(tabl_surf, grey, [int(gorizontal_tab[0]), int(vertycal_tab[u])],
                             [int(gorizontal_tab[len(gorizontal_tab)-1]) , int(vertycal_tab[u])], 2)
    draw_text(18, red, "Список поездов")
    tabl_surf.blit(surf_text_image_2, (5, 5))
    draw_text(12, grey, "№ поезда")
    tabl_surf.blit(surf_text_image_2, (gorizontal_tab[0]+5, vertycal_tab[0]+10 -5))
    draw_text(12, grey, "Масса,")
    tabl_surf.blit(surf_text_image_2, (gorizontal_tab[1] + 5, vertycal_tab[0] + 10 - 5))
    draw_text(12, grey, "т")
    tabl_surf.blit(surf_text_image_2, (gorizontal_tab[1] + 5, vertycal_tab[0] + 30 - 5))
    draw_text(12, grey, "Категория")
    tabl_surf.blit(surf_text_image_2, (gorizontal_tab[2] + 5, vertycal_tab[0] + 10 - 5))
    draw_text(12, grey, "Прибытие")
    tabl_surf.blit(surf_text_image_2, (gorizontal_tab[3] + 5, vertycal_tab[0] + 10 - 5))
    draw_text(12, grey, "поезда")
    tabl_surf.blit(surf_text_image_2, (gorizontal_tab[3] + 5, vertycal_tab[0] + 30 - 5))
    draw_text(12, grey, "Отправление")
    tabl_surf.blit(surf_text_image_2, (gorizontal_tab[4] + 5, vertycal_tab[0] + 10 - 5))
    draw_text(12, grey, "поезда")
    tabl_surf.blit(surf_text_image_2, (gorizontal_tab[4] + 5, vertycal_tab[0] + 30 - 5))

    #FONT_tabl_1.render_to(tabl_surf, (5, 5), "Список поездов", red)
    #FONT_tabl_2.render_to(tabl_surf, (gorizontal_tab[0]+5, vertycal_tab[0]+10 -5), "№ поезда", grey)
    #FONT_tabl_2.render_to(tabl_surf, (gorizontal_tab[1] + 5, vertycal_tab[0] + 10 - 5), "Масса,", grey)
    #FONT_tabl_2.render_to(tabl_surf, (gorizontal_tab[1] + 5, vertycal_tab[0] + 30 - 5), "т", grey)
    #FONT_tabl_2.render_to(tabl_surf, (gorizontal_tab[2] + 5, vertycal_tab[0] + 10 - 5), "Категория", grey)
    #FONT_tabl_2.render_to(tabl_surf, (gorizontal_tab[3] + 5, vertycal_tab[0] + 10 - 5), "Прибытие", grey)
    #FONT_tabl_2.render_to(tabl_surf, (gorizontal_tab[3] + 5, vertycal_tab[0] + 30 - 5), "поезда", grey)
    #FONT_tabl_2.render_to(tabl_surf, (gorizontal_tab[4] + 5, vertycal_tab[0] + 10 - 5), "Отправление", grey)
    #FONT_tabl_2.render_to(tabl_surf, (gorizontal_tab[4] + 5, vertycal_tab[0] + 30 - 5), "поезда", grey)

    """Draw tabl for calculations results"""
    for u in range (0, len(vertycal_tab_calc), 1):
        pygame.draw.line(surf_tabl_calc, grey, [gorizontal_tab_calc[0], vertycal_tab_calc[u]],
                         [gorizontal_tab_calc[len(gorizontal_tab_calc)-1], vertycal_tab_calc[u]], 2)
    for u in range (0, len(gorizontal_tab_calc), 1):
        pygame.draw.line(surf_tabl_calc, grey, [gorizontal_tab_calc[u], vertycal_tab_calc[0]],
                         [gorizontal_tab_calc[u], vertycal_tab_calc[len(vertycal_tab_calc)-1]], 2)

    draw_text(12, grey, "Расходы до")
    surf_tabl_calc.blit(surf_text_image_2, (gorizontal_tab_calc[1] + 5, vertycal_tab_calc[0] + 10 - 5))
    draw_text(12, grey, "использования")
    surf_tabl_calc.blit(surf_text_image_2, (gorizontal_tab_calc[1] + 5, vertycal_tab_calc[0] + 30 - 5))
    draw_text(12, grey, "технологии")
    surf_tabl_calc.blit(surf_text_image_2, (gorizontal_tab_calc[1] + 5, vertycal_tab_calc[0] + 50 - 5))
    draw_text(12, grey, "Расходы после")
    surf_tabl_calc.blit(surf_text_image_2, (gorizontal_tab_calc[2] + 5, vertycal_tab_calc[0] + 10 - 5))
    draw_text(12, grey, "использования")
    surf_tabl_calc.blit(surf_text_image_2, (gorizontal_tab_calc[2] + 5, vertycal_tab_calc[0] + 30 - 5))
    draw_text(12, grey, "технологии")
    surf_tabl_calc.blit(surf_text_image_2, (gorizontal_tab_calc[2] + 5, vertycal_tab_calc[0] + 50 - 5))
    draw_text(12, grey, "От стянок на")
    surf_tabl_calc.blit(surf_text_image_2, (gorizontal_tab_calc[0] + 5, vertycal_tab_calc[1] + 10 - 5))
    draw_text(12, grey, "пром. станциях")
    surf_tabl_calc.blit(surf_text_image_2, (gorizontal_tab_calc[0] + 5, vertycal_tab_calc[1] + 30 - 5))
    draw_text(12, grey, "От стянок на")
    surf_tabl_calc.blit(surf_text_image_2, (gorizontal_tab_calc[0] + 5, vertycal_tab_calc[2] + 10 - 5))
    draw_text(12, grey, "тех. станции")
    surf_tabl_calc.blit(surf_text_image_2, (gorizontal_tab_calc[0] + 5, vertycal_tab_calc[2] + 30 - 5))
    draw_text(12, grey, "Итого:")
    surf_tabl_calc.blit(surf_text_image_2, (gorizontal_tab_calc[0] + 5, vertycal_tab_calc[3] + 10 - 5))

    #FONT_tabl_2.render_to(surf_tabl_calc, (gorizontal_tab_calc[1] + 5, vertycal_tab_calc[0] + 10 - 5), "Расходы до", grey)
    #FONT_tabl_2.render_to(surf_tabl_calc, (gorizontal_tab_calc[1] + 5, vertycal_tab_calc[0] + 30 - 5), "использования", grey)
    #FONT_tabl_2.render_to(surf_tabl_calc, (gorizontal_tab_calc[1] + 5, vertycal_tab_calc[0] + 50 - 5), "технологии",
    #                    grey)
    #FONT_tabl_2.render_to(surf_tabl_calc, (gorizontal_tab_calc[2] + 5, vertycal_tab_calc[0] + 10 - 5), "Расходы после", grey)
    #FONT_tabl_2.render_to(surf_tabl_calc, (gorizontal_tab_calc[2] + 5, vertycal_tab_calc[0] + 30 - 5), "использования",
    #                    grey)
    #FONT_tabl_2.render_to(surf_tabl_calc, (gorizontal_tab_calc[2] + 5, vertycal_tab_calc[0] + 50 - 5), "технологии",
    #                   grey)
    #FONT_tabl_2.render_to(surf_tabl_calc, (gorizontal_tab_calc[0] + 5, vertycal_tab_calc[1] + 10 - 5), "От стянок на", grey)
    #FONT_tabl_2.render_to(surf_tabl_calc, (gorizontal_tab_calc[0] + 5, vertycal_tab_calc[1] + 30 - 5), "пром. станциях",
    #                      grey)
    #FONT_tabl_2.render_to(surf_tabl_calc, (gorizontal_tab_calc[0] + 5, vertycal_tab_calc[2] + 10 - 5), "От стянок на",
    #                      grey)
    #FONT_tabl_2.render_to(surf_tabl_calc, (gorizontal_tab_calc[0] + 5, vertycal_tab_calc[2] + 30 - 5), "тех. станции",
    #                      grey)
    #FONT_tabl_2.render_to(surf_tabl_calc, (gorizontal_tab_calc[0] + 5, vertycal_tab_calc[3] + 10 - 5), "Итого:",
    #                      grey)

def draw_stringsP():
    from Create_string import timesP, score_P_trains
    global use_draw_stringsP
    if use_draw_stringsP == False:
        k_screen_gorizontal(timesP)
    """Draw passangers strings"""
    for y in range (0, score_P_trains, 1):
        for i in range (1, (score_stations * 2) - 1, 2):
            S_0 = 125 * 35
            S_1 = (float(timesP[i + 1 + (y * 10)]) - float(timesP[i + (y * 10)])) * (stations[2] - stations[1])
            #print("S_1 = ", S_1, (timesP[i + 1 + (y * 10)] - timesP[i + (y * 10)]))
            #print("S// = ", S_1 / S_0)
            img = Image.open('./images/line_3.jpg')
            area = (0, 0, 557*(S_1/S_0)**0.5, 532*(S_1/S_0)**0.5-10)
            cropped_img = img.crop(area)
            cropped_img.save('./images/line_00.jpg')
            line_1 = pygame.image.load('./images/line_00.jpg')

            line = pygame.transform.smoothscale(line_1, (int((int(timesP[i + 1 + (y*10)])-int(timesP[i+(y*10)]))*kf_1)+5, int(stations[2]-stations[1])))
            line.set_colorkey(black)
            surf.blit(line, (int(int(timesP[i+(y*10)]) * kf_1) , int(stations[i]-stations[0])))

            #pygame.draw.line(surf, red, [int((timesP[i+(y*10)]) * kf_1) , int(stations[i]-stations[0])],
            #                 [int((timesP[i + 1 + (y*10)]) * kf_1), int(stations[i+1]-stations[0])], 5)

            #pygame.gfxdraw.line(surf, int((timesP[i + (y * 10)]) * kf_1), int(stations[i] - stations[0]),
            #                 int((timesP[i + 1 + (y * 10)]) * kf_1), int(stations[i + 1] - stations[0]), red)
    use_draw_stringsP = True

def punktir_line(l1, l2, x1, y1, x2, y2, Surface, color, tickness):

    l = ((x2-x1)**2 + (y2-y1)**2)**0.5
    kl2 = l/(l1+l2)
    kl1 = l1/(l1+l2)
    xl2 = x1+(x2-x1)/kl2
    yl2 = y1+(y2-y1)/kl2
    xl1 = x1+(xl2-x1)*kl1
    yl1 = y1+(yl2-y1)*kl1
    x1_y1 = [x1, y1]
    x2_y2 =[]
    for i in range(1, int(kl2)+1, 1):
        x2_y = x1+(xl2-x1)*i
        x1_y = x2_y - (xl2-xl1)
        x_y2 = y1+(yl2-y1) * i
        x_y1 = x_y2 - (yl2 - yl1)
        x2_y2.append(x1_y)
        x2_y2.append(x_y1)
        x2_y2.append(x2_y)
        x2_y2.append(x_y2)
        x1_y1.append(x1_y)
        x1_y1.append(x_y1)
        #if i < int(kl2):
        x1_y1.append(x2_y)
        x1_y1.append(x_y2)
        if i == int(kl2):
            if l-(int(kl2)*(l1+l2)) >= l1:
                x1_y1.append(x2_y + (x1_y1[2]-x1_y1[0]))
                x1_y1.append(x_y2 + (x1_y1[3] - x1_y1[1]))
                x2_y2.append(x2_y + (x1_y1[2] - x1_y1[0]))
                x2_y2.append(x_y2 + (x1_y1[3] - x1_y1[1]))
                x2_y2.append(x2)
                x2_y2.append(y2)
            elif l-(int(kl2)*(l1+l2)) < l1:
                x1_y1.append(x2)
                x1_y1.append(y2)

        else:
            continue
    #print("x1_y1 = ", x1_y1, len(x1_y1))
    #print("x2_y2 = ", x2_y2, len(x2_y2))
    for i in range (0, len(x1_y1), 4):
        pygame.draw.line(Surface, color, (int(x1_y1[i]), int(x1_y1[i+1])), (int(x1_y1[i+2]), int(x1_y1[i+3])), tickness)
    for i in range (0, len(x2_y2), 4):
        pygame.draw.line(Surface, black, (int(x2_y2[i]), int(x2_y2[i+1])), (int(x2_y2[i+2]), int(x2_y2[i+3])), tickness)
    #screen.blit(Surface, (0, 0))

def draw_stringsG():
    from Create_string import times_strings, good_strings
    global use_draw_stringsG
    global times_strings_0
    if use_draw_stringsG == False:
        times_strings_0 = times_strings.copy()
        k_screen_gorizontal(times_strings)
    """Draw freight strings"""
    h = len(times_strings) // len(stations)
    stationss = []
    for j in range (1, h+1, 1):
        stationss.extend(stations)
        #print(stationsx)
    for x in range (1, len(times_strings)-1, 2):
        #print("GOOD_STRING = ", good_strings)
        #print("TIME_STRINGS = ", times_strings)
        if good_strings[(x)//10] == 0:
            if (x-9)%10 == 0:
                continue
            else:
                #pygame.draw.line(surf, olive, [(int(times_strings[x]) * kf_1)+kf_2, int(stationss[x])],
                #            [(int(times_strings[x + 1]) * kf_1)+kf_2, int(stationss[x + 1])], 5)
                #punktir_line(20, 20, (int(times_strings[x]) * kf_1), int(stationss[x]-stationss[0]),
                #             (int(times_strings[x + 1]) * kf_1), int(stationss[x + 1]-stationss[0]), surf)
                pygame.draw.line(surf, green, [(int(times_strings[x]) * kf_1), int(stationss[x] - stationss[0])],
                                 [(int(times_strings[x + 1]) * kf_1), int(stationss[x + 1] - stationss[0])], 2)
        else:
            if (x-9)%10 == 0 or (x-10)%10 == 0:
                continue
            else:
                pygame.draw.line(surf, green, [(int(times_strings[x]) * kf_1), int(stationss[x]-stationss[0])],
                            [(int(times_strings[x + 1]) * kf_1), int(stationss[x + 1]-stationss[0])], 2)
    use_draw_stringsG = True

def draw_uneconomic_string():
    from Create_string import times_strings, good_strings, score_ost
    from Calculation import trains_for_strings_F, trains_for_strings_0
    global use_draw_stringsG
    global times_strings_0
    global score_ost
    if use_draw_stringsG == False:
        times_strings_0 = times_strings.copy()
        k_screen_gorizontal(times_strings)
    use_draw_stringsG = True
    if activation_calc == False:
        # trains_for_string = trains_for_string_0
        trains_for_string = trains_for_strings_0
    else:
        # trains_for_string = trains_for_string
        trains_for_string = trains_for_strings_F
    h = len(times_strings) // len(stations)
    stationss = []
    for j in range(1, h + 1, 1):
        stationss.extend(stations)
        # print(stationsx)
    for y in range (0, len(score_ost), 1):
        if score_ost[y] != 0:
            #for y in range (0, len(trains_for_string), 1):
            if trains_for_string[y] == 1:
                for x in range(1, 8, 2):
                    punktir_line(20, 20, (int(times_strings[y * 10 + x]) * kf_1), int(stationss[x] - stationss[0]),
                                 (int(times_strings[y * 10 + x + 1]) * kf_1), int(stationss[x + 1] - stationss[0]),
                                 surf, green, 2)
            else:
                for x in range(1, 8, 2):
                    pygame.draw.line(surf, green,
                                     [(int(times_strings[y * 10 + x]) * kf_1), int(stationss[x] - stationss[0])],
                                     [(int(times_strings[y * 10 + x + 1]) * kf_1),
                                      int(stationss[x + 1] - stationss[0])], 2)

        else:
            for x in range(1, 8, 2):
                pygame.draw.line(surf, green,
                                 [(int(times_strings[y * 10 + x]) * kf_1), int(stationss[x] - stationss[0])],
                                 [(int(times_strings[y * 10 + x + 1]) * kf_1), int(stationss[x + 1] - stationss[0])], 2)

def draw_trains_arrivals():
    inputfile_activation_trains = "./data/activation_trains.txt"
    activation_trains = str(open(inputfile_activation_trains, mode='r', encoding='latin_1').read().splitlines()[0])
    if activation_trains == str(True):
        from Creat_trains import trains
    elif activation_trains == str(False):
        from input_trains import trains_GID
        trains = trains_GID
    trains_d = trains.copy()
    k_screen_trains(trains_d)
    score_trains = len(trains) // 4
    vertycal_tab = [30]
    for i in range(0, score_trains + 1, 1):
        vertycal_tab.append(70 + i * 20)
    """Draw trains arrivals"""
    score_trains = len(trains) // 4
    print("score_trains=", trains)
    for u in range(1, len(trains), 4):
        text = " N " + str(trains[u+2])
        #surf_text = pygame.Surface((65, 25))
        #surf_text.fill(black)
        #surf_text.set_colorkey(black)
        surf_text_image = pygame.Surface((250, 65))
        surf_text_image.fill(black)
        surf_text_image.set_colorkey(black)

        surf_trains.blit(arrow, (int(int(trains_d[u])*kf_1)-20, int(vertycal[0]-vertycal[0])+40))
        #FONT_trains.render_to(surf_text, (1, 1), text, grey)
        FONT_trains_numbers.render_to(surf_text_image, (1, 1), text, grey)
        surf_text_image = pygame.transform.rotate(surf_text_image, 290)
        #pygame.image.save(surf_text_image, './images/numbers.png')
        surf_text_image_0 = pygame.transform.smoothscale(surf_text_image, (36, 52))
        #surf_text = pygame.transform.rotate(surf_text, 290)
        #surf_trains.blit(surf_text, (int(int(trains_d[u])*kf_1)-35, int(vertycal[0] - vertycal[0])-5))
        surf_trains.blit(surf_text_image_0, (int(int(trains_d[u]) * kf_1) - 30, int(vertycal[0] - vertycal[0]) - -5))

    for i in range (0, score_trains, 1):
        if int(trains[i * 4 + 1]-60*(trains[i * 4 + 1]//60))//10 == 0:
            time_arr = '0'+str(int(trains[i * 4 + 1]-60*(trains[i * 4 + 1]//60)))
        else:
            time_arr = str(int(trains[i * 4 + 1] - 60 * (trains[i * 4 + 1] // 60)))

        draw_text(12, grey, str(trains[i*4+3]))
        tabl_surf.blit(surf_text_image_2, (gorizontal_tab[0] + 5, vertycal_tab[i + 1] + 10 - 5))
        draw_text(12, grey, str(trains[i * 4 + 0]))
        tabl_surf.blit(surf_text_image_2, (gorizontal_tab[1] + 5, vertycal_tab[i + 1] + 10 - 5))
        draw_text(12, grey, str(trains[i * 4 + 2]))
        tabl_surf.blit(surf_text_image_2, (gorizontal_tab[2] + 5, vertycal_tab[i + 1] + 10 - 5))
        draw_text(12, grey, (str(int(trains[i * 4 + 1]//60)) + ':' + time_arr))
        tabl_surf.blit(surf_text_image_2, (gorizontal_tab[3] + 5, vertycal_tab[i + 1] + 10 - 5))

        #FONT_tabl_2.render_to(tabl_surf, (gorizontal_tab[0] + 5, vertycal_tab[i + 1] + 10 - 5), str(trains[i*4+3]), grey)
        #FONT_tabl_2.render_to(tabl_surf, (gorizontal_tab[1] + 5, vertycal_tab[i + 1] + 10 - 5), str(trains[i * 4 + 0]), grey)
        #FONT_tabl_2.render_to(tabl_surf, (gorizontal_tab[2] + 5, vertycal_tab[i + 1] + 10 - 5), str(trains[i * 4 + 2]), grey)
        #FONT_tabl_2.render_to(tabl_surf, (gorizontal_tab[3] + 5, vertycal_tab[i + 1] + 10 - 5),
                              #(str(int(trains[i * 4 + 1]//60)) + ':' + time_arr), grey)

def output_calculation_results():
    from Calculation import P_Finally1
    for u in range (0, 3, 1):
        draw_text(15, grey, str(int(P_Finally1[u]))+" р.")
        surf_tabl_calc.blit(surf_text_image_2, (gorizontal_tab_calc[1] + 10, vertycal_tab_calc[u+1] + (
            vertycal_tab_calc[u+2]-vertycal_tab_calc[u+1])//2 - 5))
        #FONT_tabl_2.render_to(surf_tabl_calc, (gorizontal_tab_calc[1] + 10, vertycal_tab_calc[u+1] + (
        #    vertycal_tab_calc[u+2]-vertycal_tab_calc[u+1])//2 - 5), str(int(P_Finally1[u]))+" р.", grey)
    for u in range (0, 3, 1):
        draw_text(15, grey, str(int(P_Finally1[u+3])) + " р.")
        surf_tabl_calc.blit(surf_text_image_2, (gorizontal_tab_calc[2] + 10, vertycal_tab_calc[u + 1] + (
            vertycal_tab_calc[u + 2] - vertycal_tab_calc[u + 1]) // 2 - 5))
        #FONT_tabl_2.render_to(surf_tabl_calc, (gorizontal_tab_calc[2] + 10, vertycal_tab_calc[u + 1] + (
        #    vertycal_tab_calc[u + 2] - vertycal_tab_calc[u + 1]) // 2 - 5), str(int(P_Finally1[u+3])) + " р.", grey)

def draw_trains_departures():
    inputfile_activation_trains = "./data/activation_trains.txt"
    activation_trains = str(open(inputfile_activation_trains, mode='r', encoding='latin_1').read().splitlines()[0])
    if activation_trains == str(True):
        from Creat_trains import trains
    elif activation_trains == str(False):
        from input_trains import trains_GID
        trains = trains_GID
    from Create_string import times_strings #trains_for_string, , trains_for_string_0
    from Calculation import trains_for_strings_F, trains_for_strings_0
    if activation_calc == False:
        #trains_for_string = trains_for_string_0
        trains_for_string = trains_for_strings_0
    else:
        #trains_for_string = trains_for_string
        trains_for_string = trains_for_strings_F

    global use_draw_stringsG
    global times_strings_0
    if use_draw_stringsG == False:
        times_strings_0 = times_strings.copy()
        k_screen_gorizontal(times_strings)
    use_draw_stringsG = True
    trains_d = trains.copy()
    k_screen_trains(trains_d)
    score_trains = len(trains) // 4
    vertycal_tab = [30]
    for i in range(0, score_trains + 1, 1):
        vertycal_tab.append(70 + i * 20)
    """Draw trains for strings"""
    score_trains = len(trains) // 4
    for u in range(0, len(trains_for_string), 1):
        if trains_for_string[u] != 0 and trains_for_string[u] != 1:

            text = " N " + str(trains_for_string[u])
            #surf_text = pygame.Surface((65, 25))
            #surf_text.fill(black)
            #surf_text.set_colorkey(black)
            surf_text_image = pygame.Surface((250, 65))
            surf_text_image.fill(black)
            surf_text_image.set_colorkey(black)
            surf_trains.blit(arrow, (int(int(times_strings[u*10+8]) * kf_1), int(vertycal[4] - vertycal[0]) + 90))
            pygame.draw.circle(surf_trains, grey, (int((int(times_strings[u*10+8])) * kf_1), int(vertycal[4]-vertycal[0])+90), 4, 2)
            #FONT_trains.render_to(surf_text, (1, 1), text, grey)
            FONT_trains_numbers.render_to(surf_text_image, (1, 1), text, grey)
            surf_text_image = pygame.transform.rotate(surf_text_image, 290)
            #pygame.image.save(surf_text_image, './images/numbers.png')
            surf_text_image_3 = pygame.transform.smoothscale(surf_text_image, (36, 52))
            #surf_text = pygame.transform.rotate(surf_text, 290)
            #surf_trains.blit(surf_text, (int(int(times_strings[u*10+8]) * kf_1)-25, int(vertycal[4]-vertycal[0]) + 100))
            surf_trains.blit(surf_text_image_3,
                             (int(int(times_strings[u*10+8]) * kf_1)-20, int(vertycal[4]-vertycal[0]) + 100))
            for i in range (0, score_trains, 1):
                if int(float(times_strings_0[u*10+1]) - 60 * (float(times_strings_0[u*10+1]) // 60)) // 10 == 0:
                    time_arr = '0' + str(int(float(times_strings_0[u*10+1]) - 60 * (float(times_strings_0[u*10+1]) // 60)))
                else:
                    time_arr = str(int(float(times_strings_0[u*10+1]) - 60 * (float(times_strings_0[u*10+1]) // 60)))
                if trains_for_string[u] == trains[i*4+3]:
                    draw_text(12, grey, (str(int(float(times_strings_0[u*10+1]) // 60)) + ':' + time_arr))
                    tabl_surf.blit(surf_text_image_2, (gorizontal_tab[4] + 5, vertycal_tab[i + 1] + 10 - 5))
                    #FONT_tabl_2.render_to(tabl_surf, (gorizontal_tab[4] + 5, vertycal_tab[i + 1] + 10 - 5),
                                        #(str(int(float(times_strings_0[u*10+8]) // 60)) + ':' + time_arr), grey)
                else:
                    continue
        else:
            continue

def draw_buttons():
    Button_P.show_button_pos_1()
    Button_G.show_button_pos_1()
    Button_N.show_button_pos_1()
    Button_Ar.show_button_pos_1()
    Button_Dep.show_button_pos_1()
    Button_R.show_button_pos_1()
    Button_Score_P.show_button_pos_1()
    if activation_F == False:
        Button_act_TF.show_button_checkbox_pos_1()
    else:
        Button_act_TF.show_button_checkbox_pos_1_3()
    if activation_R == False:
        Button_act_TR.show_button_checkbox_pos_1()
    else:
        Button_act_TR.show_button_checkbox_pos_1_3()

class Button ():
    def __init__(self, Name, size, text_size_k):
        self.Name = Name
        self.text_size = 12
        self.size = size
        self.text_size_k = text_size_k

    def show_button_pos_1(self):
        button_surf = pygame.Surface((self.size[0], self.size[1]))
        button_surf.fill(black)
        len_text = len(self.Name)
        if self.text_size_k == 0:
            self.text_size = 14
            Button_icon_1 = pygame.image.load('./images/Button_pos_1.jpg')
        elif self.text_size_k == 1:
            self.text_size = 12
            Button_icon_1 = pygame.image.load('./images/Button_select_pos_1.jpg')
        Button_icon = pygame.transform.scale(Button_icon_1, (self.size[0], self.size[1]))
        button_surf.blit(Button_icon, (0, 0))
        text_surf = pygame.freetype.SysFont("Tahoma", self.text_size)
        text_surf.render_to(button_surf, (int((self.size[0] / 2) - (self.text_size - self.text_size / 2) * (len_text / 2)),
                                          (self.size[1] // 2) - (self.text_size // 2)), self.Name, black)
        buttons_surf.blit(button_surf, (self.size[2], self.size[3]))
        pygame.display.update()

    def show_button_pos_2(self):
        button_surf = pygame.Surface((self.size[0], self.size[1]))
        button_surf.fill(black)
        len_text = len(self.Name)
        if self.text_size_k == 0:
            self.text_size = 14
            Button_icon_1 = pygame.image.load('./images/Button_pos_2.jpg')
        elif self.text_size_k == 1:
            self.text_size = 12
            Button_icon_1 = pygame.image.load('./images/Button_select_pos_2.jpg')
        Button_icon = pygame.transform.scale(Button_icon_1, (self.size[0], self.size[1]))
        button_surf.blit(Button_icon, (0, 0))
        text_surf = pygame.freetype.SysFont("Tahoma", self.text_size)
        text_surf.render_to(button_surf, (int((self.size[0] / 2) - (self.text_size - self.text_size / 2) * (len_text / 2)),
                                          (self.size[1] // 2) - (self.text_size // 2)), self.Name, black)
        buttons_surf.blit(button_surf, (self.size[2], self.size[3]))
        pygame.display.update()

    def show_button_pos_3(self):
        button_surf = pygame.Surface((self.size[0], self.size[1]))
        button_surf.fill(black)
        len_text = len(self.Name)
        if self.text_size_k == 0:
            self.text_size = 13
            Button_icon_1 = pygame.image.load('./images/Button_pos_3.jpg')
        elif self.text_size_k == 1:
            self.text_size = 11
            Button_icon_1 = pygame.image.load('./images/Button_select_pos_3.jpg')
        Button_icon = pygame.transform.scale(Button_icon_1, (self.size[0], self.size[1]))
        button_surf.blit(Button_icon, (0, 0))
        text_surf = pygame.freetype.SysFont("Tahoma", self.text_size)
        text_surf.render_to(button_surf, (int((self.size[0] / 2) - (self.text_size - self.text_size / 2) * (len_text / 2)),
                                          (self.size[1] // 2) - (self.text_size // 2)), self.Name, black)
        buttons_surf.blit(button_surf, (self.size[2], self.size[3]))
        pygame.display.update()

    def show_button_select(self):
        button_surf = pygame.Surface((self.size[0], self.size[1]))
        button_surf.fill(black)
        self.text_size = 12
        Button_icon_1 = pygame.image.load('./images/Button_select_pos_4.jpg')
        Button_icon = pygame.transform.scale(Button_icon_1, (self.size[0], self.size[1]))
        button_surf.blit(Button_icon, (0, 0))
        text_surf = pygame.freetype.SysFont("Tahoma", self.text_size)
        text_surf.render_to(button_surf, (20, (16 // 2) - (self.text_size // 2)), str(self.Name[0]), black)
        text_surf.render_to(button_surf, (20, 16 + (16 // 2) - (self.text_size // 2)), str(self.Name[1]), black)
        text_surf.render_to(button_surf, (20, 32 + (16 // 2) - (self.text_size // 2)), str(self.Name[2]), black)
        text_surf.render_to(button_surf, (self.size[0] - 20, (self.size[1] // 2) - (self.text_size // 2)), t, black)
        buttons_surf.blit(button_surf, (self.size[2], self.size[3]))
        pygame.display.update()
    def show_button_select_2(self):
        button_surf = pygame.Surface((self.size[0], self.size[1]))
        button_surf.fill(black)
        len_text = len(self.Name)
        self.text_size = 12
        Button_icon_1 = pygame.image.load('./images/Button_select_pos_5.jpg')
        Button_icon = pygame.transform.scale(Button_icon_1, (self.size[0], self.size[1]))
        button_surf.blit(Button_icon, (0, 0))
        text_surf = pygame.freetype.SysFont("Tahoma", self.text_size)
        text_surf.render_to(button_surf, (int((self.size[0] / 2) - (self.text_size - self.text_size / 2) * (len_text / 2)),
                                          (self.size[1] // 2) - (self.text_size // 2)), self.Name, black)
        buttons_surf.blit(button_surf, (self.size[2], self.size[3]))
        pygame.display.update()

    def show_button_checkbox_pos_1(self):
        button_surf = pygame.Surface((self.size[0], self.size[1]))
        button_surf.fill(black)
        len_text = len(self.Name)
        if self.text_size_k == 0:
            self.text_size = 14
            Button_icon_1 = pygame.image.load('./images/Button_pos_1.jpg')
            checkbox_icon_1 = pygame.image.load('./images/checkbox_pos_1.jpg')
        elif self.text_size_k == 1:
            self.text_size = 12
            Button_icon_1 = pygame.image.load('./images/Button_select_pos_1.jpg')
        Button_icon = pygame.transform.scale(Button_icon_1, (self.size[0], self.size[1]))
        checkbox_icon = pygame.transform.scale(checkbox_icon_1, (16, 16))
        button_surf.blit(Button_icon, (0, 0))
        button_surf.blit(checkbox_icon, (self.size[0]-self.size[1]//2-8, self.size[1]//2-8))
        text_surf = pygame.freetype.SysFont("Tahoma", self.text_size)
        text_surf.render_to(button_surf, (int(((self.size[0]-self.size[1]//2-8) / 2) - (self.text_size - self.text_size / 2) * (len_text / 2)),
                                          (self.size[1] // 2) - (self.text_size // 2)), self.Name, black)
        buttons_surf.blit(button_surf, (self.size[2], self.size[3]))
        pygame.display.update()

    def show_button_checkbox_pos_2(self):
        button_surf = pygame.Surface((self.size[0], self.size[1]))
        button_surf.fill(black)
        len_text = len(self.Name)
        if self.text_size_k == 0:
            self.text_size = 14
            Button_icon_1 = pygame.image.load('./images/Button_pos_2.jpg')
            checkbox_icon_1 = pygame.image.load('./images/checkbox_pos_2.jpg')
        elif self.text_size_k == 1:
            self.text_size = 12
            Button_icon_1 = pygame.image.load('./images/Button_select_pos_1.jpg')
        Button_icon = pygame.transform.scale(Button_icon_1, (self.size[0], self.size[1]))
        checkbox_icon = pygame.transform.scale(checkbox_icon_1, (16, 16))
        button_surf.blit(Button_icon, (0, 0))
        button_surf.blit(checkbox_icon, (self.size[0]-self.size[1]//2-8, self.size[1]//2-8))
        text_surf = pygame.freetype.SysFont("Tahoma", self.text_size)
        text_surf.render_to(button_surf, (int(((self.size[0]-self.size[1]//2-8) / 2) - (self.text_size - self.text_size / 2) * (len_text / 2)),
                                          (self.size[1] // 2) - (self.text_size // 2)), self.Name, black)
        buttons_surf.blit(button_surf, (self.size[2], self.size[3]))
        pygame.display.update()

    def show_button_checkbox_pos_3(self):
        button_surf = pygame.Surface((self.size[0], self.size[1]))
        button_surf.fill(black)
        len_text = len(self.Name)
        if self.text_size_k == 0:
            self.text_size = 13
            Button_icon_1 = pygame.image.load('./images/Button_pos_3.jpg')
            checkbox_icon_1 = pygame.image.load('./images/checkbox_pos_3.jpg')
        elif self.text_size_k == 1:
            self.text_size = 12
            Button_icon_1 = pygame.image.load('./images/Button_select_pos_1.jpg')
        Button_icon = pygame.transform.scale(Button_icon_1, (self.size[0], self.size[1]))
        checkbox_icon = pygame.transform.scale(checkbox_icon_1, (16, 16))
        button_surf.blit(Button_icon, (0, 0))
        button_surf.blit(checkbox_icon, (self.size[0]-self.size[1]//2-8, self.size[1]//2-8))
        text_surf = pygame.freetype.SysFont("Tahoma", self.text_size)
        text_surf.render_to(button_surf, (int(((self.size[0]-self.size[1]//2-8) / 2) - (self.text_size - self.text_size / 2) * (len_text / 2)),
                                          (self.size[1] // 2) - (self.text_size // 2)), self.Name, black)
        buttons_surf.blit(button_surf, (self.size[2], self.size[3]))
        pygame.display.update()

    def show_button_checkbox_pos_1_3(self):
        button_surf = pygame.Surface((self.size[0], self.size[1]))
        button_surf.fill(black)
        len_text = len(self.Name)
        if self.text_size_k == 0:
            self.text_size = 14
            Button_icon_1 = pygame.image.load('./images/Button_pos_1.jpg')
            checkbox_icon_1 = pygame.image.load('./images/checkbox_pos_3.jpg')
        elif self.text_size_k == 1:
            self.text_size = 12
            Button_icon_1 = pygame.image.load('./images/Button_select_pos_1.jpg')
        Button_icon = pygame.transform.scale(Button_icon_1, (self.size[0], self.size[1]))
        checkbox_icon = pygame.transform.scale(checkbox_icon_1, (16, 16))
        button_surf.blit(Button_icon, (0, 0))
        button_surf.blit(checkbox_icon, (self.size[0]-self.size[1]//2-8, self.size[1]//2-8))
        text_surf = pygame.freetype.SysFont("Tahoma", self.text_size)
        text_surf.render_to(button_surf, (int(((self.size[0]-self.size[1]//2-8) / 2) - (self.text_size - self.text_size / 2) * (len_text / 2)),
                                          (self.size[1] // 2) - (self.text_size // 2)), self.Name, black)
        buttons_surf.blit(button_surf, (self.size[2], self.size[3]))
        pygame.display.update()

    def show_button_checkbox_pos_2_3(self):
        button_surf = pygame.Surface((self.size[0], self.size[1]))
        button_surf.fill(black)
        len_text = len(self.Name)
        if self.text_size_k == 0:
            self.text_size = 14
            Button_icon_1 = pygame.image.load('./images/Button_pos_2.jpg')
            checkbox_icon_1 = pygame.image.load('./images/checkbox_pos_3.jpg')
        elif self.text_size_k == 1:
            self.text_size = 12
            Button_icon_1 = pygame.image.load('./images/Button_select_pos_1.jpg')
        Button_icon = pygame.transform.scale(Button_icon_1, (self.size[0], self.size[1]))
        checkbox_icon = pygame.transform.scale(checkbox_icon_1, (16, 16))
        button_surf.blit(Button_icon, (0, 0))
        button_surf.blit(checkbox_icon, (self.size[0]-self.size[1]//2-8, self.size[1]//2-8))
        text_surf = pygame.freetype.SysFont("Tahoma", self.text_size)
        text_surf.render_to(button_surf, (int(((self.size[0]-self.size[1]//2-8) / 2) - (self.text_size - self.text_size / 2) * (len_text / 2)),
                                          (self.size[1] // 2) - (self.text_size // 2)), self.Name, black)
        buttons_surf.blit(button_surf, (self.size[2], self.size[3]))
        pygame.display.update()

Button_P = Button('Пассажирские', x_yP, 0)
Button_G = Button('Грузовые', x_yG, 0)
Button_N = Button('Расчёт', x_yN, 0)
Button_Ar = Button('Прибытие', x_yAr, 0)
Button_Dep = Button('Отправление', x_yDep, 0)
Button_R = Button('Перезапуск', x_yR, 0)
Button_Score_P = Button('Количество пассажирских поездов', x_ySel, 1)
Button_select_1 = Button([4, 6, 8], x_ySel4, 1)
Button_act_TF = Button('Из файла', x_y_act_TF, 0)
Button_act_TR = Button('Генерировать', x_y_act_TR, 0)

def reload_programm():
    global vertycal_tab
    global activation_calc
    global use_draw_stringsP
    global use_draw_stringsG
    layers(True, False, False)
    reload(Creat_trains)
    reload(Create_string)
    reload(Calculation)
    activation_calc = False
    use_draw_stringsG = False
    use_draw_stringsP = False
    vertycal_tab = [30]
    inputfile_activation_trains = "./data/activation_trains.txt"
    activation_trains = str(open(inputfile_activation_trains, mode='r', encoding='latin_1').read().splitlines()[0])
    if activation_trains == str(True):
        from Creat_trains import trains
    elif activation_trains == str(False):
        from input_trains import trains_GID
        trains = trains_GID
    for i in range(0, len(trains) // 4 + 1, 1):
        vertycal_tab.append(70 + i * 20)

    layers(True, False, False)

#global activation
activation_calc = False
activation = False
activation_arrival = False
scoreP = [0,1,2]

def layers(iR, iB, iSel):

    if iR == True:

        surf.set_colorkey(white)
        surf_trains.set_colorkey(white)
        surf_tabl_calc.set_colorkey(white)
        surf.fill(black)
        surf_trains.fill(black)
        tabl_surf.fill(black)
        surf_tabl_calc.fill(black)
        grid_surf.blit(surf, (gorizontal[0], vertycal[0] + 1))
        grid_surf.blit(surf_trains, (gorizontal[0], vertycal[0] - 90 + 1))
        screen.blit(grid_surf, (0, 0))
        screen.blit(tabl_surf, (gorizontal[len(gorizontal) - 1] + 20, vertycal[0]-30))
        screen.blit(surf_tabl_calc, (gorizontal[len(gorizontal) - 1] + 25, max_y*600//760))
        #pygame.display.update()
        #print("vert_li = ", len(vertycal_tab))
    elif iB == True:
        buttons_surf.fill(black)
    elif iSel == True:
        surf_trains_select.set_colorkey(white)
        surf_trains_select.fill(black)
        grid_surf.blit(surf_trains_select, (gorizontal[0], vertycal[0] - 90 + 1))
        draw_uneconomic_string()


    surf.set_colorkey(black)
    mouse_surf.fill(black)
    surf_trains.set_colorkey(black)
    surf_trains_select.set_colorkey(black)
    surf_tabl_calc.set_colorkey(black)
    draw_shedule_grid()
    #grid_surf.blit(select_surf, (0, vertycal[0] - 10))
    grid_surf.blit(surf, (gorizontal[0], vertycal[0] + 1))
    grid_surf.blit(surf_trains, (gorizontal[0], vertycal[0] - 90 + 1))
    grid_surf.blit(surf_trains_select, (gorizontal[0], vertycal[0] - 90 + 1))
    screen.blit(buttons_surf, (0, 0))
    screen.blit(tabl_surf, (gorizontal[len(gorizontal)-1]+20, vertycal[0]-30))
    screen.blit(surf_tabl_calc, (gorizontal[len(gorizontal) - 1] + 25, max_y*600//760))
    screen.blit(grid_surf, (0, 0))
    pygame.display.update()


def clik_button():
    for event in pygame.event.get():
        global activation
        global activation_arrival
        global activation_F
        global activation_R
        global activation_calc
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                sys.exit()
        elif event.type == pygame.QUIT:
            sys.exit()

        elif pygame.mouse.get_pos():
            """Анимация выделения поездов по прибытию"""
            pos = pygame.mouse.get_pos()
            if pos[1] >= vertycal[0]-10 and pos[1] <= vertycal[0]+10:
                inputfile_activation_trains = "./data/activation_trains.txt"
                activation_trains = str(
                    open(inputfile_activation_trains, mode='r', encoding='latin_1').read().splitlines()[0])
                if activation_trains == str(True):
                    from Creat_trains import trains
                elif activation_trains == str(False):
                    from input_trains import trains_GID
                    trains = trains_GID
                from Create_string import times_strings, score_stations # trains_for_string_0, trains_for_string
                from Calculation import trains_for_strings_F, trains_for_strings_0
                if activation_calc == False:
                    #trains_for_string = trains_for_string_0
                    trains_for_string = trains_for_strings_0
                else:
                    #trains_for_string = trains_for_string
                    trains_for_string = trains_for_strings_F
                trains_d = trains.copy()
                k_screen_trains(trains_d)
                for u in range(1, len(trains), 4):
                    #if event.type == pygame.MOUSEBUTTONDOWN:
                    if activation_arrival == True:
                        x_yT = [14, 14, gorizontal[0]+int(trains_d[u])*kf_1 - 7, int(vertycal[0]) - 7]
                        if pos[0] >= x_yT[2] and pos[0] <= x_yT[2] + x_yT[0] and pos[1] >= x_yT[3] and pos[1] <= x_yT[3] + x_yT[
                            1]:
                            pygame.draw.rect(select_surf, red, ((x_yT[2], 3), (x_yT[0], x_yT[1])), 0)
                            grid_surf.blit(select_surf, (0, vertycal[0] - 7))
                            #layers(False, False)
                            pygame.display.update()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if event.button == 3:
                                    surf_trains_select.blit(arrow2, (int(int(trains_d[u]) * kf_1) - 30, int(vertycal[0] - vertycal[0]) + 15))
                                    for y in range(0, len(trains_for_string), 1):
                                        if trains_for_string[y] != 0:
                                            if trains_for_string[y] == trains[u + 2]:
                                                #print("№ = ", trains_for_string[y], trains[u +2 ])
                                                surf_trains_select.blit(arrow2, (int(int(times_strings[y * 10 + 8]) * kf_1),
                                                                          int(vertycal[4] - vertycal[0]) + 90))
                                                pygame.draw.circle(surf_trains_select, grey, (
                                                    int((int(times_strings[y * 10 + 8])) * kf_1),
                                                    int(vertycal[4] - vertycal[0]) + 90), 4, 2)
                                                #times_strings_0 = times_strings.copy()
                                                """Делаем подсветку значений в таблице"""
                                                if int(float(times_strings_0[y * 10 + 1]) - 60 * (
                                                    float(times_strings_0[y * 10 + 1]) // 60)) // 10 == 0:
                                                    time_arr = '0' + str(int(float(times_strings_0[y * 10 + 1]) - 60 * (
                                                            float(times_strings_0[y * 10 + 1]) // 60)))
                                                else:
                                                    time_arr = str(int(float(times_strings_0[y * 10 + 1]) - 60 * (
                                                            float(times_strings_0[y * 10 + 1]) // 60)))

                                                draw_text(12, white, (str(int(
                                                        float(times_strings_0[y * 10 + 1]) // 60)) + ':' + time_arr))
                                                tabl_surf.blit(surf_text_image_2, (
                                                        gorizontal_tab[4] + 5, vertycal_tab[(u-1)//4+1] + 10 - 5))

                                                if int(trains[u] - 60 * (trains[u] // 60)) // 10 == 0:
                                                    time_arr = '0' + str(
                                                        int(trains[u] - 60 * (trains[u] // 60)))
                                                else:
                                                    time_arr = str(
                                                        int(trains[u] - 60 * (trains[u] // 60)))
                                                draw_text(12, white, str(trains[u + 2]))
                                                tabl_surf.blit(surf_text_image_2,
                                                               (gorizontal_tab[0] + 5, vertycal_tab[(u-1)//4+1] + 10 - 5))
                                                draw_text(12, white, str(trains[u-1]))
                                                tabl_surf.blit(surf_text_image_2,
                                                               (gorizontal_tab[1] + 5, vertycal_tab[(u-1)//4+1] + 10 - 5))
                                                draw_text(12, white, str(trains[u+1]))
                                                tabl_surf.blit(surf_text_image_2,
                                                               (gorizontal_tab[2] + 5, vertycal_tab[(u-1)//4+1] + 10 - 5))
                                                draw_text(12, white,
                                                          (str(int(trains[u] // 60)) + ':' + time_arr))
                                                tabl_surf.blit(surf_text_image_2,
                                                               (gorizontal_tab[3] + 5, vertycal_tab[(u-1)//4+1] + 10 - 5))


                                                for w in range(1, score_stations*2-1, 2):
                                                    pygame.draw.line(surf, white, [(int(times_strings[y * 10 + w]) * kf_1),
                                                                                   int(stations[w] - stations[0])],
                                                                     [(int(times_strings[y * 10 + w + 1]) * kf_1),
                                                                      int(stations[w + 1] - stations[0])], 1)

                                            else:
                                                continue
                                        else:
                                            continue

                        else:

                            pygame.draw.rect(select_surf, black, ((x_yT[2], 0), (x_yT[0], x_yT[1])), 0)
                            grid_surf.blit(select_surf, (0, vertycal[0] - 10))
                            pygame.display.update()

            else:
                select_surf.fill(black)
                grid_surf.blit(select_surf, (0, vertycal[0] - 10))
                pygame.display.update()


            if pos[0] >= x_yP[2] and pos[0] <= x_yP[2]+x_yP[0] and pos[1] >= x_yP[3] and pos[1] <= x_yP[3]+x_yP[1]:
                """Строим пассажирские нитки"""
                Button_P.show_button_pos_2()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #draw_button('', 25, str(event.pos[0]), [100, 40, 200, 670], Button_pos_1)
                    Button_P.show_button_pos_3()
                    layers(True, False, False)
                    draw_stringsP()
                    print("vert_li = ", len(vertycal_tab))

            elif pos[0] >= x_yG[2] and pos[0] <= x_yG[2]+x_yG[0] and pos[1] >= x_yG[3] and pos[1] <= x_yG[3]+x_yG[1]:
                """Строим грузовые нитки"""
                Button_G.show_button_pos_2()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Button_G.show_button_pos_3()
                    layers(False, False, False)
                    draw_stringsG()

            elif pos[0] >= x_yN[2] and pos[0] <= x_yN[2] + x_yN[0] and pos[1] >= x_yN[3] and pos[1] <= x_yN[3] + x_yN[
                1]:
                """Выполняем расчет"""
                Button_N.show_button_pos_2()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Button_N.show_button_pos_3()
                    if activation_F == True or activation_R == True:
                        activation_calc = True
                        layers(True, False, False)
                        draw_uneconomic_string()
                        draw_stringsP()
                        output_calculation_results()
                    else:
                        continue

            elif pos[0] >= x_yAr[2] and pos[0] <= x_yAr[2] + x_yAr[0] and pos[1] >= x_yAr[3] and pos[1] <= x_yAr[3] + x_yAr[
                1]:
                """Строим прибытие поездов"""
                Button_Ar.show_button_pos_2()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Button_Ar.show_button_pos_3()
                    if activation_F == True or activation_R == True:
                        draw_trains_arrivals()
                        activation_arrival = True

                    else:
                        continue

            elif pos[0] >= x_yDep[2] and pos[0] <= x_yDep[2] + x_yDep[0] and pos[1] >= x_yDep[3] and pos[1] <= x_yDep[3] +x_yDep[1]:
                """Строим отправление пездов"""
                Button_Dep.show_button_pos_2()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Button_Dep.show_button_pos_3()
                    if activation_F == True or activation_R == True:
                        draw_trains_departures()
                    else:
                        continue

            elif pos[0] >= x_yR[2] and pos[0] <= x_yR[2]+x_yR[0] and pos[1] >= x_yR[3] and pos[1] <= x_yR[3]+x_yR[1]:
                """Перезагрузка программы"""
                Button_R.show_button_pos_2()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Button_R.show_button_pos_3()
                    #pygame.draw.rect(surf, black, ((0, 0), (gorizontal[len(gorizontal)-1]-gorizontal[0], vertycal[4]- vertycal[0])), 5)
                    reload_programm()
                else:
                    continue

            elif pos[0] >= x_y_act_TF[2] and pos[0] <= x_y_act_TF[2]+x_y_act_TF[0] and pos[1] >= x_y_act_TF[3] and pos[
                1] <= x_y_act_TF[3]+x_y_act_TF[1]:
                """Строим поезда из файла"""
                if activation_F == False:
                    Button_act_TF.show_button_checkbox_pos_2()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        Button_act_TF.show_button_checkbox_pos_3()
                        activation_F = True
                        activation_R = False
                        #Button_act_TF.show_button_checkbox_pos_1()
                        Button_act_TR.show_button_checkbox_pos_1()
                        outputfile_activation_trains = "./data/activation_trains.txt"
                        activation_trains_write = open(outputfile_activation_trains, mode='w', encoding='latin_1')
                        activation_trains_write.write(str(False))
                        activation_trains_write.close()
                        reload_programm()
                        #layers(False, False, False)

                else:
                    Button_act_TF.show_button_checkbox_pos_2_3()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        Button_act_TF.show_button_checkbox_pos_3()
                        activation_F = False
                        activation_R = False
                        Button_act_TR.show_button_checkbox_pos_1()

                layers(False, False, False)

            elif pos[0] >= x_y_act_TR[2] and pos[0] <= x_y_act_TR[2]+x_y_act_TR[0] and pos[1] >= x_y_act_TR[3] and pos[
                1] <= x_y_act_TR[3]+x_y_act_TR[1]:
                """Строим поезда посредством генерирования"""
                if activation_R == False:
                    Button_act_TR.show_button_checkbox_pos_2()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        Button_act_TR.show_button_checkbox_pos_3()
                        activation_R = True
                        activation_F = False
                        Button_act_TF.show_button_checkbox_pos_1()
                        #Button_act_TR.show_button_checkbox_pos_1()
                        outputfile_activation_trains = "./data/activation_trains.txt"
                        activation_trains_write = open(outputfile_activation_trains, mode='w', encoding='latin_1')
                        activation_trains_write.write(str(True))
                        activation_trains_write.close()
                        reload_programm()
                        #layers(False, False, False)
                else:
                    Button_act_TR.show_button_checkbox_pos_2_3()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        Button_act_TR.show_button_checkbox_pos_3()
                        activation_R = False
                        activation_F = False
                        Button_act_TF.show_button_checkbox_pos_1()

                layers(False, False, False)


            elif pos[0] >= x_ySel[2] and pos[0] <= x_ySel[2] + x_ySel[0] and pos[1] >= x_ySel[3] and pos[1] <= x_ySel[
                3] + x_ySel[1]:
                """Выбираем количество пассажирских поездов"""
                Button_Score_P.show_button_pos_2()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if activation == False:
                        Button_Score_P.show_button_pos_3()
                        Button_select_1.show_button_select()
                        # global activation
                        activation = True
                    else:
                        activation = False
                        layers(False, True, False)
                        draw_buttons()

            elif pos[0] >= x_ySel4[2] and pos[0] <= x_ySel4[2] + x_ySel4[0] and pos[1] >= x_ySel4[3] + \
                scoreP[0] * x_ySel4[1] // 3 and pos[1] <= x_ySel4[3] + (scoreP[0] + 1) * x_ySel4[1] // 3:
                if activation == True:
                    x_ySel5 = [250, 16, 460, vertycal[4]+80 + 20 + scoreP[0] * x_ySel4[1] // 3]
                    Button_select_1.show_button_select()
                    Button_select_2 = Button('4', x_ySel5, 1)
                    Button_select_2.show_button_select_2()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        activation = False
                        layers(False, True, False)
                        draw_buttons()
                        inputfile_score_P_trains = "./data/score_P_trains.txt"
                        myfile = open(inputfile_score_P_trains, mode='w', encoding='latin_1')
                        myfile.write(str(4) )
                        myfile.close()
                        reload_programm()

            elif pos[0] >= x_ySel4[2] and pos[0] <= x_ySel4[2] + x_ySel4[0] and pos[1] >= x_ySel4[3] + \
                scoreP[1] * x_ySel4[1] // 3 and pos[1] <= x_ySel4[3] + (scoreP[1] + 1) * x_ySel4[1] // 3:
                if activation == True:
                    x_ySel5 = [250, 16, 460, vertycal[4]+80 + 20 + scoreP[1] * x_ySel4[1] // 3]
                    Button_select_1.show_button_select()
                    Button_select_2 = Button('6', x_ySel5, 1)
                    Button_select_2.show_button_select_2()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        activation = False
                        layers(False, True, False)
                        draw_buttons()
                        inputfile_score_P_trains = "./data/score_P_trains.txt"
                        myfile = open(inputfile_score_P_trains, mode='w', encoding='latin_1')
                        myfile.write(str(6))
                        myfile.close()
                        reload_programm()

            elif pos[0] >= x_ySel4[2] and pos[0] <= x_ySel4[2] + x_ySel4[0] and pos[1] >= x_ySel4[3] + \
                scoreP[2] * x_ySel4[1] // 3 and pos[1] <= x_ySel4[3] + (scoreP[2] + 1) * x_ySel4[1] // 3:
                if activation == True:
                    x_ySel5 = [250, 16, 460, vertycal[4]+80 + 20 + scoreP[2] * x_ySel4[1] // 3]
                    Button_select_1.show_button_select()
                    Button_select_2 = Button('8', x_ySel5, 1)
                    Button_select_2.show_button_select_2()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        activation = False
                        layers(False, True, False)
                        draw_buttons()
                        inputfile_score_P_trains = "./data/score_P_trains.txt"
                        myfile = open(inputfile_score_P_trains, mode='w', encoding='latin_1')
                        myfile.write(str(8))
                        myfile.close()
                        reload_programm()

            elif pos[0] >= 0 and pos[0] <= max_x and pos[1] >= 0 and pos[1] <= max_y:
                draw_buttons()
                if activation == True:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        activation = False
                        layers(False, True, False)
                        draw_buttons()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 3:
                        draw_trains_arrivals()
                        draw_trains_departures()
                        layers(False, False, True)


                else:
                    continue

            else:
                draw_buttons()


clock = pygame.time.Clock()
t = ''
draw_buttons()
pygame.display.update()
while True:
    clock.tick(60)
    clik_button()
    layers(False, False, False)

time.sleep(1)

#pygame.quit()
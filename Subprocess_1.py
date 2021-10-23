import pygame
import sys
import  subprocess
import pygame.freetype

import time

black = [0, 0 ,0]
white = [255, 255, 255]
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
grey =[128, 128, 128]
maroon = [128, 0, 0]
unvis = [255, 0, 255]
olive = [128, 128, 0]
max_x = 300
max_y = 300
x_y_1280 = [100, 40, 100, 100]
x_y_1600 = [100, 40, 100, 160]
x_y_1920 = [100, 40, 100, 220]


buttons_surf = pygame.Surface((max_x, max_y))
buttons_surf.fill(black)

#input = <insert input>
def process():
    process = subprocess.Popen(["python","Grafic_pygame.py"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=False)
#output = process.communicate(input)[0]


pygame.init()
screen_1 = pygame.display.set_mode((max_x, max_y), pygame.RESIZABLE)
pygame.display.set_caption("Clever_shedule")
Label_FONT = pygame.freetype.SysFont("Tahoma", 22)


def screen_2 ():
    pygame.init()
    screen_2 = pygame.display.set_mode((max_x, max_y), pygame.RESIZABLE)
    pygame.display.set_caption("Крутая игра")


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
            Button_icon_1 = pygame.image.load('D:/Python/Shedule/exet/images/Button_pos_1.jpg')
        elif self.text_size_k == 1:
            self.text_size = 12
            Button_icon_1 = pygame.image.load('D:/Python/Shedule/exet/images/Button_select_pos_1.jpg')
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
            Button_icon_1 = pygame.image.load('D:/Python/Shedule/exet/images/Button_pos_2.jpg')
        elif self.text_size_k == 1:
            self.text_size = 12
            Button_icon_1 = pygame.image.load('D:/Python/Shedule/exet/images/Button_select_pos_2.jpg')
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
            Button_icon_1 = pygame.image.load('D:/Python/Shedule/exet/images/Button_pos_3.jpg')
        elif self.text_size_k == 1:
            self.text_size = 11
            Button_icon_1 = pygame.image.load('D:/Python/Shedule/exet/images/Button_select_pos_3.jpg')
        Button_icon = pygame.transform.scale(Button_icon_1, (self.size[0], self.size[1]))
        button_surf.blit(Button_icon, (0, 0))
        text_surf = pygame.freetype.SysFont("Tahoma", self.text_size)
        text_surf.render_to(button_surf, (int((self.size[0] / 2) - (self.text_size - self.text_size / 2) * (len_text / 2)),
                                          (self.size[1] // 2) - (self.text_size // 2)), self.Name, black)
        buttons_surf.blit(button_surf, (self.size[2], self.size[3]))
        pygame.display.update()


clock = pygame.time.Clock()
Button_1 = Button('1280x768', x_y_1280, 0)
Button_2 = Button('1600x900', x_y_1600, 0)
Button_3 = Button('1920x1080', x_y_1920, 0)

def click_button():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
        elif pygame.mouse.get_pos():
            pos = pygame.mouse.get_pos()
            if pos[0] >= x_y_1280[2] and pos[0] <= x_y_1280[2] + x_y_1280[0] and pos[1] >= x_y_1280[3] and pos[1] <= \
                x_y_1280[3] + x_y_1280[1]:
                Button_1.show_button_pos_2()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        Button_1.show_button_pos_3()
                        screen_1.blit(buttons_surf, (0, 0))
                        pygame.display.update()
                        outputfile_display = "./data/display_x.txt"
                        activation_display_write = open(outputfile_display, mode='w', encoding='latin_1')
                        activation_display_write.write(str(1280))
                        activation_display_write.close()
                        outputfile_display = "./data/display_y.txt"
                        activation_display_write = open(outputfile_display, mode='w', encoding='latin_1')
                        activation_display_write.write(str(768))
                        activation_display_write.close()
                        import Grafic_pygame

            elif pos[0] >= x_y_1600[2] and pos[0] <= x_y_1600[2] + x_y_1600[0] and pos[1] >= x_y_1600[3] and pos[1] <= \
                x_y_1600[3] + x_y_1600[1]:
                Button_2.show_button_pos_2()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Button_2.show_button_pos_3()
                    screen_1.blit(buttons_surf, (0, 0))
                    pygame.display.update()
                    outputfile_display = "D:/Python/Shedule/exet/data/display_x.txt"
                    activation_display_write = open(outputfile_display, mode='w', encoding='latin_1')
                    activation_display_write.write(str(1600))
                    activation_display_write.close()
                    outputfile_display = "D:/Python/Shedule/exet/data/display_y.txt"
                    activation_display_write = open(outputfile_display, mode='w', encoding='latin_1')
                    activation_display_write.write(str(900))
                    activation_display_write.close()
                    import Grafic_pygame

            elif pos[0] >= x_y_1920[2] and pos[0] <= x_y_1920[2] + x_y_1920[0] and pos[1] >= x_y_1920[3] and pos[1] <= \
                x_y_1920[3] + x_y_1920[1]:
                Button_3.show_button_pos_2()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Button_3.show_button_pos_3()
                    screen_1.blit(buttons_surf, (0, 0))
                    pygame.display.update()
                    outputfile_display = "D:/Python/Shedule/exet/data/display_x.txt"
                    activation_display_write = open(outputfile_display, mode='w', encoding='latin_1')
                    activation_display_write.write(str(1920))
                    activation_display_write.close()
                    outputfile_display = "D:/Python/Shedule/exet/data/display_y.txt"
                    activation_display_write = open(outputfile_display, mode='w', encoding='latin_1')
                    activation_display_write.write(str(1080))
                    activation_display_write.close()
                    import Grafic_pygame

            elif pos[0] >= 0 and pos[0] <= max_x and pos[1] >= 0 and pos[1] <= max_y:
                Button_1.show_button_pos_1()
                Button_2.show_button_pos_1()
        else:
            Button_1.show_button_pos_1()
            Button_2.show_button_pos_1()


Button_1.show_button_pos_1()
Button_2.show_button_pos_1()
Button_3.show_button_pos_1()
Label_FONT.render_to(buttons_surf, (50, 50), "Выбирите разрешение", red)
screen_1.blit(buttons_surf, (0, 0))
pygame.display.update()
while True:
    clock.tick(60)
    click_button()
    screen_1.blit(buttons_surf, (0, 0))
    pygame.display.update()

time.sleep(1)


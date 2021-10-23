"""print('Введите координаты концов первого отрезка.')
x1_1, y1_1 = int(input('Первая точка x = ')), int(input('y = '))
x1_2, y1_2 = int(input('вторая точка x = ')), int(input('y = '))
print('Введите координаты концов второго отрезка.')
x2_1, y2_1 = int(input('Первая точка x = ')), int(input('y = '))
x2_2, y2_2 = int(input('вторая точка x = ')), int(input('y = '))"""

from Create_string import timesG11
from Create_string import times_strings
St1_DG =0
def cross_lines1 (x1_1, x1_2, y1_1, y1_2, x2_1, x2_2, y2_1, y2_2):
# составляем формулы двух прямых
    A1 = y1_1 - y1_2
    B1 = x1_2 - x1_1
    C1 = x1_1*y1_2 - x1_2*y1_1
    A2 = y2_1 - y2_2
    B2 = x2_2 - x2_1
    C2 = x2_1*y2_2 - x2_2*y2_1
# решаем систему двух уравнений
    if B1*A2 - B2*A1 != 0:
        y = (C2*A1 - C1*A2) / (B1*A2 - B2*A1)
        x = (-C1 - B1*y) / A1
# проверяем, находится ли решение системы (точка пересечения) на первом отрезке, min/max - потому
# что координаты точки могут быть заданы не по порядку возрастания
        if min(x1_1, x1_2) <= x <= max(x1_1, x1_2) and min(y1_1, y1_2) <= y <= max(y1_1, y1_2) and \
            min(x2_1, x2_2) <= x <= max(x2_1, x2_2) and min(y2_1, y2_2) <= y <= max(y2_1, y2_2):
#            print('Точка пересечения отрезков есть, координаты: ({0:f}, {1:f}).'.format(x, y))
            timesG11[1] = int(times1[1]) + 5
            timesG11[2] = int(timesG11[1]) + Gtravel_time1_2
            timesG11[3] = timesG11[2]
            timesG11[4] = int(timesG11[3]) + Gtravel_time2_3
            timesG11[5] = timesG11[4]
            timesG11[6] = int(timesG11[5]) + Gtravel_time3_4
            timesG11[7] = timesG11[6]
            timesG11[8] = int(timesG11[7]) + Gtravel_time4_5
            timesG11[9] = timesG11[8]
            St1_DG = int(timesG11[1])
            times_strings.extend(timesG11)
            print(times_strings)
            timesG11.clear()
            print(timesG11)

        else:
            times_strings.extend(timesG11)
          # print('Точки пересечения отрезков нет.')

# случай деления на ноль, то есть параллельность
    if B1*A2 - B2*A1 == 0:
        times_strings.extend(timesG11)
#        print('Точки пересечения отрезков нет, отрезки ||.')

#cross_lines(5,6,7,8,2,4,6,8)
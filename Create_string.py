import random
from Creat_class_stringP import StringP, Ptravel_time
from Creat_class_stringG import StringG, Gtravel_time


St1_departure = 0
global St2_departure1
times_strings = []
times_strings1 =[]
timesG11 = []
timesP = []
St1_D = 0
score_stations = 5
inputfile_score_P_trains = "./data/score_P_trains.txt"
score_P_trains = int(open(inputfile_score_P_trains, mode = 'r', encoding = 'latin_1').read().splitlines()[0])
print("score_p = ", score_P_trains)
score_clock = 8
def creat_string (x, y, z, n):
    St1_departure = y + random.randint(10, 120)
    while St1_departure > z or St1_departure < n:
        #print("St1_departure0 = " + str (St1_departure))
        St1_departure = y + random.randint(10, 120)
    else:
        St1_departure = St1_departure + 0
        #print("St1_departure = " + str (St1_departure))
    x = StringP(0, 0, St1_departure, 0, 0, 0, 0, 0, 0, 0, 0, Ptravel_time[0], Ptravel_time[1], Ptravel_time[2],
              Ptravel_time[3])
    x.creat_arrival_depature()
    x.show_arrival_depature()
    inputfile = "./data/Parametrs.txt"
    timesP1 = open(inputfile, mode = 'r', encoding = 'latin_1').read().splitlines()
    timesP.extend(timesP1)
    global St1_D
    St1_D = St1_departure
    return St1_D

#inputfileG = 'D:\Python\Shedule\ParametrsG.txt'
inputfileG = "./data/ParametrsG.txt"
def creat_string_gr (a, b):
    St1_departure = b + 10
    a = StringG (0, 0, St1_departure, 0, 0, 0, 0, 0, 0, 0, 0, Gtravel_time[0], Gtravel_time[1], Gtravel_time[2],
              Gtravel_time[3])
    a.creat_arrival_depature()
    timesG1 = open(inputfileG, mode='r', encoding='latin_1').read().splitlines()
    timesG11.extend(timesG1)
    #print(timesG11)
    global St1_DG
    St1_DG = St1_departure
    return St1_DG

def cross_lines1 (x1_1, x1_2, y1_1, y1_2, x2_1, x2_2, y2_1, y2_2, j):
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
            """"==============Перенос времени отправления при пересечении с пассажирским поездом==============="""
            for G in range (1, (score_stations - 1) * 2, 2):
                if j == G:
                    timesG11[j] = str(x1_1 + 5)
                    for i in range (G, (score_stations * 2) - 1, 2):
                        timesG11[i+1] = str(int(timesG11[i]) + Gtravel_time[(i-1)//2])
                        timesG11[i+2] = timesG11[i+1]
                else:
                    continue
                global St1_DG
                St1_DG = int(timesG11[1])
                return St1_DG
                times_strings1.clear()
                times_strings1.extend(timesG11)

        else:
            times_strings1.clear()
            times_strings1.extend(timesG11)
          # print('Точки пересечения отрезков нет.')

# случай деления на ноль, то есть параллельность
    if B1*A2 - B2*A1 == 0:
        times_strings1.clear()
        times_strings1.extend(timesG11)

#inputfile = 'D:\Python\Shedule\Parametrs.txt'
#inputfile = "Parametrs.txt"
for i in range (1, score_P_trains+1, 1):
    creat_string("P", St1_D, 60 * i, 0)
    #print("timesP =", timesP, len(timesP))
creat_string_gr("G1", St1_departure - 20)
timesG11.clear()

while St1_DG < (score_clock)*60-10:
    creat_string_gr("G2", St1_DG)

    for i in range (1, 8, 2):
        for ti in range (-5, 6, 5):
            for y in range (0, score_P_trains):
                cross_lines1(int(timesP[i+(y*10)]), int(timesP[i + 1+(y*10)]), 0, 1, int(timesG11[i]) + ti, int(timesG11[i + 1]) + ti, 0,1, i)

    times_strings.extend(times_strings1)
    timesG11.clear()
    #print(times_strings)
stations = [150, 150, 300, 300, 450, 450, 600, 600, 750, 750]

#print(len(times_strings))


#print("times 1 = ",times1)
#print(times2)
#print(times3)
#print(times4)


"""======================Integration================================================="""
#global trains
inputfile_activation_trains = "./data/activation_trains.txt"
activation_trains = str(open(inputfile_activation_trains, mode = 'r', encoding = 'latin_1').read().splitlines()[0])
if activation_trains == str(True):
    from Creat_trains import trains
elif activation_trains == str(False):
    from input_trains import trains_GID
    trains = trains_GID


trains_2 = trains.copy()
time_t = 30
good_trains = []
k = 1
for u in range(1, len(times_strings), 10):
    for i in range(1, len(trains), 4):
        if int(times_strings[u]) >= int(trains[i])+time_t:
            good_trains.append("№-"+str((u-1)//10))
            good_trains.extend(trains[i-1:i+3])
            k += 1
        else:
            continue
i = 0
score_trains_str = []
score_ost = []
for u in range (1, len(times_strings), 10):
    score_trains_str.append(good_trains.count('№-' + str(u//10)))
    i += 1

"""Opredelnie kolichestva ostanovok u kajdoy nitky"""
for u in range(0, len(score_trains_str), 1):
    if score_trains_str[u] != 0:
        ost = 0
        for i in range(2, 7, 2):
            if times_strings[u*10+i] != times_strings[u*10+i+1]:
                ost += 1
            else:
                continue
        score_ost.append(ost)
    else:
        score_ost.append(0)

"""First selection stage"""
h = 0

for i in range(0, len(score_trains_str), 1):
    if score_trains_str[i] == 0:
        h += 1
    else:
        continue

"""Determenation lost time at technical station"""
use_strings = len(times_strings)//10-h
loss_strings = []
loss_strings_time = []
for i in range(0, len(score_trains_str), 1):
    if score_trains_str[i] != 0:
        j = i
        a = score_trains_str[i]
        if (int(score_trains_str[i])+j) <= (len(score_trains_str)-1):

            while a!= score_trains_str[int(score_trains_str[i])+j]:
                a = score_trains_str[int(score_trains_str[i])+j]
                j +=(a-(int(score_trains_str[j])))
                if a < len(score_trains_str) and (
                        int(score_trains_str[i]) + j) <= (len(score_trains_str) - 1):
                    continue

                else:

                    b = score_trains_str[len(score_trains_str)-1] - (len(score_trains_str)- i - 1)
                    loss_strings.append((len(score_trains_str)- i - 1) + b)
                    loss_time = (int(times_strings[len(times_strings)-9]) - int(times_strings[i*10+1]))
                    for g in range (1, b+1, 1):
                        if i == len(score_trains_str):
                            g = 0
                        else:
                            continue
                        loss_time = loss_time + (int(times_strings[len(times_strings)-9]) - int(times_strings[(i+g)*10+1]))
                    loss_strings_time.append(loss_time)
                    break

            else:
                loss_strings.append(a)
                loss_time = (int(times_strings[(int(score_trains_str[i]) +j)*10 +1]) - int(times_strings[i * 10 + 1]))
                loss_strings_time.append(loss_time)

        else:
            b = score_trains_str[len(score_trains_str) - 1] - (len(score_trains_str) - i - 1) # kolichestvo poezdov za predelamy grafika
            loss_strings.append((len(score_trains_str) - i - 1) + b)
            loss_time = (int(times_strings[len(times_strings)-9]) - int(times_strings[i * 10 + 1]))
            for g in range(1, b + 1, 1):
                if i == len(score_trains_str):
                    g = 0
                else:
                    continue
                loss_time = loss_time + (int(times_strings[len(times_strings) - 9]) - int(times_strings[(i + g) * 10 + 1]))

                if i+g+1 <= len(score_trains_str)-1:
                    continue
                else:
                    break
            loss_strings_time.append(loss_time)

    else:
        loss_strings.append(0)
        loss_strings_time.append(0)

"""Determination a good strings"""
good_strings =[]
weights = []
for i in range(0, len(score_ost), 1):
    string_number = '№-' + str(i)
    if score_ost[i] != 0:
        time_racing = 3
        time_slowdown  = 2
        e_br = 1130.81
        e_lok = 560.31
        e_p = 20.24
        V_x = 80
        alpha = 3.6
        C_e = 3.1
        H_e = 124.8

        time_promej = int(times_strings[i*10+3]) - int(times_strings[i*10+2]) + int(times_strings[i*10+5]) - \
                      int(times_strings[i*10+4]) + int(times_strings[i*10+7]) - int(times_strings[i*10+6])
        for j in range(0, len(good_trains), 5):
            if str(good_trains[j]) ==  string_number:
                weights.append(good_trains[j+1])
            else:
                continue

        weight = min(weights)
        weights.clear()
        P_lb = e_br*((time_racing+time_slowdown)*score_ost[i] + time_promej)/60
        P_rz = 3.8*weight*(V_x**2)*alpha*score_ost[i]*(10**(-6))
        P_lok = e_lok*((time_racing+time_slowdown)*score_ost[i] + time_promej)/60
        P_p = e_p*((time_racing+time_slowdown)*score_ost[i] + time_promej)/60
        P_e = C_e*time_promej*H_e/60
        P_tex = loss_strings_time[i]*(e_lok+e_p)/60
        P_prom = P_lb+P_rz+P_lok+P_p+P_e
        #print("P_tex =", P_tex)
        #print("P_prom =", P_prom)
        if P_prom <= P_tex:
            good_strings.append(1)
        else:
            good_strings.append(0)
    else:
        good_strings.append(1)
#print("good_strings =", good_strings)

"""Second selection stage"""
score_trains_str_2 = score_trains_str.copy()
good_trains_2 = good_trains.copy()
trains_for_string = []
strings_prom = []
priority = []
f = 0
for i in range(0, len(score_ost), 1):
    #print("!i =", i)
    if score_trains_str_2[i] > 0 and good_strings[i] != 0:
        if score_trains_str_2[i] != 1:
            string_number1 = '№-' + str(i) #str(score_trains_str_2[i])
            for y in range(0, len(good_trains_2), 5):
                if str(good_trains_2[y]) == str(string_number1):
                    weights.append(good_trains_2[y + 1])
                    priority.append(good_trains_2[y + 3])
                else:
                    continue

            for j in range(i, len(good_strings)+10, 1):
                if len(strings_prom)< len(weights):
                    if j < len(good_strings):
                        if good_strings[j] == 0:
                            continue
                        else:
                            strings_prom.append(score_ost[j])
                    else:
                        strings_prom.append(0)
                else:
                    break

            z=len(priority)
            for y in range(z-1, -1, -1):
                if priority[y] != max(priority):
                    del priority[y]
                    del weights[y]
                    del strings_prom[y]
                else:
                    continue
            priority.clear()

            """Распределение n поездов между k ниток"""
            for u in range(len(weights) - 1, -1, -1):
                #print("string_prom[0] = ", strings_prom[0])
                if strings_prom[0] != min(strings_prom):
                    if strings_prom[0] <= strings_prom[u]:
                        if len(weights) != 1:
                            weights.remove(min(weights))
                        del strings_prom[u]
                    else:
                        if len(weights) != 1:
                            weights.remove(max(weights))
                        del strings_prom[u]
                    #print("weight_0 = ", weights)
                else:
                    weights_1 = max(weights)
                    weights.clear()
                    weights.append(weights_1)

            trains_for_string.append(100)
            for y in range(0, len(good_trains_2)-2, 5):
                #print("y = ", y)
                if str(good_trains_2[y+1]) == str(weights[0]):
                    trains_for_string = trains_for_string[:-1]
                    trains_for_string.append(good_trains_2[y + 4])
                else:
                    continue
            weights.clear()
            for y in range(0, len(good_trains_2), 5):
                if good_trains_2[y + 4] == trains_for_string[len(trains_for_string) - 1]:
                    del good_trains_2[y]
                    good_trains_2.insert(y, 0)
                    del good_trains_2[y + 1]
                    good_trains_2.insert(y + 1, 0)
                    del good_trains_2[y + 2]
                    good_trains_2.insert(y + 2, 0)
                    del good_trains_2[y + 3]
                    good_trains_2.insert(y + 3, 0)
                    del good_trains_2[y + 4]
                    good_trains_2.insert(y + 4, 0)
                else:
                    continue
            for u in range(i + 1, len(score_ost), 1):
                score_trains_str_2[u] -= 1

        else:
            trains_for_string.append(100)
            string_number2 = '№-' + str(i) # str(score_trains_str_2[i])
            for y in range(0, len(good_trains_2), 5):
                if str(good_trains_2[y]) == str(string_number2):
                    trains_for_string = trains_for_string[:-1]
                    trains_for_string.append(good_trains_2[y+4])
                else:
                    continue
            for y in range(0, len(good_trains_2), 5):
                if good_trains_2[y + 4] == trains_for_string[len(trains_for_string) - 1]:

                    del good_trains_2[y]
                    good_trains_2.insert(y, 0)
                    del good_trains_2[y + 1]
                    good_trains_2.insert(y + 1, 0)
                    del good_trains_2[y + 2]
                    good_trains_2.insert(y + 2, 0)
                    del good_trains_2[y + 3]
                    good_trains_2.insert(y + 3, 0)
                    del good_trains_2[y + 4]
                    good_trains_2.insert(y + 4, 0)
                else:
                    continue
            for u in range(i + 1, len(score_ost), 1):
                score_trains_str_2[u] -= 1

    else:
        trains_for_string.append(0)

print("trains_for_string =", trains_for_string)

"""=========Formation of trains without taking into account calculation===================="""
trains_for_string_0 = []
trains_0 = trains.copy()
for i in range(0, len(times_strings) // 10, 1):
    for u in range(0, len(trains) // 4, 1):
        #print("====", times_strings[i * 10 + 1], trains_0[u * 4 + 1])
        if int(trains_0[u * 4 + 1]) != 5000:
            if int(times_strings[i * 10 + 1]) >= int(trains_0[u * 4 + 1]) + time_t:
                trains_for_string_0.append(trains[u * 4 + 3])
                del trains_0[u * 4 + 1]
                trains_0.insert(u * 4 + 1, 5000)
                break
            else:
                trains_for_string_0.append(0)
                break
        elif int(trains_0[u * 4 + 1]) == 5000:
            continue

print("trains_for_string_0 = ",trains_for_string_0)

"""===========Finaly calculation==================="""
def calculation (trains_for_string):
    P_tex_finally = 0
    P_prom_finally = 0
    #P_Finally = 0
    for i in range (0, len(trains_for_string), 1):
        if trains_for_string[i] != 0:
            if score_ost[i] != 0:
                time_racing = 3
                time_slowdown = 2
                e_br = 1130.81
                e_lok = 560.31
                e_p = 20.24
                V_x = 80
                alpha = 3.6
                C_e = 3.1
                H_e = 124.8
                time_promej = int(times_strings[i * 10 + 3]) - int(times_strings[i * 10 + 2]) + int(
                    times_strings[i * 10 + 5]) - \
                              int(times_strings[i * 10 + 4]) + int(times_strings[i * 10 + 7]) - int(
                    times_strings[i * 10 + 6])
                for j in range(3, len(trains), 4):
                    if str(trains[j]) == str(trains_for_string[i]):
                        weight = int(trains[j-3])
                        time = int(trains[j-2])
                        break
                    else:
                        continue
                P_lb = e_br * ((time_racing + time_slowdown) * score_ost[i] + time_promej) / 60
                P_rz = 3.8 * weight * (V_x ** 2) * alpha * score_ost[i] * (10 ** (-6))
                P_lok = e_lok * ((time_racing + time_slowdown) * score_ost[i] + time_promej) / 60
                P_p = e_p * ((time_racing + time_slowdown) * score_ost[i] + time_promej) / 60
                P_e = C_e * time_promej * H_e / 60
                #print("TT1 = ", int(times_strings[i * 10 + 1]), time)
                P_tex = (int(times_strings[i*10+1])-time) * (e_lok + e_p) / 60
                P_prom = P_lb + P_rz + P_lok + P_p + P_e
                P_prom_finally += P_prom
                P_tex_finally += P_tex
            else:
                for j in range(3, len(trains), 4):
                    if str(trains[j]) == str(trains_for_string[i]):
                        time = int(trains[j - 2])
                        break
                    else:
                        continue
                e_lok = 560.31
                e_p = 20.24
                #print("TT = ", int(times_strings[i * 10 + 1]),  time)
                P_tex = (int(times_strings[i * 10 + 1]) - time) * (e_lok + e_p) / 60
                P_prom = 0
                P_prom_finally += P_prom
                P_tex_finally += P_tex
            P_Finally = P_prom_finally + P_tex_finally
            #print("P_tex"+"№"+str(i)+"=", P_tex_finally)
            #print("P_prom =", P_prom_finally)
            #print("P_finally =", P_Finally)

        else:
            continue
    P_Finally = P_prom_finally + P_tex_finally
    #print("P_tex =", P_tex_finally)
    #print("P_prom =", P_prom_finally)
    print("P_finally =", P_Finally)

calculation(trains_for_string)
calculation(trains_for_string_0)


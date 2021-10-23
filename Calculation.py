from Create_string import times_strings, score_ost, trains_for_string_0
#from Creat_trains import trains
inputfile_activation_trains = "./data/activation_trains.txt"
activation_trains = str(open(inputfile_activation_trains, mode = 'r', encoding = 'latin_1').read().splitlines()[0])
if activation_trains == str(True):
    from Creat_trains import trains
elif activation_trains == str(False):
    from input_trains import trains_GID
    trains = trains_GID


time_t = 30
good_trains = []
P_prom_for_trains = []
P_tex_for_trains = []
k = 1
score_strings = len(times_strings)//10
score_ost_1 = score_ost.copy()
trains_for_strings_0 = trains_for_string_0.copy()
for u in range(1, len(times_strings), 10):
    for i in range(1, len(trains), 4):
        if int(times_strings[u]) >= int(trains[i])+time_t:
            good_trains.append("№-"+str((u-1)//10))
            good_trains.extend(trains[i-1:i+3])
            k += 1
        else:
            continue
score_trains_str = []

for u in range (1, len(times_strings), 10):
    score_trains_str.append(good_trains.count('№-' + str(u//10)))

#print("score_trains_str", score_trains_str)
print("trains = ", trains)
"""==========Формирование массивов весов пездов, нулевого массива с поездами бля ниток, и ниток возмжных для использования============="""
strings_for_trains = []
trains_order = []
trains_for_strings = []

weights =[]
for u in range (0, len(trains)//4, 1):
    weights.append(trains[u*4])
    for i in range (1, len(times_strings), 10):
        if u == 0:
            trains_for_strings.append(0)

        if int(trains[u*4+1])+time_t <= int(times_strings[i]):
            strings_for_trains.append(1)
        else:
            strings_for_trains.append(0)
print("strings_for_trains", strings_for_trains)
#print(score_ost)
"""=========================Формирование массива trains_for_strings распределения пездов между нитками==========================="""
for y in range (0, len(trains)//4, 1):
    u = weights.index(max(weights))
    for i in range (0, score_strings, 1):
        if score_ost_1[i] != 100:
            if score_ost_1[i] == min(score_ost_1[i:score_strings]):
                if strings_for_trains[u*score_strings+i] == 1:
                    if trains_for_strings[i] == 0:
                        del trains_for_strings[i]
                        del score_ost_1[i]
                        trains_for_strings.insert(i, '№-' + str(u))
                        score_ost_1.insert(i, 100)
                        break
                    else:
                        continue
                else:
                    continue
            else:
                continue
        else:
            continue
    del weights[u]
    weights.insert(u, 0)

for u in range (0, score_strings, 1):
    if score_trains_str[u] != 0 and score_ost[u] != 0 and trains_for_strings[u] == 0:
        del trains_for_strings[u]
        trains_for_strings.insert(u, 1)
    else:
        continue


for u in range (0,score_strings, 1):
    if trains_for_strings_0[u] != 0:
        i = trains.index(trains_for_strings_0[u])
        del trains_for_strings_0[u]
        trains_for_strings_0.insert(u, '№-' + str((i-3)//4))

"""================Расчет P_prom_for_trains расходов по промежуточным станциям для каждого поезда и каждой нитки ================"""
for i in range (0, score_strings, 1):
    for u in range (0, len(trains)//4, 1):
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
            weight = int(trains[u * 4])
            P_lb = e_br * ((time_racing + time_slowdown) * score_ost[i] + time_promej) / 60
            P_rz = 3.8 * weight * (V_x ** 2) * alpha * score_ost[i] * (10 ** (-6))
            P_lok = e_lok * ((time_racing + time_slowdown) * score_ost[i] + time_promej) / 60
            P_p = e_p * ((time_racing + time_slowdown) * score_ost[i] + time_promej) / 60
            P_e = C_e * time_promej * H_e / 60
            P_prom = P_lb + P_rz + P_lok + P_p + P_e
        else:
            P_prom = 0

        P_prom_for_trains.append(P_prom)
"""for i in range (0, score_strings, 1):
    for u in range (0, len(trains)//4, 1):
        #if score_trains_str[i] != 0:
        if strings_for_trains[u*len(trains)//4+i] != 0:
            e_lok = 560.31
            e_p = 20.24
            time = int(times_strings[i * 10 + 1])
            if (u + i + 1) >= score_strings:
                d = score_strings - i - 2
            else:
                d = u+1
            P_tex = (int(times_strings[(i+d) * 10 + 1]) - time) * (e_lok + e_p) / 60
        else:
            P_tex = 0
        P_tex_for_trains.append(P_tex)"""


for u in range (0, score_strings, 1):
    e_lok = 560.31
    e_p = 20.24
    if u != score_strings-1:
        P_tex = (int(times_strings[(u+1) * 10 + 1])-int(times_strings[u * 10 + 1]))* (e_lok + e_p) / 60
    else:
        P_tex = 10 * (e_lok + e_p) / 60
    P_tex_for_trains.append(P_tex)

#print("trains_for_strings = ", trains_for_strings)
trains_for_strings_F = trains_for_strings.copy()
print("P_tex_for_trains", P_tex_for_trains)

def formation_trains_for_strings_F ():
    for u in range (score_strings-1, 1, -1):
        summa_P_tex = 0
        if trains_for_strings_F[u] == 1:
            for i in range (0, score_trains_str[u], 1):
                if trains_for_strings_F[0:u].count('№-' + str(i)) == 0 and trains_for_strings_F.count('№-' + str(i)) == 1:
                    p = trains_for_strings_F.index('№-' + str(i))
                    for y in range (u, p, 1):
                        summa_P_tex += P_tex_for_trains[y]
                    #if P_prom_for_trains[u*len(trains)//4+i] <= P_prom_for_trains[p*len(trains)//4+i] +P_tex_for_trains[u*len(trains)//4+(p-u)]:
                    if P_prom_for_trains[u * len(trains) // 4 + i] <= P_prom_for_trains[p * len(trains) // 4 + i] + summa_P_tex:
                        del trains_for_strings_F[u]
                        trains_for_strings_F.insert(u, '№-' + str(i))
                        del trains_for_strings_F[p]
                        trains_for_strings_F.insert(p, 1)
                        break
                    else:
                        continue
                else:
                    continue
        else:
            continue


P_Finally1 = []
P_tex1 = []
P_prom1 = []
def calculation (trains_for_string):
    P_tex_finally = 0
    P_prom_finally = 0
    #P_Finally = 0
    for i in range (0, len(trains_for_string), 1):
        if str(trains_for_string[i]) != str(0) and str(trains_for_string[i]) != str(1):
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
                for j in range(0, len(trains)//4, 1):
                    if '№-'+str(j) == str(trains_for_string[i]):
                        weight = int(trains[j*4])
                        time = int(trains[j*4+1])
                        break
                    else:
                        continue
                P_lb = e_br * ((time_racing + time_slowdown) * score_ost[i] + time_promej) / 60
                P_rz = 3.8 * weight * (V_x ** 2) * alpha * score_ost[i] * (10 ** (-6))
                P_lok = e_lok * ((time_racing + time_slowdown) * score_ost[i] + time_promej) / 60
                P_p = e_p * ((time_racing + time_slowdown) * score_ost[i] + time_promej) / 60
                P_e = C_e * time_promej * H_e / 60
                P_tex = (int(times_strings[i*10+1])-time) * (e_lok + e_p) / 60
                P_prom = P_lb + P_rz + P_lok + P_p + P_e
                P_prom_finally += P_prom
                P_tex_finally += P_tex
            else:
                for j in range(0, len(trains)//4, 1):
                    if '№-'+str(j) == str(trains_for_string[i]):
                        time = int(trains[j*4+1])
                        break
                    else:
                        continue
                e_lok = 560.31
                e_p = 20.24
                P_tex = (int(times_strings[i * 10 + 1]) - time) * (e_lok + e_p) / 60
                P_prom = 0
                P_prom_finally += P_prom
                P_tex_finally += P_tex
            #P_Finally = P_prom_finally + P_tex_finally
            #print("P_tex"+"№"+str(i)+"=", P_tex_finally)
            #print("P_prom =", P_prom_finally)
            #print("P_finally =", P_Finally)
            P_tex1.append(P_tex)
            P_prom1.append(P_prom)

        else:
            P_tex1.append(0)
            P_prom1.append(0)
            continue
    P_Finally = P_prom_finally + P_tex_finally
    print("P_tex =", P_tex_finally)
    print("P_prom =", P_prom_finally)
    print("P_finally =", P_Finally)
    P_Finally1.append(P_prom_finally)
    P_Finally1.append(P_tex_finally)
    P_Finally1.append(P_Finally)
    #print(P_tex1)
    #print(P_prom1)

formation_trains_for_strings_F()
#calculation(trains_for_strings_F)

for u in range (0, 2000, 1):
    formation_trains_for_strings_F()
def revers (trains_for_strings):
    for u in range (0, score_strings, 1):
        if trains_for_strings[u] != 0 and trains_for_strings[u] != 1:
            for i in range (0, len(trains)//4, 1):
                if '№-' + str(i) == trains_for_strings[u]:
                    del trains_for_strings[u]
                    trains_for_strings.insert(u, trains[i*4+3])
    #print(trains_for_strings)

#calculation(trains_for_strings)
calculation(trains_for_strings_0)
calculation(trains_for_strings_F)
revers(trains_for_strings_F)
revers(trains_for_strings_0)
#print("trains_for_strings = ", trains_for_strings)
print("trains_for_strings_F = ", trains_for_strings_F)
#print(trains_for_strings_0)
print(P_Finally1)
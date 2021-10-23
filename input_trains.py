import xlrd,datetime, re
data_trains = xlrd.open_workbook('./data/fact_gruz.xls')
sheet = data_trains.sheet_by_index(0)

trains_GID_0 = []
row_score = sheet.nrows

textlookfor = r"\d{2}\:\d{2}\:\d{2}"
textlookfor_1 = r"\d{2}"


for i in range (1, row_score, 1):

    if int(float(str(sheet.cell(rowx=i, colx=2)).replace("number:",""))) == int(83360):
        if int(float(str(sheet.cell(rowx=i, colx=3)).replace("number:","")))/2 == int(
            float(str(sheet.cell(rowx=i, colx=3)).replace("number:","")))//2:
            trains_GID_0.append(int(float(str(sheet.cell(rowx=i, colx=10)).replace("number:",""))))
            a1 = sheet.cell_value(rowx=i, colx=4)
            a1_as_datetime = str(datetime.datetime(*xlrd.xldate_as_tuple(a1, data_trains.datemode)))
            a1_date = re.findall(textlookfor_1, str(re.findall(textlookfor, a1_as_datetime)))
            time = int(a1_date[0]) * 60 + int(a1_date[1])
            trains_GID_0.append(time)
            if int(float(str(sheet.cell(rowx=i, colx=3)).replace("number:",""))) > 1000 and  int(
                float(str(sheet.cell(rowx=i, colx=3)).replace("number:",""))) < 2000:

                trains_GID_0.append(2)
            elif int(float(str(sheet.cell(rowx=i, colx=3)).replace("number:",""))) > 1000:
                trains_GID_0.append(1)
            trains_GID_0.append(str(int(float(str(sheet.cell(rowx=i, colx=3)).replace("number:","")))))
#print(trains_GID_0)
trains_GID = []
times_trains = []
for i in range (1, len(trains_GID_0), 4):
    times_trains.append(trains_GID_0[i])
for i in range (0, len(times_trains), 1):
    if min(times_trains) != 3000:
        for u in range (0, len(times_trains), 1):
            if times_trains[u] == min(times_trains):
                trains_GID.extend(trains_GID_0[u*4:u*4+4])
                del times_trains[u]
                times_trains.insert(u, 3000)
                #print(times_trains)
                break
            else:
                continue
print("!!! = ", len(trains_GID), trains_GID)


a1 = sheet.cell_value(rowx=2, colx=4)
a1_as_datetime = str(datetime.datetime(*xlrd.xldate_as_tuple(a1, data_trains.datemode)))
a1_date = re.findall(textlookfor_1, str(re.findall(textlookfor, a1_as_datetime)))
time = int(a1_date[0])*60 + int(a1_date[1])
if 2160/2 > 2160//2:
    print("!!!")
print ( a1_as_datetime)
print(int(float(str(sheet.cell(rowx=2, colx=2)).replace("number:",""))))
print(a1_date)
print(time)

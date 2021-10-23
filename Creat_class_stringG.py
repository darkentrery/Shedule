Gtravel_time1_2 = 35
Gtravel_time2_3 = 30
Gtravel_time3_4 = 38
Gtravel_time4_5 = 25
Gtravel_time = [35, 30, 38, 25]
class StringG ():
    def __init__(self, numero_string, St1_arrival, St1_departure, St2_arrival, St2_departure, St3_arrival, St3_departure,
                 St4_arrival, St4_departure, St5_arrival, St5_departure, Gtravel_time1_2, Gtravel_time2_3, Gtravel_time3_4,
                 Gtravel_time4_5):
        self.numero_string = numero_string
        self.St1_arrival = St1_arrival
        self.St1_departure = St1_departure
        self.St2_arrival = St2_arrival
        self.St2_departure = St2_departure
        self.St3_arrival = St3_arrival
        self.St3_departure = St3_departure
        self.St4_arrival = St4_arrival
        self.St4_departure = St4_departure
        self.St5_arrival = St5_arrival
        self.St5_departure = St5_departure
        self.Gtravel_time1_2 = Gtravel_time1_2
        self.Gtravel_time2_3 = Gtravel_time2_3
        self.Gtravel_time3_4 = Gtravel_time3_4
        self.Gtravel_time4_5 = Gtravel_time4_5

    def create_numero_string (self):
        num_1 = random.randint(1, 9)
        num_2 = random.randint(0, 9)
        num_3 = random.randint(0, 9)
        num_4 = random.randint(0, 9)
        if num_4%2 == 0:
            num_4 = num_4
        else:
            num_4 += 1
        if num_4 == 10:
            num_4 = 0
        self.numero_string = (str (num_1) + str (num_2) + str (num_3) + str (num_4))

    def show_numero_string (self):
        show_numero = (self.numero_string)
        print("Время прибытия поезда №" + show_numero)

    def creat_arrival_depature (self):
#        self.St1_arrival = 0
#        self.St1_departure = St1_departure
        self.St2_arrival = self.St1_departure + Gtravel_time1_2
        self.St2_departure = self.St2_arrival
        self.St3_arrival = self.St2_departure + Gtravel_time2_3
        self.St3_departure = self.St3_arrival
        self.St4_arrival = self.St3_departure + Gtravel_time3_4
        self.St4_departure = self.St4_arrival
        self.St5_arrival = self.St4_departure + Gtravel_time4_5
        self.St5_departure = self.St5_arrival
        #inputfile = 'D:\Python\Shedule\ParametrsG.txt'
        inputfile = "./data/ParametrsG.txt"
        myfile = open (inputfile, mode = 'w', encoding = 'latin_1')
        myfile.write(str(self.St1_arrival) + "\n")
        myfile.write(str(self.St1_departure) + "\n")
        myfile.write(str (self.St2_arrival) + "\n")
        myfile.write(str (self.St2_departure) + "\n")
        myfile.write(str (self.St3_arrival) + "\n")
        myfile.write(str (self.St3_departure) + "\n")
        myfile.write(str (self.St4_arrival) + "\n")
        myfile.write(str (self.St4_departure) + "\n")
        myfile.write(str (self.St5_arrival) + "\n")
        myfile.write(str (self.St5_departure) + "\n")
        myfile.close()

    def show_arrival_depature (self):
        show_arrival5 = (self.St5_arrival)
        print("Время прибытия на станция 5 = " + str (show_arrival5))
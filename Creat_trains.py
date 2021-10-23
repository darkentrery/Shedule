import random

class trains():
    def __init__(self, weight, time_arrival, priority, number):
        self.weight = weight
        self.time_arrival = time_arrival
        self.priority = priority
        self.number = number

    def creat_trains(self):
        interval = 10
        x =[]
        y = []
        while self.time_arrival < 480:
            self.weight = random.randint (0, 6300)
            self.time_arrival = self.time_arrival + interval + random.randint(0, 20)
            self.priority = random.randint(1, 3)
            if self.priority == 1:
                num_1 = 1
            elif self.priority == 2:
                num_1 = 2
            else:
                num_1 = 3
            num_2 = random.randint(0, 9)
            num_3 = random.randint(0, 9)
            num_4 = random.randint(0, 9)
            if num_4 % 2 == 0:
                num_4 = num_4
            else:
                num_4 += 1
            if num_4 == 10:
                num_4 = 0
            self.number = (str(num_1) + str(num_2) + str(num_3) + str(num_4))
            x.append(self.weight)
            x.append(self.time_arrival)
            x.append(self.priority)
            x.append(self.number)
            #print(x)
        global trains
        trains = x
        return trains
        print("trains=", trains)


a = trains(0, 0, 0, 0)
a.creat_trains()
#print("train1111= ", trains)
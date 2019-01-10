import random
import math
from EvaluationMock import Distance
from BasicClasses import Track


def RandomGenerate(number, board_size_x, board_size_y,time):
    file = open('Tracks2.txt', 'w')
    max = 0
    total_time = 0
    for i in range(1, number):
        track = Track(0,0,0,0,0,0,0)
        track.ID = random.randint(0, 10000)
        track.starting_point[0] = random.randint(1, board_size_x)
        track.starting_point[1] = random.randint(1, board_size_y)
        track.ending_point[0] = random.randint(1, board_size_x)
        track.ending_point[1] = random.randint(1, board_size_y)
        track.start_time = random.randint(0, time)

        money = math.floor((random.random()+0.2) * math.floor(
        abs(track.ending_point[1] - track.starting_point[1]) + abs(track.ending_point[0] - track.starting_point[0])))
        max = max + money
        total_time += Distance(track.starting_point,track.ending_point)

        file.write("ID:" + str(track.ID) + " Start:" + str(track.starting_point[0]) + "," + str(
            track.starting_point[1]) + " Finish:" + str(track.ending_point[0]) + "," + str(
            track.ending_point[1]) + " Time:" + str(track.start_time
                                                    ) + " Money:" + str(money) + "\n")
    print(max,total_time)

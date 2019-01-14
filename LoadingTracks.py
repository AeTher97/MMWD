import re
from BasicClasses import Track,Cab
from EvaluationMock import Distance

class LoadTracksFromFile:
    @staticmethod
    def Load(filepath):
        track_list = []
        File = open(filepath,"r")
        for Line in File:
            outputs = Line.split(' ')

            Start_outputs = outputs[1].split(',')
            End_outputs = outputs[2].split(',')
            Time_output = outputs[3]
            Money_output = outputs[4]
            Punishment_output = outputs[5]

            ID = re.search(r"(?P<ID>[\d]+)",outputs[0]).group()
            Start_a = int(re.search(r"(?P<ID>[\d]+)", Start_outputs[0]).group())
            Start_b = int(re.search(r"(?P<ID>[\d]+)", Start_outputs[1]).group())
            Finish_a = int(re.search(r"(?P<ID>[\d]+)", End_outputs[0]).group())
            Finish_b = int(re.search(r"(?P<ID>[\d]+)", End_outputs[1]).group())
            Time = int(re.search(r"(?P<ID>[\d]+)",Time_output).group())
            Money = int(re.search(r"(?P<ID>[\d]+)", Money_output).group())
            Punishment = int(re.search(r"(?P<ID>[\d]+)", Punishment_output).group())

            track_list.append(Track(ID,Start_a,Start_b,Finish_a,Finish_b,Time,Money,Punishment))
        total_money = 0
        total_time = 0
        latest_finish = 0
        total_puhishment = 0
        for track in track_list:
            total_money += track.reward
            total_puhishment += track.punishment
            total_time += Distance(track.starting_point,track.ending_point)
            if track.start_time + Distance(track.starting_point,track.ending_point) > latest_finish:
                latest_finish = track.start_time + Distance(track.starting_point,track.ending_point)

        print("Total money to make: " + str(total_money) + " Total punishment: "+ str(total_puhishment)+ " Total time: " + str(total_time) + " Latest Finish: " + str(latest_finish))
        return track_list

class LoadCabsFromFile:
    @staticmethod
    def Load(filepath):
        cabs_list = []
        File = open(filepath, "r")
        for Line in File:
            outputs = Line.split(' ')

            Start_outputs = outputs[1].split(',')


            ID = re.search(r"(?P<ID>[\d]+)", outputs[0]).group()
            Start_a = int(re.search(r"(?P<ID>[\d]+)", Start_outputs[0]).group())
            Start_b = int(re.search(r"(?P<ID>[\d]+)", Start_outputs[1]).group())



            cabs_list.append(Cab(ID, [Start_a, Start_b]))

        return cabs_list
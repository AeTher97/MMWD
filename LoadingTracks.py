import re
from BasicClasses import Track

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

            ID = re.search(r"(?P<ID>[\d]+)",outputs[0]).group()
            Start_a = int(re.search(r"(?P<ID>[\d]+)", Start_outputs[0]).group())
            Start_b = int(re.search(r"(?P<ID>[\d]+)", Start_outputs[1]).group())
            Finish_a = int(re.search(r"(?P<ID>[\d]+)", End_outputs[0]).group())
            Finish_b = int(re.search(r"(?P<ID>[\d]+)", End_outputs[1]).group())
            Time = int(re.search(r"(?P<ID>[\d]+)",Time_output).group())
            Money = int(re.search(r"(?P<ID>[\d]+)", Money_output).group())

            track_list.append(Track(ID,Start_a,Start_b,Finish_a,Finish_b,Time,Money))

        return track_list
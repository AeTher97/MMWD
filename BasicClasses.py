import random


class Track:
    def __init__(self,_ID,_starting_point_a,_starting_point_b,_ending_point_a,_ending_point_b):
        self.ID = _ID
        self.starting_point = [_starting_point_a,_starting_point_b]
        self.ending_point = [_ending_point_a,_ending_point_b]


    def GetStartingPoint(self):
        return self.starting_point

    def GetEndingPOint(self):
        return self.ending_point

    def SetStartingPoint(self,starting_point_a,starting_point_b):
        self.starting_point = [starting_point_a,starting_point_b]

class Cab:
    def __init__(self,_ID,_start_point,_ending_point):
        self.Tracks = []
        self.ID = _ID
        self.start_point = _start_point
        self.ending_point = _ending_point

    def AddTrack(self,Track):
        self.Tracks.append(Track)

    def ShowTracks(self):
        for item in self.Tracks:
            print("ID:"+str(item.ID)+" Start: " + str(item.starting_point),"Finish: " + str(item.ending_point))

def WeightedChoice(objects, weights):
    totals = []
    running_total = 0.0

    for w in weights:
        running_total += w
        totals.append(running_total)

    rnd = random.random() * running_total

    for i, total in enumerate(totals):
        if rnd < total:
            return objects[i]
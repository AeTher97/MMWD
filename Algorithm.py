import copy

from BasicClasses import Cab, WeightedChoice
from enum import Enum
import random
from SelectionFunctions import RankingSelection, Roulette_wheel_selection


### Selection methods
# 1 - Ranking method
# 2 - Roulette wheel method
selection_functions = [RankingSelection, Roulette_wheel_selection]

class Config(Enum):
    # Problem Data
    Number_of_cabs = 3
    # New generation creation
    Number_of_initial_solutions = 20
    Number_of_children = 30
    Selection_method = 1
    Chance_of_crossing = 1
    Chance_of_mutation = 20
    # Mutation weights
    Mutation_1 = 1
    Mutation_2 = 10
    Mutation_3 = 30
    # Cross weights
    Cross_1 = 1



class Solution:
    def __init__(self, number_of_cabs):
        self.number_of_cabs = number_of_cabs
        self.Cabs = []
        self.fitness = 0
        self.quality_factors = []

    def AddCab(self, Cab):
        self.Cabs.append(Cab)


class Algorithm:
    def __init__(self, _list_of_tracks, _board_size_x, _board_size_y, _number_of_cabs=Config.Number_of_cabs.value):
        self.selection_function = selection_functions[Config.Selection_method.value-1]
        self.solutions = []
        self.number_of_cabs = _number_of_cabs
        self.list_of_tracks = _list_of_tracks
        self.board_size_x = _board_size_x
        self.board_size_y = _board_size_y
        self.GenereateBasicSolutions(Config.Number_of_initial_solutions.value)

    def GenereateBasicSolutions(self, number):

        for i in range(0, number):
            solution = Solution(self.number_of_cabs)
            for j in range(1, self.number_of_cabs + 1):
                solution.AddCab(Cab(j, [random.randint(1, self.board_size_x), random.randint(1, self.board_size_y)]))
            for item in self.list_of_tracks:
                choosed_cab = random.randint(0, self.number_of_cabs - 1)
                solution.Cabs[choosed_cab].AddTrack(item)

            self.solutions.append(solution)

    def ShowSolution(self):
        i = 1
        for solution in self.solutions:

            print("SOLUTION: ", str(i))
            for item in solution.Cabs:
                print("Cab " + str(item.ID) + " Start point:" + str(item.start_point))
                item.ShowTracks()
                print("\n")
            i = i + 1




    def NewGeneration(self):
        result = self.selection_function(self.solutions, self.list_of_tracks)
        parents = result[0]
        untouchable = result[1]
        for solution in untouchable:
            parents.append(copy.deepcopy(solution))

        Mutation_object = Mutation()
        Cross_object = Crossing()
        children = []
        weights = []
        for parent in parents:
            weights.append(1)


        for i in range(0,Config.Number_of_children.value):
            solution = parents[i%len(parents)]
            choosed_mutation = Mutation_object.GetMutation()
            choosed_crossing = Cross_object.GetCrossing()
            operations = [choosed_mutation,choosed_crossing]
            picked_operation = WeightedChoice(operations,[Config.Chance_of_mutation.value,Config.Chance_of_crossing.value])
            if picked_operation == choosed_crossing:
                solution_b = WeightedChoice(parents,weights)
                while (solution_b == solution):
                    solution_b = WeightedChoice(parents, weights)
                new_solution = choosed_crossing.Cross(solution,solution_b)
                CompleteSolution(new_solution,self.list_of_tracks)
                children.append(new_solution)
            else:
                new_solution = choosed_mutation.Mutate(solution)
                CompleteSolution(new_solution,self.list_of_tracks)
                children.append(new_solution)
        for solution in untouchable:
            children.append(solution)

        self.solutions = children

def CompleteSolution(solution,list_of_tracks):
    total_list = copy.deepcopy(list_of_tracks)

    for cab in solution.Cabs:
        list_to_remove = []
        for track in cab.Tracks:
            try:
                total_list.remove(track)
            except ValueError:
                list_to_remove.append(track)

        for track in list_to_remove:
            cab.Tracks.remove(track)

    for track in total_list:
        choosed_cab = random.randint(0, solution.number_of_cabs - 1)
        solution.Cabs[choosed_cab].AddTrack(track)
    return solution

class Crossing_1:
    weight = Config.Cross_1.value

    def Cross(self, solution_a, solution_b):

        used_cabs = []
        new_solution = Solution(solution_b.number_of_cabs)
        for cab_a in solution_a.Cabs:
            chosen_cab = random.randint(0, len(solution_b.Cabs) - 1)
            while (chosen_cab in used_cabs):
                chosen_cab = random.randint(0, len(solution_b.Cabs) - 1)

            used_cabs.append(chosen_cab)
            cab_b = solution_b.Cabs[chosen_cab]
            if (len(cab_a.Tracks) > 1):
                cut_cab_a = random.randint(0, len(cab_a.Tracks) - 1)
            else:
                cut_cab_a = 0
            if (len(cab_b.Tracks) > 1):
                cut_cab_b = random.randint(0, len(cab_b.Tracks) - 1)
            else:
                cut_cab_b = 0

            #print("mixing cab " + str(cab_a.ID) + " with cab " + str(cab_b.ID) + " in points a: " + str(
            #    cut_cab_a) + " b: " + str(cut_cab_b))  # cos
            temp_a = cab_a.Tracks[:cut_cab_a] + cab_b.Tracks[cut_cab_b:]
            temp_b = cab_b.Tracks[:cut_cab_b] + cab_a.Tracks[cut_cab_a:]
            new_cab = Cab(cab_a.ID, cab_a.start_point)
            new_cab.Tracks = temp_a
            new_solution.Cabs.append(new_cab)


        return new_solution

class Mutation_1:
    weight = Config.Mutation_1.value

    def Mutate(self,solution):
        new_solution = copy.deepcopy(solution)
        cab = random.choice(new_solution.Cabs)
        random.shuffle(cab.Tracks)
        return new_solution

class Mutation_2:
    weight = Config.Mutation_2.value

    def Mutate(self,solution):
        new_solution = copy.deepcopy(solution)
        cab_1 = random.choice(new_solution.Cabs)
        cab_2 = random.choice(new_solution.Cabs)
        while cab_1 == cab_2:
            cab_2 = random.choice(new_solution.Cabs)
        if(len(cab_1.Tracks)>0 and len(cab_2.Tracks)>0):
            track_1 = random.choice(cab_1.Tracks)
            track_2 = random.choice(cab_2.Tracks)

            cab_1.Tracks.append(track_2)
            cab_2.Tracks.append(track_1)

            cab_1.Tracks.remove(track_1)
            cab_2.Tracks.remove(track_2)

        return new_solution

class Mutation_3:
    weight = Config.Mutation_3.value

    def Mutate(self,solution):
        new_solution = copy.deepcopy(solution)
        cab = random.choice(new_solution.Cabs)
        if(len(cab.Tracks)>=2):
            track_number = random.randint(0,len(cab.Tracks)-2)
            if(cab.Tracks[track_number].start_time > cab.Tracks[track_number+1].start_time):
                cab.Tracks[track_number] , cab.Tracks[track_number+1] =  cab.Tracks[track_number+1] , cab.Tracks[track_number]

        return new_solution


class Mutation:
    def __init__(self):
        self.list_of_mutations = []
        self.list_of_mutations.append(Mutation_1())
        self.list_of_mutations.append(Mutation_2())
        self.list_of_mutations.append(Mutation_3())
        # add new mutations

    def GetMutation(self):
        weights = []
        for object in self.list_of_mutations:
            weights.append(object.weight)
        return WeightedChoice(self.list_of_mutations,weights)


class Crossing:
    def __init__(self):
        self.list_of_crossings = []
        self.list_of_crossings.append(Crossing_1())
        # add new crossings

    def GetCrossing(self):
        weights = []
        for object in self.list_of_crossings:
            weights.append(object.weight)

        return WeightedChoice(self.list_of_crossings, weights)




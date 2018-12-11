from BasicClasses import Cab
import random
import copy
number_of_initial_solutions = 3
number_of_solutions_to_carry = 10
number_of_solutions_to_pass = 2

class Solution:
    def __init__(self,_number_of_cabs):
        self.number_of_cabs = _number_of_cabs
        self.Cabs = []
        self.fitness = 0

    def AddCab(self,Cab):
        self.Cabs.append(Cab)

class Algorithm:
    def __init__(self,_number_of_cabs,_list_of_tracks,_board_size_x,_board_size_y):
        self.solutions = []
        self.number_of_cabs = _number_of_cabs
        self.list_of_tracks = _list_of_tracks
        self.board_size_x = _board_size_x
        self.board_size_y = _board_size_y
        self.GenereateBasicSolutions(number_of_initial_solutions)

    def GenereateBasicSolutions(self,number):

        for i in range(0,number):
            solution = Solution(self.number_of_cabs)
            for j in range(1, self.number_of_cabs + 1):
                solution.AddCab(Cab(j,random.randint(1,self.board_size_x),random.randint(1,self.board_size_y)))
            for item in self.list_of_tracks:
                choosed_cab = random.randint(0,self.number_of_cabs-1)
                solution.Cabs[choosed_cab].AddTrack(item)

            self.solutions.append(solution)


    def ShowSolution(self):
        i = 1
        for solution in self.solutions:

            print("SOLUTION: ",str(i))
            for item in solution.Cabs:
                print("Cab " + str(item.ID)+" Start point:"+str(item.start_point)+","+str(item.ending_point))
                item.ShowTracks()
                print("\n")
            i = i+1

    def CompleteSolution(self,solution):
        total_list = copy.copy(self.list_of_tracks)

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

    def Cross(self,solution_a,solution_b):
        if solution_a.number_of_cabs > solution_b.number_of_cabs:
            solution_b.number_of_cabs = solution_b.number_of_cabs+1
        elif solution_b.number_of_cabs > solution_a.number_of_cabs:
            solution_a.number_of_cabs = solution_a.number_of_cabs+1
        used_cabs = []
        new_solution = Solution(solution_b.number_of_cabs)
        for cab_a in solution_a.Cabs:
            chosen_cab = random.randint(0, len(solution_b.Cabs) - 1)
            while(chosen_cab in used_cabs):
                chosen_cab = random.randint(0, len(solution_b.Cabs) - 1)

            used_cabs.append(chosen_cab)
            cab_b = solution_b.Cabs[chosen_cab]
            if(len(cab_a.Tracks)>1):
                cut_cab_a = random.randint(0,len(cab_a.Tracks)-1)
            else:
                cut_cab_a = 0
            if(len(cab_b.Tracks)>1):
                cut_cab_b = random.randint(0,len(cab_b.Tracks)-1)
            else:
                cut_cab_b = 0


            print("mixing cab " + str(cab_a.ID) + " with cab " + str(cab_b.ID) + " in points a: " + str(
                cut_cab_a) + " b: " + str(cut_cab_b)) #cos
            temp_a = cab_a.Tracks[:cut_cab_a] + cab_b.Tracks[cut_cab_b:]
            temp_b = cab_b.Tracks[:cut_cab_b] + cab_a.Tracks[cut_cab_a:]
            new_cab = Cab(cab_a.ID,cab_a.start_point,cab_a.ending_point)
            new_cab.Tracks = temp_a
            new_solution.Cabs.append(new_cab)

        self.CompleteSolution(new_solution)
        return copy.deepcopy(new_solution)

    def EvaluateSolutions(self):
        for solution in self.solutions:
            solution.fitness = 0 # TODO run evaluation function
        self.solutions.sort(key=lambda x: x.fitness)
        self.solutions = self.solutions[:number_of_solutions_to_pass]

    def NewGeneration(self):

        new_population = []
        for i in range(0,number_of_solutions_to_carry):
            solution_to_cross_a = random.randint(0,len(self.solutions)-1)
            solution_to_cross_b = random.randint(0,len(self.solutions)-1)
            while(solution_to_cross_b == solution_to_cross_a):
                solution_to_cross_b = random.randint(0, len(self.solutions) - 1)
            print("odpalamto " + str(i+1) +" " +str(solution_to_cross_a+1) +" " +str(solution_to_cross_b+1))

            new_population.append(self.Cross(self.solutions[solution_to_cross_a],self.solutions[solution_to_cross_b]))

        self.solutions = new_population




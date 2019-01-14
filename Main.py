import copy
import math
from time import sleep
import progressbar
import os
from ProgressBar import print_progress_bar
from Algorithm import Algorithm
from Algorithm import Mutation
import time
from LoadingTracks import LoadTracksFromFile,LoadCabsFromFile
from EvaluationMock import EvaluateTaxi,EvaluateSolution
from RandomGenerator import RandomGenerate

def clear():
    os.system('cls')


#RandomGenerate(20,30,30,2000)
iterations = 1000


cabs_list = LoadCabsFromFile.Load('Cabs.txt')
track_list = LoadTracksFromFile.Load('Tracks2.txt')
bar = progressbar.ProgressBar(max_value=iterations).start()
cos = Algorithm(track_list,cabs_list,50,50)


for i in range(0,iterations):

    cos.NewGeneration()

    if(i%10 == 0):
        wynik = copy.deepcopy(cos.solutions)

        bar.update(i + 1)

        for solution in wynik:
            EvaluateSolution(solution, track_list)
        wynik.sort(key=lambda x: x.fitness, reverse=True)


        solution = wynik[0]
        best = cos.best_solution

        print("\n[Money [Idle time, Time with passenger, Time traveligh between tracks, Time busy, Distances to trascks, Overall distance, Tracks completed]" + str([solution.fitness, solution.quality_factors]))
        if best!= None:
            print("Best" +  str([best.fitness, best.quality_factors]))
    #for solution in cos.solutions:
        #print([solution.fitness, solution.quality_factors])
    #print("iteration")
bar.finish()
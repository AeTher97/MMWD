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
import matplotlib.pyplot as plt
from RandomGenerator import RandomGenerate

def clear():
    os.system('cls')



#RandomGenerate(20,30,30,2000)
iterations = 100

x = []
best_solution_data = []
average_data = []

cabs_list = LoadCabsFromFile.Load('Cabs.txt')
track_list = LoadTracksFromFile.Load('Tracks2.txt')
bar = progressbar.ProgressBar(max_value=iterations).start()
cos = Algorithm(track_list,cabs_list,50,50)
average_data = [[],[],[],[],[],[],[],[]]

for i in range(0,iterations):

    cos.NewGeneration()

    if(i%5 == 0):
        x.append(i)
        wynik = copy.deepcopy(cos.solutions)
        fitness_sum = 0
        bar.update(i + 1)

        for solution in wynik:
            EvaluateSolution(solution, track_list)
            fitness_sum += solution.fitness
        wynik.sort(key=lambda x: x.fitness, reverse=True)
        average_data[0].append(fitness_sum/len(wynik))
        i = 1
        for item in solution.quality_factors:
            average_data[i].append(item)
            i += 1

        solution = wynik[0]
        best = cos.best_solution
        best_solution_data.append(solution.fitness)
        print("\n[Money [Idle time, Time with passenger, Time traveligh between tracks, Time busy, Distances to trascks, Overall distance, Tracks completed]" + str([solution.fitness, solution.quality_factors]))
        if best!= None:
            print("Best" +  str([best.fitness, best.quality_factors]))




    #for solution in cos.solutions:
        #print([solution.fitness, solution.quality_factors])
    #print("iteration")
bar.finish()
cos.ShowSolution(best)



plt.plot(x,best_solution_data,label='Best solution')

plt.plot(x,average_data[0],label='Average solution fitness')
plt.legend(['Best solution Fitness','Average Fitness'])
plt.show()
plt.figure()
for i in range(1,len(average_data)):
    plt.plot(x,average_data[i])
plt.legend(['Idle time', 'Time with passenger', 'Time traveligh between tracks', 'Time busy', 'Distances to trascks', 'Overall distance', 'Tracks completed'])
plt.show()
input("Press Enter to continue...")
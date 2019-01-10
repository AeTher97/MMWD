import copy

from Algorithm import Algorithm
from Algorithm import Mutation
from BasicClasses import Cab,Track
from LoadingTracks import LoadTracksFromFile
from EvaluationMock import EvaluateTaxi,EvaluateSolution
from RandomGenerator import RandomGenerate


RandomGenerate(60,30,30,300)


track_list = LoadTracksFromFile.Load('Tracks2.txt')
cos = Algorithm(track_list,50,50)
for i in range(0,300):
    print(i)
    cos.NewGeneration()
    if(i%10 == 0):
        wynik = copy.deepcopy(cos.solutions)
        for solution in wynik:

            EvaluateSolution(solution, track_list)
        wynik.sort(key=lambda x: x.fitness, reverse=False)

        for solution in wynik:
            print([solution.fitness, solution.quality_factors])

    #for solution in cos.solutions:
        #print([solution.fitness, solution.quality_factors])
    #print("iteration")

import copy

import numpy as np
from EvaluationMock import EvaluateSolution
from BasicClasses import WeightedChoice
from enum import Enum


class Config(Enum):
    # Selection Funcions parameters
    Number_to_pass_ranking = 15
    Number_to_pass_roulette = 15
    Number_of_untouchable_solutions = 10


def RankingSelection(solutions, tracks, alg):

    for solution in solutions:
        EvaluateSolution(solution, tracks)


    solutions.sort(key=lambda x: x.fitness, reverse=True)
    if alg.best_solution != None:
        if(solutions[0].fitness > alg.best_solution.fitness):
            alg.best_solution = copy.deepcopy(solutions[0])
    else:
        alg.best_solution = copy.deepcopy(solutions[0])
    untouchable_solutions = solutions[:Config.Number_of_untouchable_solutions.value]


    new_generation = solutions[Config.Number_of_untouchable_solutions.value:Config.Number_to_pass_ranking.value+Config.Number_of_untouchable_solutions.value]

    return [new_generation, untouchable_solutions]


def Roulette_wheel_selection(solutions, tracks,alg):
    weights = []

    for solution in solutions:
        EvaluateSolution(solution, tracks)

    new_generation = []

    solutions.sort(key=lambda x: x.fitness, reverse=True)
    if alg.best_solution != None:
        if (solutions[0].fitness > alg.best_solution.fitness):
            alg.best_solution = copy.deepcopy(solutions[0])
    else:
        alg.best_solution = copy.deepcopy(solutions[0])
    untouchable_solutions = solutions[:Config.Number_of_untouchable_solutions.value]
    solutions = solutions[Config.Number_of_untouchable_solutions.value:]
    for solution in solutions:
        weights.append(solution.fitness)
    for i in range(1, Config.Number_to_pass_roulette.value):
        new_generation.append(WeightedChoice(solutions, weights))

    for solution in new_generation:
        if solution == None:
            new_generation.remove(solution)
    return [new_generation,untouchable_solutions]

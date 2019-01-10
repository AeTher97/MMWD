from EvaluationMock import EvaluateSolution
from BasicClasses import WeightedChoice
from enum import Enum


class Config(Enum):
    # Selection Funcions parameters
    Number_to_pass_ranking = 5
    Number_to_pass_roulette = 5
    Number_of_untouchable_solutions = 2


def RankingSelection(solutions, tracks):

    for solution in solutions:
        EvaluateSolution(solution, tracks)


    solutions.sort(key=lambda x: x.fitness, reverse=True)
    untouchable_solutions = solutions[:Config.Number_of_untouchable_solutions.value]
    new_generation = []

    new_generation = solutions[Config.Number_of_untouchable_solutions.value:Config.Number_to_pass_ranking.value+Config.Number_of_untouchable_solutions.value]

    return [new_generation, untouchable_solutions]


def Roulette_wheel_selection(solutions, tracks):
    weights = []
    i = 1
    for solution in solutions:
        solution.fitness = EvaluateSolution(solution, tracks)
        print("Solution " + str(i))
        print([solution.fitness,solution.quality_factors])
        weights.append(solution.fitness)
        i+= 1

    new_generation = []
    solutions.sort(key=lambda x: x.fitness, reverse=True)
    untouchable_solutions = solutions[:Config.Number_of_untouchable_solutions.value]
    solutions = solutions[Config.Number_of_untouchable_solutions:]

    for i in range(1, Config.Number_to_pass_roulette.value):
        new_generation.append(WeightedChoice(solutions, weights))

    return [new_generation,untouchable_solutions]

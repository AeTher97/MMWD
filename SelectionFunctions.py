from EvaluationMock import EvaluateSolution
from BasicClasses import WeightedChoice
from enum import Enum


class Config(Enum):
    # Selection Funcions parameters
    Number_to_pass_ranking = 5
    Number_to_pass_roulette = 5


def RankingSelection(solutions, tracks):
    for solution in solutions:
        EvaluateSolution(solution, tracks)  # TODO evalutaion

    solutions.sort(key=lambda x: x.fitness, reverse=True)

    new_generation = []

    new_generation = solutions[:Config.Number_to_pass_ranking.value]

    return new_generation


def Roulette_wheel_selection(solutions, tracks):
    weights = []

    for solution in solutions:
        solution.fitness = EvaluateSolution(solution, tracks)  # TODO evaluation
        weights.append(solution.fitness)

    new_generation = []

    for i in range(1, Config.Number_to_pass_roulette.value):
        new_generation.append(WeightedChoice(solutions, weights))

    return new_generation

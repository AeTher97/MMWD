import random
from BasicClasses import Cab


def EvaluateSolution(solution, tracks):
    fitness = 0
    solution.quality_factors = []
    iteration = 0

    for cab in solution.Cabs:
        quality = EvaluateTaxi(cab)
        fitness+=quality[0]
        if iteration == 0:
            solution.quality_factors = quality[1:]
        else:
            j = 0
            for z in solution.quality_factors:
                solution.quality_factors[j] += quality[j+1]
                j+=1
        iteration += 1
    solution.fitness = fitness



def EvaluateTaxi(cab):
    money_made = 0
    turn_number = 0
    riding_without_passenger = 0
    riding_with_passenger = 0
    busy_time = 0
    wait_time = 0
    overall_distance_to_target = 0
    distance_covered = 0
    tracks_completed = 0

    for track in cab.Tracks:
        if track.is_wait:

            turn_number += track.wait_time
            continue
        distance = Distance(cab.current_position,track.starting_point)
        overall_distance_to_target += distance
        if cab.current_position != track.starting_point and distance < track.start_time - turn_number:
            cab.current_track = None
            while (cab.current_position != track.starting_point):
                if (cab.current_position[0] < track.starting_point[0]):
                    cab.current_position[0] = cab.current_position[0] + 1
                    turn_number += 1
                    riding_without_passenger +=1
                    busy_time+=1
                elif (cab.current_position[0] > track.starting_point[0]):
                    cab.current_position[0] = cab.current_position[0] - 1
                    turn_number += 1
                    riding_without_passenger += 1
                    busy_time += 1
                if (cab.current_position[1] < track.starting_point[1]):
                    cab.current_position[1] = cab.current_position[1] + 1
                    turn_number += 1
                    riding_without_passenger += 1
                    busy_time += 1
                elif (cab.current_position[1] > track.starting_point[1]):
                    cab.current_position[1] = cab.current_position[1] - 1
                    turn_number += 1
                    riding_without_passenger += 1
                    busy_time += 1

            wait_time += track.start_time - turn_number
            turn_number = track.start_time
        elif cab.current_position == track.starting_point and track.start_time >= turn_number:
            turn_number += track.start_time - turn_number
            wait_time += track.start_time - turn_number
        elif track.start_time < turn_number:
            money_made -= track.punishment
            continue
        elif distance > track.start_time - turn_number:
            money_made -= track.punishment
            continue
        else:
            money_made -= track.punishment
            continue


        cab.current_track = track
        if turn_number == track.start_time and cab.current_track == track:
            money_made += track.reward
            tracks_completed += 1
        cab.current_track = track
        while (cab.current_position != track.ending_point):
            if (cab.current_position[0] < track.ending_point[0]):
                cab.current_position[0] += 1
                turn_number += 1
                riding_with_passenger += 1
                busy_time += 1
            elif (cab.current_position[0] > track.ending_point[0]):
                cab.current_position[0] -= 1
                turn_number += 1
                riding_with_passenger += 1
                busy_time += 1
            if (cab.current_position[1] < track.ending_point[1]):
                cab.current_position[1] += 1
                turn_number += 1
                riding_with_passenger += 1
                busy_time += 1
            elif (cab.current_position[1] > track.ending_point[1]):
                cab.current_position[1] -= 1
                turn_number += 1
                riding_with_passenger += 1
                busy_time += 1
   # print(wait_time)

    distance_covered = riding_without_passenger + riding_with_passenger

    return [money_made, wait_time,riding_with_passenger,riding_without_passenger,busy_time,overall_distance_to_target,distance_covered,tracks_completed]

def Distance(starting_point,ending_point):
    distance = abs(ending_point[0] - starting_point[0]) + abs(ending_point[1] - starting_point[1])
    return distance


def TrackTime(track):
    time = abs(track.starting_point[1] - track.starting_point[0]) + abs(track.ending_point[1] - track.ending_point[0])
    return time

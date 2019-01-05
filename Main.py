
from Algorithm import Algorithm
from Algorithm import Mutation
from LoadingTracks import LoadTracksFromFile

track_list = LoadTracksFromFile.Load('Tracks.txt')
cos = Algorithm(track_list,50,50)

cos.NewGeneration()
#cos.ShowSolution()

lolz = Mutation()
print(lolz.GetMutation())
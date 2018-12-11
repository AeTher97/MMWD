
from Algorithm import Algorithm
from LoadingTracks import LoadTracksFromFile

tracks_list = LoadTracksFromFile.Load("Tracks.txt")

algo = Algorithm(4,tracks_list,5,5)

algo.ShowSolution()
print("%%%%%%%%%%%%%%%")
algo.NewGeneration()
algo.ShowSolution()

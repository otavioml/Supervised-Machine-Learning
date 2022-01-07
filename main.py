from read_files import *
from xnn import *

point_list = getDataPoints('data/banana.dat')
trainingPoints, testPoints = getTrainingAndTestsPoints(point_list)

point = [-0.238,-1.41]

xnn = Xnn(priority_queue=[], kdtree=None)
xnn.buildKdtree(trainingPoints)
xnn.k_nearest(getDimensions(trainingPoints), 5, point, xnn.kdtree)

print(xnn.priority_queue)
print(xnn.getClassificationFromPQ(getDimensions(trainingPoints)))








# point_list = [(2,3), (5,4), (9,6), (4,7), (8,1), (7,2)]
# point_list = [(6.7,5.3), (1.8,3.6), (4.8,1), (7.6,4.5), (6.7,4.3), (3.4,7), (5.9,3), (4.6,4.2), (2,8.9), (3.7,8.6)]
from read_files import *
from xnn import *

databases = ['appendicitis', 'banana', 'haberman', 'pima', 'led7digit', 'monk-2', 'heart', 'wdbc', 'phoneme', 'iris', 'ecoli']
# databases = ['ecoli']

for database in databases:
    print('Database: ' + database)
    point_list = getDataPoints('data/' + database + '.dat')
    trainingPoints, testPoints = getTrainingAndTestsPoints(point_list)

    xnn = Xnn(priority_queue=[], kdtree=None)
    xnn.buildKdtree(trainingPoints)
    xnn.getStatisticsFromTestPoints(testPoints, getUniqueClasses(testPoints))

# xnn.k_nearest(getDimensions(trainingPoints), 5, point, xnn.kdtree)

# print(xnn.getClassificationFromPQ(getDimensions(trainingPoints)))
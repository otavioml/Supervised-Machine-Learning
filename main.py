from read_files import *
from xnn import *

databases = ['appendicitis', 'haberman', 'pima', 'led7digit', 'monk-2', 'heart', 'wdbc', 'phoneme', 'iris', 'ecoli', 'banana']

for database in databases:
    print('Database: ' + database)
    point_list = getDataPoints('data/' + database + '.dat')
    trainingPoints, testPoints = getTrainingAndTestsPoints(point_list)

    xnn = Xnn(priority_queue=[], kdtree=None)
    xnn.buildKdtree(trainingPoints)
    xnn.getStatisticsFromTestPoints(5, testPoints, getUniqueClasses(testPoints))
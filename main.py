from kd_tree import Kdtree, printPreorder
from read_files import *
from xnn import *

databases = ['appendicitis', 'haberman', 'pima', 'led7digit', 'monk-2', 'heart', 'wdbc', 'phoneme', 'iris', 'ecoli', 'banana']
databases=['ecoli']

k = 5
print("Quantidades de vizinhos próximos calculados: ", k)

for database in databases:
    print('Database: ' + database)
    point_list = getDataPoints('data/' + database + '.dat')
    trainingPoints, testPoints = getTrainingAndTestsPoints(point_list)


    xnn = Xnn(priority_queue=[])
    xnn.buildKdtree(trainingPoints)
    xnn.getStatisticsFromTestPoints(k, testPoints, getUniqueClasses(testPoints))
    print(len(getUniqueClasses(testPoints)))
    print("\n")
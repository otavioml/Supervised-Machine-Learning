from kd_tree import Kdtree, printPreorder
from read_files import *
from xnn import *

# databases = ['appendicitis', 'haberman', 'pima', 'led7digit', 'monk-2', 'heart', 'wdbc', 'phoneme', 'iris', 'ecoli', 'banana']
databases = ["drug200"]

k = 5
print("Quantidades de vizinhos próximos calculados: ", k)

for database in databases:
    print('Database: ' + database)
    point_list = getDataPoints('data/' + database + '.csv')
    trainingPoints, testPoints = getTrainingAndTestsPoints(point_list)


    xnn = Xnn(priority_queue=[])
    xnn.buildKdtree(trainingPoints)
    xnn.getStatisticsFromTestPoints(k, testPoints, getUniqueClasses(testPoints))
    
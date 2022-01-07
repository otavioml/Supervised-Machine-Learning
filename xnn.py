import numpy as np
import heapq
from kd_tree import Node, Kdtree
from statistics import mode

def euclideanDistance(a, b):
    return np.linalg.norm(np.asarray(a)-np.asarray(b))

def k_nearestAux(dimensions, k, point, current_node, priority_queue=[], depth=0):

        axis = depth % dimensions
        depth += 1

        if current_node.left == None and current_node.right == None:
            # print("*****")
            # print("Current node value: ")
            # print(current_node.value)
            distance = euclideanDistance(point, current_node.value[:dimensions-1])
            # print("Distance: " + str(distance))
            # print("Priority queue")
            # print(priority_queue)
            if len(priority_queue) < k:
                heapq.heappush(priority_queue, (-distance,current_node.value))
                priority_queue = sorted(priority_queue)

            elif -distance < -priority_queue[0][0]:
                heapq.heappushpop(priority_queue, (-distance, current_node.value))
                priority_queue = sorted(priority_queue)

            return priority_queue

        else:
            priority_queue = k_nearestAux(dimensions, k, point, current_node.right, priority_queue, depth)
            priority_queue = k_nearestAux(dimensions, k, point, current_node.left, priority_queue, depth)
        
        # elif point[axis] > current_node.value:
        #     priority_queue = k_nearest(k, point, current_node.right, priority_queue, depth)
        #     if len(priority_queue) < k:
        #         priority_queue = k_nearest(k, point, current_node.left, priority_queue, depth)

        # else:
        #     priority_queue = k_nearest(k, point, current_node.left, priority_queue, depth)
        #     if len(priority_queue) < k:
        #         priority_queue = k_nearest(k, point, current_node.right, priority_queue, depth)

        return priority_queue

def kdtree(point_list, depth=0):
    try:
        k = len(point_list[0]) - 1
    except IndexError as e:
        return None

    if len(point_list) == 1:
        return Node(value=point_list[0],left=None,right=None)

    axis = depth % k

    point_list.sort(key=lambda x: x[axis])
    
    l = len(point_list)
    if l%2 == 0:
        median = int((l/2)-1)
    else:
        median = l // 2

    return Node(
        value=point_list[median][axis],
        left=kdtree(point_list[:median+1], depth + 1),
        right=kdtree(point_list[median + 1:], depth + 1)
    )

class Xnn():

    def __init__(self, priority_queue, kdtree):
        self.priority_queue = priority_queue
        self.kdtree = kdtree

    def buildKdtree(self, point_list):
        self.kdtree = kdtree(point_list)

    def k_nearest(self, dimensions, k, point, current_node):
        self.priority_queue = k_nearestAux(dimensions, k, point, current_node, self.priority_queue, depth=0)

    def getClassificationFromPQ(self, dimensions):
        temp = []
        for p in self.priority_queue:
            temp.append(p[1][dimensions-1])

        return mode(temp)
        

import numpy as np
import heapq

def euclideanDistance(a, b):
    return np.linalg.norm(np.asarray(a)-np.asarray(b))

def printPreorder(node):

    if node:
        print(node.value)
        printPreorder(node.left)
        printPreorder(node.right)

class Node():
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def kdtree(point_list, depth=0):
    try:
        k = len(point_list[0])
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

def k_nearest(k, point, current_node, priority_queue=[], depth=0):

    dimensions = 2
    axis = depth % dimensions
    depth += 1

    if current_node.left == None and current_node.right == None:
        print("*****")
        print("Current node value: ")
        print(current_node.value)
        distance = euclideanDistance(point, current_node.value)
        print("Distance: " + str(distance))
        print("Priority queue")
        print(priority_queue)
        if len(priority_queue) < k:
            heapq.heappush(priority_queue, (-distance,current_node.value))
            priority_queue = sorted(priority_queue)

        elif -distance < -priority_queue[0][0]:
            heapq.heappushpop(priority_queue, (-distance, current_node.value))
            priority_queue = sorted(priority_queue)

        return priority_queue

    else:
        priority_queue = k_nearest(k, point, current_node.right, priority_queue, depth)
        priority_queue = k_nearest(k, point, current_node.left, priority_queue, depth)
    
    # elif point[axis] > current_node.value:
    #     priority_queue = k_nearest(k, point, current_node.right, priority_queue, depth)
    #     if len(priority_queue) < k:
    #         priority_queue = k_nearest(k, point, current_node.left, priority_queue, depth)

    # else:
    #     priority_queue = k_nearest(k, point, current_node.left, priority_queue, depth)
    #     if len(priority_queue) < k:
    #         priority_queue = k_nearest(k, point, current_node.right, priority_queue, depth)

    return priority_queue



# point_list = [(2,3), (5,4), (9,6), (4,7), (8,1), (7,2)]
point_list = [(6.7,5.3), (1.8,3.6), (4.8,1), (7.6,4.5), (6.7,4.3), (3.4,7), (5.9,3), (4.6,4.2), (2,8.9), (3.7,8.6)]
point = [6.8, 5.4]

tree = kdtree(point_list)
#Print kd-tree in preorder transversal
# printPreorder(tree)

pq = k_nearest(3, point, tree)

print(pq)




# x = 1
# for i in point_list:
#     print(x)
#     print(i)
#     print(euclideanDistance(point, i))
#     x+=1
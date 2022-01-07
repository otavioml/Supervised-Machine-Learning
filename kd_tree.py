class Node():
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def printPreorder(node):

    if node:
        print(node.value)
        printPreorder(node.left)
        printPreorder(node.right)

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
class Kdtree():
    def _init__(self, root):
        self.root = root

    def buildKdtree(self, point_list):
        self.root = kdtree(point_list)

kdt = Kdtree()
point_list = [(6.7,5.3), (1.8,3.6), (4.8,1), (7.6,4.5), (6.7,4.3), (3.4,7), (5.9,3), (4.6,4.2), (2,8.9), (3.7,8.6)]
kdt.buildKdtree(point_list)

# printPreorder(kdt.root)


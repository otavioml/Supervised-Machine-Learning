from operator import itemgetter

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
        k = len(point_list[0]) # assumes all points have the same dimension
    except IndexError as e: # if not point_list:
        return None
    # Select axis based on depth so that axis cycles through all valid values
    
    # if k == 1:
    #     return Node(value=point_list[0], left=None, right=None)

    axis = depth % k

    # Sort point list and choose median as pivot element
    point_list.sort(key=itemgetter(axis))
    median = len(point_list) // 2 # choose median

    node_left = kdtree(point_list[:median], depth + 1)
    node_right = kdtree(point_list[median + 1:], depth + 1)

    # if (node_left == None and node_right == None):
    #     return Node(
    #         value=point_list[median],
    #         left=node_left,
    #         right=node_right
    #     )
    # else:
    return Node(
        value=point_list[median][axis],
        left=kdtree(point_list[:median], depth + 1),
        right=kdtree(point_list[median + 1:], depth + 1)
    )



    # Create node and construct subtrees
    return Node(
        value=point_list[median][axis],
        left=kdtree(point_list[:median], depth + 1),
        right=kdtree(point_list[median + 1:], depth + 1)
    )

def main():
    """Example usage"""
    point_list = [(2,3), (5,4), (9,6), (4,7), (8,1), (7,2)]
    # point_list = [(6.7,5.3), (1.8,3.6), (4.8,1), (7.6,4.5), (6.7,4.3), (3.4,7), (5.9,3), (4.6,4.2), (2,8.9), (3.7,8.6)]
    tree = kdtree(point_list)
    printPreorder(tree)

if __name__ == '__main__':
    main()
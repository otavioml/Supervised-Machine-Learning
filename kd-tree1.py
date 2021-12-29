from collections import namedtuple
from operator import itemgetter
from pprint import pformat

class Node(namedtuple('Node', 'location left_child right_child')):
    def __repr__(self):
        return pformat(tuple(self))

def kdtree(point_list, depth=0):
    try:
        k = len(point_list[0]) # assumes all points have the same dimension
    except IndexError as e: # if not point_list:
        return None
    # Select axis based on depth so that axis cycles through all valid values
    axis = depth % k

    # Sort point list and choose median as pivot element
    point_list.sort(key=itemgetter(axis))
    median = len(point_list) // 2 # choose median

    node_left = kdtree(point_list[:median], depth + 1)
    node_right = kdtree(point_list[median + 1:], depth + 1)

    if (node_left == None and node_right == None):
        print("no folha")

    # Create node and construct subtrees
    return Node(
        location=point_list[median][axis],
        left_child=kdtree(point_list[:median], depth + 1),
        right_child=kdtree(point_list[median + 1:], depth + 1)
    )

def main():
    """Example usage"""
    # point_list = [(2,3), (5,4), (9,6), (4,7), (8,1), (7,2)]
    point_list = [(6.7,5.3), (1.8,3.6), (4.8,1), (7.6,4.5), (6.7,4.3), (3.4,7), (5.9,3), (4.6,4.2), (2,8.9), (3.7,8.6)]
    tree = kdtree(point_list)
    print(tree)

if __name__ == '__main__':
    main()
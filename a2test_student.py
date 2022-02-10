"""
Assignment 2: Quadtree Compression

=== CSC148 Winter 2021 ===
Department of Mathematical and Computational Sciences,
University of Toronto Mississauga

=== Module Description ===
This module contains the test suite
"""

import pytest
from a2tree import QuadTreeNode, QuadTreeNodeEmpty, QuadTreeNodeLeaf, QuadTree

"""
Test cases
"""


def test_split_quadrants_1():
    matrix = [ [ 1,  2,  3,  4],
               [ 5,  6,  7,  8],
               [ 9, 10, 11, 12],
               [13, 14, 15, 16]
               ]
    
    tree = QuadTree(0) # loss = 0
    # tree.build_quad_tree(matrix)
    ans = tree._split_quadrants(matrix)
    print(ans)
    expected_out = [[[1,2], [5,6]], [[3,4],[7,8]], [[9, 10],[13 , 14]], [[11,12],[15,16]]]
    print(expected_out)
    assert ans == expected_out


def test_split_quadrants_2():
    matrix = [ [ 1,  2,  3,  4],
               [ 5,  6,  7,  8],
               [ 9, 10, 11, 12],
               [13, 14, 15, 16],
               [ 5,  6,  7,  8]
               ]
    
    tree = QuadTree(0) # loss = 0
    # tree.build_quad_tree(matrix)
    ans = tree._split_quadrants(matrix)
    print(ans)
    expected_out = [[[1,2], [5,6]], [[3,4],[7,8]], [[9, 10],[13 , 14]], [[11,12],[15,16]]]
    print(expected_out)
    assert ans == expected_out



def test_split_quadrants_3():
    matrix = [ [ 2,  3,  1],
               [ 6,  7,  5],
               [10, 11,  9],
               [14, 15, 13],
               ]
    
    tree = QuadTree(0) # loss = 0
    # tree.build_quad_tree(matrix)
    ans = tree._split_quadrants(matrix)
    print(ans)
    expected_out = [[[2], [6]], [[3, 1], [7, 5]], [[10], [14]], [[11, 9], [15, 13]]]
    print(expected_out)
    assert ans == expected_out
    


def test_restore_from_preorder_1():
    preorder = ",,3,4,2,3,,5,6,4,5,,5,6,1,2,,7,8,3,4"
    preorderArr = preorder.split(",")
    tree = QuadTree()
    tree = tree.restore_from_preorder(preorderArr, 3, 3)
    s = tree.preorder()
    assert s == preorder
    


def test_restore_from_preorder_2():
    preorder = ",,215,236,167,158,,149,148,255,102,,202,133,,E,177,E,162,,E,188,E,156,,244,155,,E,199,E,245,,E,100,E,150"
    preorderArr = preorder.split(",")
    tree = QuadTree()
    tree = tree.restore_from_preorder(preorderArr, 4, 5)
    s = tree.preorder()
    assert s == preorder
    


def test_restore_from_preorder_3():
    preorder = ",175,,244,155,199,100,182,,245,150,,E,255,E,149,125"
    preorderArr = preorder.split(",")
    tree = QuadTree()
    tree = tree.restore_from_preorder(preorderArr, 4, 5)
    s = tree.preorder()
    assert s == preorder
    


if __name__ == '__main__':

    pytest.main(['a2test_student.py'])

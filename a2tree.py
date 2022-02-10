"""
Assignment 2: Quadtree Compression

=== CSC148 Winter 2021 ===
Department of Mathematical and Computational Sciences,
University of Toronto Mississauga

=== Module Description ===
This module contains classes implementing the quadtree.
"""

from __future__ import annotations
import math
from typing import List, Tuple, Optional
from copy import deepcopy
# No other imports allowed


def mean_and_count(matrix: List[List[int]]) -> Tuple[float, int]:
    """
    Returns the average of the values in a 2D list
    Also returns the number of values in the list
    """
    total = 0
    count = 0
    # print("matrix: ", matrix)
    # print("W:", len(matrix), "H:", len(matrix[0]))

    for row in matrix:
        # print("row: ", row)
        for v in row:
            total += v
            count += 1

    # print('matrixEnd', count)
    return total / count, count


def standard_deviation_and_mean(matrix: List[List[int]]) -> Tuple[float, float]:
    """
    Return the standard deviation and mean of the values in <matrix>

    https://en.wikipedia.org/wiki/Root-mean-square_deviation

    Note that the returned average is a float.
    It may need to be rounded to int when used.
    """
    avg, count = mean_and_count(matrix)
    total_square_error = 0
    for row in matrix:
        for v in row:
            total_square_error += ((v - avg) ** 2)
    deviation = math.sqrt(total_square_error / count)
    # print("deviation: ", deviation)
    return deviation, avg


class QuadTreeNode:
    """
    Base class for a node in a quad tree
    """

    def __init__(self) -> None:
        pass

    def tree_size(self) -> int:
        raise NotImplementedError

    def convert_to_pixels(self, width: int, height: int) -> List[List[int]]:
        raise NotImplementedError

    def preorder(self) -> str:
        raise NotImplementedError


class QuadTreeNodeEmpty(QuadTreeNode):
    """
    An empty node represents an area with no pixels included
    """

    def __init__(self) -> None:
        super().__init__()

    def tree_size(self) -> int:
        """
        Note: An empty node still counts as 1 node in the quad tree
        """
        # TODO: implement this method
        return 1

    def convert_to_pixels(self, width: int, height: int) -> List[List[int]]:
        """
        Convert to a properly formatted empty list
        """
        # Note: Normally, this method should return an empty list or a list of
        # empty lists. However, when the tree is mirrored, this returned list
        # might not be empty and may contain the value 255 in it. This will
        # cause the decompressed image to have unexpected white pixels.
        # You may ignore this caveat for the purpose of this assignment.
        # print("empty node convertToPix: ",[[255] * width for _ in range(height)], "w,h: ", width, height)
        return [[255] * width for _ in range(height)]

    def convert_to_pixels_helper(self, w: int, h: int, x: int, y: int, outputArray: List[List[int]]):
        # print("Empty Node")
        return

    def preorder(self) -> str:
        """
        The letter E represents an empty node
        """
        return 'E'


class QuadTreeNodeLeaf(QuadTreeNode):
    """
    A leaf node in the quad tree could be a single pixel or an area in which
    all pixels have the same colour (indicated by self.value).
    """

    value: int  # the colour value of the node

    def __init__(self, value: int) -> None:
        super().__init__()
        assert isinstance(value, int)
        self.value = value

    def tree_size(self) -> int:
        """
        Return the size of the subtree rooted at this node
        """
        # TODO: complete this method
        # leaf node has no childern
        return 1

    def convert_to_pixels(self, width: int, height: int) -> List[List[int]]:
        """
        Return the pixels represented by this node as a 2D list

        >>> sample_leaf = QuadTreeNodeLeaf(5)
        >>> sample_leaf.convert_to_pixels(2, 2)
        [[5, 5], [5, 5]]
        """
        # TODO: complete this method
        # convert single leaf node to 2x2 pixel matrix
        pixArr = []
        for h in range(height):
            rowArr = []
            for w in range(width):
                rowArr.append(self.value)
            pixArr.append(rowArr)
        # print("leaf convertToPix: ", pixArr, "W,H: ", width, height)
        return pixArr

    def convert_to_pixels_helper(self, w: int, h: int, x: int, y: int, outputArray: List[List[int]]):
        matrix = outputArray
        # fill the leaf value 2d array
        # children attributes

        newMatrix = self.convert_to_pixels(w, h)
        # print("leaf node: ", newMatrix )
        # print("h,w,x,y: ", h, w, x, y)
        for i in range(0, h):
            for j in range(0, w):
                # print("[x+i], [y+j] , i, j: ",[x+i], [y+j], i, j)
                matrix[x+i][y+j] = newMatrix[i][j]
                # print("evolved matrix:")
                # for row in matrix:
                #     print(row)
        return

    def preorder(self) -> str:
        """
        A leaf node is represented by an integer value in the preorder string
        """
        return str(self.value)


class QuadTreeNodeInternal(QuadTreeNode):

    """
    An internal node is a non-leaf node, which represents an area that will be
    further divided into quadrants (self.children).

    The four quadrants must be ordered in the following way in self.children:
    bottom-left, bottom-right, top-left, top-right

    (List indices increase from left to right, bottom to top)

    Representation Invariant:
    - len(self.children) == 4
    """
    children: List[Optional[QuadTreeNode]]


    def __init__(self) -> None:
        """
        Order of children: bottom-left, bottom-right, top-left, top-right
        """
        super().__init__()

        # Length of self.children must be always 4.
        self.children = [None, None, None, None]
        # self.nodeCount = 1
    def tree_size(self) -> int:
        """
        The size of the subtree rooted at this node.

        This method returns the number of nodes that are in this subtree,
        including the root node.
        """
        # TODO: complete this method
        size = 1
        size += self.children[0].tree_size()
        size += self.children[1].tree_size()
        size += self.children[2].tree_size()
        size += self.children[3].tree_size()

        return size


    def convert_to_pixels(self, width: int, height: int) -> List[List[int]]:
        """
        Return the pixels represented by this node as a 2D list.

        You'll need to recursively get the pixels for the quadrants and
        combine them together.

        Make sure you get the sizes (width
        # This assert will help you find errors.
        # Since this is an internal node, the first entry to restore should
        # be an empty string
        assert lst[start] == ''

        # This assert will help you find errors.
        # Since this is an internal node, the first entry to restore should
        # be an empty string
        assert lst[start] == ''
/height) of the quadrants correct!
        Read the docstring for split_quadrants() for more info.
        """
        # TODO: complete this method
        # traverse through tree. determine position, height, width of leaf node pixels
        # generate 2d array.

        parentNodePixArr = []
        for row in range(height):
            rowArr =[]
            for col in range(width):
                rowArr.append(-1)
            parentNodePixArr.append(rowArr)

        self.convert_to_pixels_helper( width, height, 0, 0, parentNodePixArr)
        # print("converted 2D array")
        # for row in parentNodePixArr:
        #     print(row)
        return parentNodePixArr

    def convert_to_pixels_helper(self, w: int, h: int, x: int, y: int, outputArray: List[List[int]]):
        # matrix = outputArray
        # fill the leaf value 2d array
        # children attributes
        # print("Internal Node:  h,w,x,y", h,w,x,y)

        self.children[0].convert_to_pixels_helper(int((w)/2)  , int(h/2)    , x, y, outputArray) # TR
        self.children[1].convert_to_pixels_helper(int((w+1)/2), int(h/2)    , x, y+ int(w/2), outputArray) # TR
        self.children[2].convert_to_pixels_helper(int(w/2)    , int((h+1)/2), x+int(h/2), y, outputArray) # BL
        self.children[3].convert_to_pixels_helper(int((w+1)/2), int((h+1)/2), x+int(h/2), y+int(w/2), outputArray) # BR

    def preorder(self) -> str:
        """
        Return a string representing the preorder traversal or the tree rooted
        at this node. See the docstring of the preorder() method in the
        QuadTree class for more details.

        An internal node is represented by an empty string in the preorder
        string.
        """
        # TODO: complete this method
        # call 4 preorders, append the return values to string with ','
        str0 = self.children[0].preorder()
        str1 = self.children[1].preorder()
        str2 = self.children[2].preorder()
        str3 = self.children[3].preorder()

        subTreePreorder = "," + str0 + "," + str1 + "," + str2 + "," + str3
        # print("subtree prorder: ", subTreePreorder)
        return subTreePreorder

    def restore_from_preorder(self, lst: List[str], start: int) -> int:
        """
        Restore subtree from preorder list <lst>, starting at index <start>
        Return the number of entries used in the list to restore this subtree
        """

        # This assert will help you find errors.
        # Since this is an internal node, the first entry to restore should
        # be an empty string
        assert lst[start] == ''
        preOrderIndex = [start+1]
        # TODO: complete this method
        self.restore_from_preorder_helper(lst, preOrderIndex)
        pass

    def restore_from_preorder_helper(self, preOrderList, index):
        if(len(preOrderList) == index[0]):
            return

        emptyPos = 0
        while(emptyPos < 4) :
            if preOrderList[index[0]] == 'E':
                self.children[emptyPos] = QuadTreeNodeEmpty()
                emptyPos += 1
                index[0] += 1

            elif preOrderList[index[0]] == '':
                self.children[emptyPos] = QuadTreeNodeInternal()
                index[0] += 1
                self.children[emptyPos].restore_from_preorder_helper(preOrderList, index)
                emptyPos += 1

            else:
                self.children[emptyPos] = QuadTreeNodeLeaf(int(preOrderList[index[0]]))
                emptyPos += 1
                index[0] += 1

    def mirror(self) -> None:
        """
        Mirror the bottom half of the image represented by this tree over
        the top half

        Example:
            Original Image
            1 2
            3 4

            Mirrored Image
            3 4 (this row is flipped upside down)
            3 4

        See the assignment handout for a visual example.
        """
        # TODO
        print("mirror self: ", self)
        


class QuadTree:
    """
    The class for the overall quadtree
    """

    loss_level: float
    height: int
    width: int
    root: Optional[QuadTreeNode]  # safe to assume root is an internal node

    def __init__(self, loss_level: int = 0) -> None:
        """
        Precondition: the size of <pixels> is at least 1x1
        """
        self.loss_level = float(loss_level)
        self.height = -1
        self.width = -1
        self.root = None

    def build_quad_tree(self, pixels: List[List[int]],
                        mirror: bool = False) -> None:
        """
        Build a quad tree representing all pixels in <pixels>
        and assign its root to self.root

        <mirror> indicates whether the compressed image should be mirrored.
        See the assignment handout for examples of how mirroring works.
        """
        # print('building_quad_tree...')
        self.height = len(pixels)
        self.width = len(pixels[0])
        self.root = self._build_tree_helper(pixels)
        if mirror:
            self.root.mirror()
        return

    def _build_tree_helper(self, pixels: List[List[int]]) -> QuadTreeNode:
        """
        Build a quad tree representing all pixels in <pixels>
        and return the root

        Note that self.loss_level should affect the building of the tree.
        This method is where the compression happens.

        IMPORTANT: the condition for compressing a quadrant is the standard
        deviation being __LESS THAN OR EQUAL TO__ the loss level. You must
        implement this condition exactly; otherwise, you could fail some
        test cases unexpectedly.
        """
        # TODO: complete this method
        # recieve pixel array
        # create a intermediate node, value = mean of pixel
        # find deviation loss condition
        # if below loss: return
        # if above loss:
        # split pixels in quadrant
        # initialise 4 intermediate node and call build_quad_tree() with quadrant pixels as pixels arr
        # print("pixels: ", pixels)
        if( pixels == [[]]):
            # print("adding empty node: ")
            emptyNode = QuadTreeNodeEmpty()
            return emptyNode

        deviation, mean = standard_deviation_and_mean(pixels)
        # print(deviation, self.loss_level, mean)
        if(deviation <= self.loss_level):
            # create n return leaf node. ie root == leaf
            # print("adding leaf with value: ", int(mean))
            leafNode = QuadTreeNodeLeaf(round(mean))
            return leafNode
        else:
            quadArr = self._split_quadrants(pixels)
            # print("spliting to: ", )
            # for qd in range(4):
            #     print("qd", qd)
            #     for row in quadArr[qd]:
            #         print(row)


            intermediateNode = QuadTreeNodeInternal()
            intermediateNode.children[0] = self._build_tree_helper(quadArr[0])
            intermediateNode.children[1] = self._build_tree_helper(quadArr[1])
            intermediateNode.children[2] = self._build_tree_helper(quadArr[2])
            intermediateNode.children[3] = self._build_tree_helper(quadArr[3])
            # print("layer complete")
            return intermediateNode
            # create intermediate node, split to 4 quadrants,
            # call build_quad_tree with quadrant pixels as pixels arr and
            # assign the return value to children of intermediate node



    @staticmethod
    def _split_quadrants(pixels: List[List[int]]) -> List[List[List[int]]]:
        """
        Precondition: size of <pixels> is at least 1x1
        Returns a list of four lists of lists, correspoding to the quadrants in
        the following order: bottom-left, bottom-right, top-left, top-right

        IMPORTANT: when dividing an odd number of entries, the smaller half
        must be the left half or the bottom half, i.e., the half with lower
        indices.

        Postcondition: the size of the returned list must be 4

        >>> example = QuadTree(0)
        >>> example._split_quadrants([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [[[1]], [[2, 3]], [[4], [7]], [[5, 6], [8, 9]]]
        """
        # TODO: complete this method
        height = len(pixels)
        width = len(pixels[0])

        halfH = int(height/2)
        halfW = int(width/2)
        topL = []
        topR = []
        bottomL = []
        bottomR = []


        #q1 top left in array (bottom left in Image)
        if(halfH == 0):
            topL = [[]]
            topR = [[]]
        for y in range(halfH):
            rowArr = []
            for x in range(halfW):
                rowArr.append(pixels[y][x])
            topL.append(rowArr)
            #q2 top right in array (bottom right in Image)
        for y in range(halfH):
            rowArr = []
            for x in range(halfW, width):
                rowArr.append(pixels[y][x])
            topR.append(rowArr)
            #q3 bottom left in array (top left in Image)
        for y in range(halfH,height):
            rowArr = []
            for x in range(halfW):
                rowArr.append(pixels[y][x])
            bottomL.append(rowArr)
            #q4 bottom right in array (top right in Image)
        for y in range(halfH,height):
            rowArr = []
            for x in range(halfW,width):
                rowArr.append(pixels[y][x])
            bottomR.append(rowArr)

        resArr = [topL,topR,bottomL,bottomR]
        # print(resArr)
        return resArr

    def tree_size(self) -> int:
        """
        Return the number of nodes in the tree, including all Empty, Leaf, and
        Internal nodes.
        """
        return self.root.tree_size()

    def convert_to_pixels(self) -> List[List[int]]:
        """
        Return the pixels represented by this tree as a 2D matrix
        """
        compressedPixArr = self.root.convert_to_pixels(self.width, self.height)
        # print("rootTree pixel arr")
        # for row in compressedPixArr:
        #     print(row)
        return compressedPixArr

    def preorder(self) -> str:
        """
        return a string representing the preorder traversal of the quadtree.
        The string is a series of entries separated by comma (,).
        Each entry could be one of the following:
        - empty string '': represents a QuadTreeNodeInternal
        - string of an integer value such as '5': represents a QuadTreeNodeLeaf
        - string 'E': represents a QuadTreeNodeEmpty

        For example, consider the following tree with a root and its 4 children
                __      Root       __
              /      |       |        \
            Empty  Leaf(5), Leaf(8), Empty

        preorder() of this tree should return exactly this string: ",E,5,8,E"

        (Note the empty-string entry before the first comma)
        """
        return self.root.preorder()

    @staticmethod
    def restore_from_preorder(lst: List[str], width: int, height: int) -> QuadTree:
        """
        Restore the quad tree from the preorder list <lst>
        The preorder list <lst> is the preorder string split by comma

        Precondition: the root of the tree must be an internal node (non-leaf)
        """
        tree = QuadTree()
        tree.width = width
        tree.height = height
        tree.root = QuadTreeNodeInternal()
        tree.root.restore_from_preorder(lst, 0)
        return tree



def maximum_loss(original: QuadTreeNode, compressed: QuadTreeNode) -> float:
    """
    Given an uncompressed image as a quad tree and the compressed version,
    return the maximum loss across all compressed quadrants.

    Precondition: original.tree_size() >= compressed.tree_size()

    Note: original, compressed are the root nodes (QuadTreeNode) of the
    trees, *not* QuadTree objects

    >>> pixels = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> orig, comp = QuadTree(0), QuadTree(2)
    >>> orig.build_quad_tree(pixels)
    >>> comp.build_quad_tree(pixels)
    >>> maximum_loss(orig.root, comp.root)
    1.5811388300841898
    """
    # TODO: complete this function
    # simultaneously traverse trees in same direction
    # if comp has mean leaf node where orignal has subtree
    # calculate the loss between mean and each leaf node of the sub tree
    # save the loss in loss_arr
    # traverse to parrent sibling, goto step 1
    max_loss = [0]
    maximum_loss_helper(max_loss, original.root , compressed.root)
    # print("final max_loss: ", max_loss[0])
    return max_loss[0]

def maximum_loss_helper(max_loss, original, compressed):

    if original.tree_size() == 1 and compressed.tree_size() == 1:
        # if nodes are leaf - compare absolute loss value
        if(original.preorder() != 'E' and compressed.preorder() != 'E'):
            loss = abs(original.value - compressed.value)
            if max_loss[0] < loss:
                max_loss[0] = loss

            # print("max_loss, loss: ", original.value, compressed.value ,max_loss, loss)

    elif original.tree_size() > 1 and compressed.tree_size() == 1:
        maximum_loss_helper(max_loss, original.children[0], compressed)
        maximum_loss_helper(max_loss, original.children[1], compressed)
        maximum_loss_helper(max_loss, original.children[2], compressed)
        maximum_loss_helper(max_loss, original.children[3], compressed)
    elif original.tree_size() > 1 and compressed.tree_size() > 1:
        maximum_loss_helper(max_loss, original.children[0], compressed.children[0])
        maximum_loss_helper(max_loss, original.children[1], compressed.children[1])
        maximum_loss_helper(max_loss, original.children[2], compressed.children[2])
        maximum_loss_helper(max_loss, original.children[3], compressed.children[3])


if __name__ == '__main__':

    import doctest
    doctest.testmod()

    # import python_ta
    # python_ta.check_all()

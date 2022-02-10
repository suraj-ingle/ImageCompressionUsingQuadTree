from a2main import Compressor, Decompressor

comp = Compressor('dog.bmp', 40) # less_level = 0
comp.run()

decomp = Decompressor('dog.bmp.qdt')
decomp.run()

# from a2tree import QuadTreeNode, QuadTreeNodeEmpty, QuadTreeNodeLeaf, QuadTree

# """
# Test cases
# """

# def test_split_quadrants_1():
    
#     preorder = ",175,,244,155,199,100,182,,245,150,,E,255,E,149,125"
#     preorderArr = preorder.split(",")
#     tree = QuadTree()
#     tree = tree.restore_from_preorder(preorderArr, 4, 5)
#     s = tree.preorder()
    
#     assert s == preorder

# test_split_quadrants_1()

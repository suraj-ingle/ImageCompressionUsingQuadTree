QuadTreeNodeEmpty
    tree_size: Return the size of the subtree rooted at this node (1)

QuadTreeNodeLeaf
    tree_size: Return the size of the subtree rooted at this node (1)
    convert_to_pixels: split array as per qudrants

QuadTreeNodeInternal
    tree_size: Return the size of the subtree rooted at this node (sub-tree traversal)

    convert_to_pixels: 2d array (to be clarified)

    preorder: 

    restore_from_preorder: 
    mirror: 

QuadTree: 
    _build_tree_helper :
    _split_quadrants

maximum_loss
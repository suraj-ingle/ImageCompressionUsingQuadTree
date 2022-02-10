preOrder = ",,215,236,167,158,,149,148,255,102,,202,133,,E,177,E,162,,E,188,E,156,,244,155,,E,199,E,245,,E,100,E,150"
preOrder = preOrder.split()

start = 0
preOrderIndex = 0
root = QuadTreeNodeInternal()
add_to_current(root)

def add_to_current( currentNode, preOrderIndex ):
    emptyPos = 0
    if preOrder[preOrderIndex] == 'E':
        currentNode[emptyPos] = QuadTreeNodeEmpty()
        emptyPos += 1
        preOrderIndex += 1
    
    elif preOrder[preOrderIndex].isnumeric():
        currentNode[emptyPos] = QuadTreeNodeLeaf( int(preOrder[preOrderIndex]) )
        emptyPos += 1
        preOrderIndex += 1

    elif preOrder[preOrderIndex] == '':
        currentNode[emptyPos] = QuadTreeNodeInternal()
        preOrderIndex += 1
        emptyPos += 1
        add_to_current(currentNode[emptyPos])

    if emptyPos == 4:
        return
from a2tree import QuadTree, maximum_loss

arr = [
    [202,133,244,155],
    [177,188,199,100],
    [162,156,245,150],
    [167,158,255,102],
    [215,236,149,148],
    ]

arr2 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
preOrder = ",,215,236,167,158,,149,148,255,102,,202,133,,E,177,E,162,,E,188,E,156,,244,155,,E,199,E,245,,E,100,E,150"
preOrder = preOrder.split(",")

comp20preOrder = ",175,,244,155,199,100,182,,245,150,,E,255,E,149,125"
comp20preOrder = comp20preOrder.split(',')

tree = QuadTree()
tree.build_quad_tree(arr)
# print("tree size")
# tree.tree_sizee convTo()
# print("trePix")
tree.convert_to_pixels()
# tree2 = QuadTree()
# tree2.build_quad_tree(arr)
# tree2.restore_from_preorder(preOrder.split(","), len(arr[0]), len(arr))
# print("restored preorder", tree.preorder())

comp = QuadTree(40)
comp.build_quad_tree(arr)
print(comp.tree_size())
print(comp.tree_size())
print(comp.tree_size())
print(comp.tree_size())
# for row in tree.convert_to_pixels():
#     print(row)
# print("\n")
# print("orignal    preorder: ", tree.preorder())
# for row in comp.convert_to_pixels():
#     print(row)
# print("compressed preorder: ", comp.preorder())
# comp.convert_to_pixels()
# print("max loss: ")
# print("final returned max_loss: ", maximum_loss(tree, comp))


def splitQd(pixel):
    # print(pixel)
    height = len(pixel) 
    width = len(pixel[0])

    halfH = int(height/2)
    halfW = int(width/2)
    q1 = []
    q2 = []
    q3 = []
    q4 = []

    if( halfH == 0):
        q1 = [[]]
        q2 = [[]]
    #q1
    for y in range(halfH):
        rowArr = []
        for x in range(halfW):
            rowArr.append(pixel[y][x])
        q1.append(rowArr)  
    
    #q2
    for y in range(halfH):
        rowArr = []
        for x in range(halfW, width):
            rowArr.append(pixel[y][x])
        q2.append(rowArr)  
   #q3
    for y in range(halfH,height):
        rowArr = []
        for x in range(halfW):
            rowArr.append(pixel[y][x])
        q3.append(rowArr)  
    #q4
    for y in range(halfH,height):
        rowArr = []
        for x in range(halfW,width):
            rowArr.append(pixel[y][x])
        q4.append(rowArr)  


    resArr = [q1,q2,q3,q4]
    print(resArr)
    return resArr
# splitQd(arr)

def inputs():
    print("Quad Tree Image Compression")
    print("===========================")
    print("Input 'q' at any point to terminate the app\n\n") 

    compOrDecomp = input("Command [c -> Compress| d -> Decompress]: ")
    if compOrDecomp == "q":
        exit()
    if compOrDecomp == "c":
        loss = input("Loss [between 0-255]: ")
        if loss == "q":
            exit()

    fileName = input("File name: ")
    if fileName == "q":
        exit() 
# inputs()


# arr = [[-1]*4]*5
# h = 5; w=4; x = 0; y = 0
# [int(h/2) , int(h/2), int((h+1)/2), int((h+1)/2)]
# [int(w/2) , int((w+1)/2), int(w/2), int((w+1)/2)]
# [x, x, x+int(h/2), x+int(h/2)]
# [y, y+int(w/2), y, y+int(w/2)]

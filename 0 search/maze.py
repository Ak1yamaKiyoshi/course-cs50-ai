class Node:
    def __init__(self, action, parent, state):
        self.action = action  #  action to do 
        self.parent = parent  #  state before current state 
        self.state = state    #  current state 
        

class StackFrontier: #  last in, first out 
    """ Dept first search frontier """
    
    def __init__(self) -> None:
        self.frontier = [] #  array of frontier to decide which actions to do   
    
    def add(self, node) -> None:
        """ add node to frontier """
        self.frontier.append(node)
        
    def contains_state(self, state) -> bool:
        """ checks if frontier already contains given state """
        return any(node.state == state for node in self.frontier)
    
    def empty(self) -> bool:
        """ checks if frontier is empty """
        return len(self.frontier) == 0
    
    def remove(self):
        """ remove from end of frontier 
            * if frontier is empty, will raise an exception 
            * returns removed from frontier node 
        """
        if self.empty():
            raise Exception("StackFrontier: Frontier is empty")
        else:
            #  save last element of frontier until deleting it 
            node = self.frontier[-1] 
            #  delete last element of frontier 
            self.frontier = self.frontier[:-1] # frontier = frontier without last element
            return node #  returns saved node  
        
class QueueFrontier(StackFrontier):
    """ Breadth first search frontier """

    def remove(self) -> Node:
        """ remove from beginning of frontier ( first element )
            * if frontier is empty, will raise an exception 
            * returns removed from frontier node 
        """
        if self.empty():
            raise Exception("QueueFrontier: Frontier is empty")
        else:
            #  save first element of frontier 
            node = self.frontier[0] 
            #  delete first element from frontier 
            self.frontier = self.frontier [1:]    
            return node #  return popped element 
        
class Maze():
    def __init__(self, rawMaze) -> None:
        # check if there is start and finish point 
        if "A" not in rawMaze:
            raise Exception("No starting point in raw maze string")
        if "B" not in rawMaze:
            raise Exception("No finish point in raw maze string")
        self.parse(rawMaze)


    def matrixLookForSpaces(self, matrix, explored, pos):
        """ returns list of cells around pos that not explored yet """
        
        output = []
        
        try:
            # if cell above is space and not explored 
            if (matrix[pos[0]+1][pos[1]] != "#" and [pos[0]+1, pos[1]] not in explored):
                output.append([pos[0]+1, pos[1]]) # append to output list 
        except: pass
        try:
            # if cell below is space and not explored 
            if (pos[0]-1 >= 0 and matrix[pos[0]-1][pos[1]] != "#" and [pos[0]-1, pos[1]] not in explored):
                output.append([pos[0]-1, pos[1]]) # append to output list 
        except: pass
        # if cell right is space and not explored 
        try:
            if (matrix[pos[0]][pos[1]+1] != "#" and [pos[0], pos[1]+1] not in explored):
                output.append([pos[0], pos[1]+1]) # append to output list 
        except: pass
        try:
            # if cell left is space and not explored 
            if (pos[1]-1 >= 0 and matrix[pos[0]][pos[1]-1] != "#" and [pos[0], pos[1]-1] not in explored):
                output.append([pos[0], pos[1]-1]) # append to output list 
        except: pass
        return output
    
    def findAInMatrix(self, matrix):
        """ Finds strarting point in the matrix """
        for i_y, y in enumerate(matrix):
            for i_x, x in enumerate(y):
                if x == "A":
                    return [i_y, i_x]
                
    def raw_maze_to_matrix(self, rawMaze):
        return [list(x) for x in  rawMaze.splitlines()]
    
    def parse(self, rawMaze):
        """ parse raw maze string to Node tree """
        matrix = self.raw_maze_to_matrix(rawMaze)
        
        explored = []
        position = self.findAInMatrix(matrix)
        flag = True
        positions = []
        while (flag == True): 
            # find next avaivable positions
            positions += self.matrixLookForSpaces(matrix, explored, position)
            # add current position to explored, so we cant go back 
            explored.append(position) 
            # check if there is no positions 
            if positions == []: # if so, end loop 
                flag = False
                continue 
            position = positions.pop() # update current position
        print(explored, len(explored))
    
    def build_tree(explored):
        pass
    # TODO: build tree 
        
    
    def printMatrix(self, rawMaze):
        """ print matrix from rawMaze """
        matrix = [list(x) for x in  rawMaze.splitlines()]
        c = 0
        for y in matrix:
            
            if (c == 0): # print indexes by x
                b = 0; print('.', end=' ')
                for i in range(len(y)):
                    print(b, end='|'); b+= 1
                print('')
            print(c, end=''); c+= 1 # print indexes by y
            
            # print maze 
            for i in y:
                if (i == "#"): print("⬜", end='')
                elif (i == " "): print("⬛", end='')
                elif (i == "A"): print("🅰️", end='')
                elif (i == "B" ): print("🅱️", end='')
            print("")
            
    def print_with_highlight(self, rawMaze, highlight):
        matrix = [list(x) for x in  rawMaze.splitlines()]
        c = 0
        for i_y, y in enumerate(matrix):
            
            if (c == 0): # print indexes by x
                b = 0; print('.', end=' ')
                for i in range(len(y)):
                    print(b, end='|'); b+= 1
                print('')
            print(c, end=''); c+= 1 # print indexes by y
            
            # print maze 
            for i_x, i in enumerate(y):
                if ([i_y, i_x] in highlight): print("🟪", end='')
                elif (i == "#"): print("⬜", end='')
                elif (i == " "): print("⬛", end='')
                elif (i == "A"): print("🅰️", end='')
                elif (i == "B" ): print("🅱️", end='')
            print("")
                
    
mazeRaw2 ="""######                #
##     ############## #
## ### #        ##### #
     #   ###### ##    #
 ### ### ###### ## ## #
  ##              B##A#
"""

mazeRaw1 = """###    #
##  ## #
#  ##  #
#A##B ##
"""
mazeRaw = """#   #    #
# # # ## #
# #   ## #
# ###### A
#      B##"""

print(mazeRaw2.count(" "))
Maze(mazeRaw2)


    
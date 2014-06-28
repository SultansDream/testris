#!/usr/bin/python2.7

import sys
import numpy as np
import copy

WIDTH = 10
LENGTH = 22

#Command Codes
PRINT_TETRAMINO_CODE = "P"
PRINT_CODE = 'p'
EXIT_CODE = 'q'
GIVEN_CODE = 'g'
CLEAR_CODE = 'c'
SCORE_CODE = '?s'
REGISTER_CODE = '?n'
STEP_CODE = 's'
DISPLAY_CODE = 't'
ROTATE_CODE = ')'
CODE_SPACE = ';'
LEFT_CODE = '<'
RIGHT_CODE = '>'
DOWN_CODE = 'v'
CROTATE_CODE = '('
HARD_DROP_CODE = 'V'

#Dictionary to contain all them tetraminos
tetraminos = {
'I': '''. . . .
c c c c
. . . .
. . . .'''
,
'O': '''y y
y y'''
,
'Z': '''r r .
. r r
. . .'''
,
'S': '''. g g
g g .
. . .'''
,
'J': '''b . .
b b b
. . .'''
,
'L': '''. . o
o o o
. . .'''
,
'T': '''. m .
m m m
. . .'''
}

tetraminos_building_blocks = {
'O': 'y',
'L': 'o',
'J': 'b',
'Z': 'r',
'S': 'g',
'I': 'c',
'T': 'm'
}

tetraminos_starting_position = {
'O': [0,4],
'L': [0,3],
'J': [0,3],
'Z': [0,3],
'S': [0,3],
'I': [0,3],
'T': [0,3]
}



 
def main():
    #Initialize our matrix with '.' to denote empty spaces
    matrix = [['.']*WIDTH for y in xrange(LENGTH)]
    #Initialize score and register to 0
    score = 0
    register = 0
    tetramino_objects = {}

    while True:
        commands = raw_input()
        
            
        for command in read_commands(commands).split():
            if command == EXIT_CODE:
                sys.exit()
            
          


            elif command == PRINT_CODE:
                for tetramino in tetramino_objects:
                    matrix = tetramino_objects[tetramino].lower_array(matrix)
                
                print_matrix(matrix)

            elif command == GIVEN_CODE:
                matrix = given(matrix)

            elif command == CLEAR_CODE:
                matrix =  [['.']*WIDTH for y in xrange(LENGTH)]

            elif command == SCORE_CODE:
                print score

            elif command == REGISTER_CODE:
                print register
            
            elif command == STEP_CODE:
                score, register = step(matrix, score, register)
        
            elif command in tetraminos.keys():
                for tetramino in tetramino_objects:
                    matrix = tetramino_objects[tetramino].lower_array(matrix)
                tetramino_objects.clear()
                tetramino_objects[command] = Tetramino(tetraminos[command], tetraminos_starting_position[command], tetraminos_building_blocks[command])
           
            elif command == DISPLAY_CODE:
                for tetramino in tetramino_objects:
                    tetramino_objects[tetramino].print_tetramino()
            
            elif command == PRINT_TETRAMINO_CODE:
                        
                for tetramino in tetramino_objects:
                    matrix = tetramino_objects[tetramino].concatenate_tetramino_with_matrix(matrix)
                
                print_matrix(matrix)
                
               
                
            elif command == ROTATE_CODE:
                for tetramino in tetramino_objects:
                    tetramino_objects[tetramino].rotate()
        

            elif command == CROTATE_CODE:
                for tetramino in tetramino_objects:
                    tetramino_objects[tetramino].crotate()

            elif command == CODE_SPACE:
                print ""

            elif command == LEFT_CODE:
                for tetramino in tetramino_objects:
                    matrix = tetramino_objects[tetramino].move_tetramino(matrix, LEFT_CODE, commands)
                
            elif command == RIGHT_CODE:
                for tetramino in tetramino_objects:
                    matrix = tetramino_objects[tetramino].move_tetramino(matrix, RIGHT_CODE, commands)
            elif command == DOWN_CODE:
                for tetramino in tetramino_objects:
                    matrix = tetramino_objects[tetramino].move_tetramino(matrix, DOWN_CODE, commands)
            
            elif command == HARD_DROP_CODE:
                for tetramino in tetramino_objects:
                    matrix = tetramino_objects[tetramino].hard_drop(matrix)
                
                    

            else:
                pass

            #So the most recent problem is that we still have the for loops which mean that every movement applies to all the tetramino that we have spawned so far

class Tetramino:
    
    def __init__(self, tetramino, start_position, brick):
        self.tetramino = tetramino.upper()
        self.tetramino_array = self.tetramino_to_array()
        self.index = start_position
        self.brick = brick
        self.matrix = None
    

    def rotate(self):
        #rotation algorithm I will never understand again
        self.split_tetramino = self.tetramino.split('\n')
        self.rotated_tetramino = ""
        for column in range(0, len(self.split_tetramino[0]), 2):
            for row in reversed(self.split_tetramino):
                self.rotated_tetramino += row[column] + " "
            self.rotated_tetramino.rstrip()
            self.rotated_tetramino += "\n"
        self.tetramino = self.rotated_tetramino.rstrip("\n")
        
        #Make sure to update tetramino array
        self.tetramino_array = self.tetramino_to_array()
        return self.tetramino

    def crotate(self):
        #counter clockwise rotation written using numpy arrrays this time
        #to conserve sanity
        new_array = self.tetramino_array[:]
        for new_y, colomn in enumerate(reversed(range(len(self.tetramino_array[0])))): 
            for new_x, row in enumerate(range(len(self.tetramino_array[:,0]))):
                new_array[new_y, new_x] = self.tetramino_array[row, colomn]

        self.tetramino_array = new_array
            
    
    def print_tetramino(self):
       #Just a simple function to print out the bare tetramino 
       #Lowers the case to pass the test's requirements
        print self.tetramino.lower()
        return

    def lower_array(self, matrix):
        #make a copy of the string to work with
        tetramino = self.tetramino[:] 
        tetramino = tetramino.lower()
        tetramino_array = self.tetramino_to_array(tetramino)
        matrix = self.concatenate_tetramino_with_matrix(matrix, tetramino_array)
        return matrix



    def concatenate_tetramino_with_matrix(self, matrix, tetramino_array = None, index = None, collision_flag = 0):
        
        if tetramino_array == None:
            tetramino_array = self.tetramino_array[:]

        if index == None:
            index = self.index[:]

    #Replace the matrix with the tetramino
    #Replaces the matrix if it is empty with the appropriate block
    #Uses index to denote tetramino top left corner on matrix, and x and y as 
    #offsets
        matrix = np.array(matrix)  
        for y in range(len(tetramino_array)):
            for x in range(len(tetramino_array[0])):
                if y+index[0] < len(matrix[:,0]) + 1 and x+index[1] < len(matrix[0]):
                    if tetramino_array[y][x] != '.':
                        matrix[y+index[0]][x+index[1]] = tetramino_array[y][x]

  
                    
        return matrix
             
    def clear_tetramino_on_matrix(self, matrix): 
  
        matrix = np.array(matrix)
        
  
        for y in range(len(self.tetramino_array)):
            for x in range(len(self.tetramino_array[0])):
                if self.tetramino_array[y][x] != '.':
                    matrix[y+self.index[0]][x+self.index[1]] = "."
        return matrix


    def hard_drop(self, matrix):
       
        flying = True

        while flying:
          
           
            new_index = self.index[:]
            new_index[0] =  new_index[0] + 1

            
            
            
            collision_simulation = self.collision_detection(matrix, new_index)
            collision_result = collision_simulation[0]
            collision_new_index = collision_simulation[1]
            collision_new_array = collision_simulation[2]
        
           
            
            if collision_result != True:
                matrix = self.clear_tetramino_on_matrix(matrix) 
                matrix = self.concatenate_tetramino_with_matrix(matrix, collision_new_array, collision_new_index, 1)    
    
                self.index = new_index[:]

            else:
                flying = False

       

        return matrix


    def move_tetramino(self, matrix, direction, commands):
        RIGHT = '>'
        LEFT = '<'
        DOWN = 'v'
        NOWHERE = 0

        #use the new matrix instead of the old one, this is because the old
        #matrix is not updated following every move
      

        new_index = self.index[:]
        
        
        
        #changes the phantom index
        if direction == RIGHT:
            new_index[1] += 1

        elif direction == LEFT:
            new_index[1] += -1
        
        elif direction == DOWN:
            new_index[0] += 1
       
            

        collision_simulation = self.collision_detection(matrix, new_index)
        collision_result = collision_simulation[0]
        collision_new_index = collision_simulation[1]
        collision_new_array = collision_simulation[2]
        
        if collision_result != True:
            matrix = self.clear_tetramino_on_matrix(matrix)
            matrix = self.concatenate_tetramino_with_matrix(matrix, collision_new_array, collision_new_index, 1)
            self.index = new_index

            

        return matrix 
        
        
    def collision_detection(self, matrix, new_index): 

        #Remove all single colomns and rows that are simply "white space"
        #Then depending on the direction:
        #Find the first tetramino block in each row/colomn and find if the space
        #It is moving into is empty
        #If so the index can be changed

        new_index = new_index[:]
      
        EMPTY_SPACE = '.'
        EMPTY_ROW = len(self.tetramino_array[0])*[EMPTY_SPACE]
        EMPTY_COLOMN = len(self.tetramino_array[:,0])*[EMPTY_SPACE]
       
        collision = False
       
        whiteless_array = self.tetramino_array[:]
        matrix = np.array(matrix)

        #now we change the index (this is To Make Collision Easier to deal with)
        for index, row in enumerate(whiteless_array):
            if np.array_equal(row, EMPTY_ROW):
                new_index[0] += 1
            else:
                break

        for colomn in range(len(whiteless_array[0])):
            if np.array_equal(whiteless_array[:,colomn], EMPTY_COLOMN):
                new_index[1] += 1
            else:
                break

        
        #deletes the colomn if it is empty
        columns_to_delete = []
        for colomn in range(len(whiteless_array[0])):
            if np.array_equal(whiteless_array[:,colomn], EMPTY_COLOMN):
                columns_to_delete.append(colomn)


        whiteless_array = np.delete(whiteless_array, columns_to_delete, 1)
           

        EMPTY_ROW = len(self.tetramino_array[0])*[EMPTY_SPACE]
            
        #deletes the row if it is empty
        #uses some nifty numpy functions
        for index, row in enumerate(whiteless_array):
            if np.array_equal(row, EMPTY_ROW):
                whiteless_array = np.delete(whiteless_array, index, 0)
                
                
           
    
       


        #This is border detection control/police
        if new_index[1] < 0:
            collision = True
        elif new_index[1] + len(whiteless_array[0]) > len(matrix[0]):
            collision = True
        elif new_index[0] + len(whiteless_array[:,0]) > len(matrix[:,0]):
            collision = True
      
     
         


        #So run a loop using the index and the matrix to gather the coordiantes
        #of all the original tetramino blocks
        #Next, using the new index and the matrix, if some coordinate does not
        #belong in the compiled list then compare it to the matrix and see if 
        #the matrix is clear
        #If at anypoint the matrix is not clear clear, break the loop


   

        if collision != True:
            old_tetramino_blocks = []
            for y in range(len(self.tetramino_array)):
                for x in range(len(self.tetramino_array[0])):
                    if self.tetramino_array[y][x] != ".":
                        old_tetramino_blocks.append([self.index[0] +  y, self.index[1]+ x])
                                          
            for y in range(len(whiteless_array)):
                for x in range(len(whiteless_array[0])):
                    if [y + new_index[0] ,x + new_index[1]] not in old_tetramino_blocks:    
                        if whiteless_array[y][x] != '.':
                            if matrix[y + new_index[0]][x + new_index[1]] == ".":
                                pass
                            else:
            
                                collision = True    
                
                if collision == True:
                    break

      
                         
        return collision, new_index, whiteless_array 

    def tetramino_to_array(self, tetramino_array1 = 5):
        
        if tetramino_array1 == 5:
        #get the tetramino ready to be made into a 2Darray
            tetramino_array = self.tetramino.split('\n')
        else:
            tetramino_array = tetramino_array1.split('\n')


        for line in range(len(tetramino_array)):
            tetramino_array[line] = tetramino_array[line].split()
  
        #Make the tetramino into 2Darray
        tetramino_array  = np.array(tetramino_array)

        return tetramino_array
    

def read_commands(commands):
    interpreted_commands = ""
    for command in commands:
        if command == '?':
            interpreted_commands += command
        else:
            interpreted_commands += command + " "
    return interpreted_commands
            

def step(matrix, score, register):
    #Check if a line in the matrix is completely filled, if so clear it 
    #and increment score
    for y in range(len(matrix)):
        if '.' not in matrix[y]:
            matrix[y] = ['.']*WIDTH
            score += 100
            register += 1
    return score, register

def given(matrix):
    for y in range(len(matrix)):
        matrix[y] = raw_input().split()
    return matrix
    
def print_matrix(matrix):
    #join the strings together with spaces, and then print them
    for y in matrix:
        print ' '.join(y)
          
    return 




if __name__ == '__main__':
    main()


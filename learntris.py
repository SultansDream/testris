#!/usr/bin/python2.7

import sys

WIDTH = 10
LENGTH = 22

#Command Codes
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


 
def main():
    #Initialize our matrix with '.' to denote empty spaces
    matrix = [['.']*WIDTH for y in xrange(LENGTH)]
    #Initialize score and register to 0
    score = 0
    register = 0
    tetramino_objects = {}

    while True:
        commands = raw_input()
    
        for command in commands.split():
            if command == EXIT_CODE:
                sys.exit()

            elif command == PRINT_CODE:
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
                tetramino_objects[command] = Tetramino(tetraminos[command])
           
            elif command == DISPLAY_CODE:
                for tetramino in tetramino_objects:
                    tetramino_objects[tetramino].print_tetramino()
            
            elif command == ROTATE_CODE:
                for tetramino in tetramino_objects:
                    tetramino_objects[tetramino].rotate()

            elif command == CODE_SPACE:
                print ""
            else:
                pass

class Tetramino:
    
    def __init__(self, tetramino):
        self.tetramino = tetramino
        
    def rotate(self):
        self.split_tetramino = self.tetramino.split('\n')
        self.rotated_tetramino = ""
        for column in range(0, len(self.split_tetramino[0]), 2):
            for row in reversed(self.split_tetramino):
                self.rotated_tetramino += row[column] + " "
            self.rotated_tetramino.rstrip()
            self.rotated_tetramino += "\n"
        self.tetramino = self.rotated_tetramino.rstrip("\n")
        return self.tetramino
    
    def print_tetramino(self):
        print self.tetramino
  

    
def step(matrix, score, register):
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
    for y in matrix:
        print ' '.join(y)
          
    return 




if __name__ == '__main__':
    main()


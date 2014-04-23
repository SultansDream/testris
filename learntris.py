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
 
def main():
    #Initialize our matrix with '.' to denote empty spaces
    matrix = [['.']*WIDTH for y in xrange(LENGTH)]
   

    while True:
        command = raw_input()
       
        if command == EXIT_CODE:
            sys.exit()

        elif command == PRINT_CODE:
            print_matrix(matrix)

        elif command == GIVEN_CODE:
            matrix = given(matrix)

        elif command == CLEAR_CODE:
            matrix =  [['.']*WIDTH for y in xrange(LENGTH)]

        elif command == SCORE_CODE:
            print score()

        elif command == REGISTER_CODE:
            print register()
        
        else:
            pass
    
def register():
    return 0

def score():
    return 0

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


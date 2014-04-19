#!/usr/bin/python2.7

import sys

WIDTH = 10
LENGTH = 22
PRINT_CODE = 'p'
EXIT_CODE = 'q'
 
def main():
    command_line_arguments = sys.argv
    

 
    command = raw_input()
    if len(command_line_arguments) >= 2:
        arguments(command_line_arguments)
    elif command == EXIT_CODE:
        pass
    elif command == PRINT_CODE:
        draw(WIDTH, LENGTH)
    else:
        pass
  


def arguments(command_line_arguments):
   
    if PRINT_CODE in command_line_arguments:
        draw(WIDTH, LENGTH)
    elif EXIT_CODE in command_line_arguments:
        pass
    else:
        print "no valid arguments passed, pass an argument to do something"
    

    return
    
def draw(width, length):
    matrix = ""
    for y in range(length):
        for x in range(width):
            matrix += "." + " "
        matrix.rstrip()
        matrix += "\n"
    
    print matrix
    return 




if __name__ == '__main__':
    main()


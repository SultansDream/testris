#!/usr/bin/python2.7

import sys

WIDTH = 10
LENGTH = 22

def main():
    command_line_arguments = sys.argv
    print command_line_arguments[0]
    
    if len(command_line_arguments) >= 2:
        arguments(command_line_arguments)
    else:
        print "no arguments passed"


def arguments(command_line_arguments):
   
    print_code = 'p'
    quit = 'q'
    if print_code in command_line_arguments:
        draw(WIDTH, LENGTH)
    elif quit in command_line_arguments:
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


#!/usr/bin/env python
# Brainfuck Interpreter
# python 3.0
# Semester work for Python FIT CVUT
# Author Tomas Sykora, jr.
# Fell free to use or modify !!!


if __name__ == "__main__":
        bCode = input()
        if len(bCode) == 0: print("nic si nezadal tupce") 
        array = [0] * 30000
        i = 0
        pointer = 0
        for x in range(0, len(bCode)):
        	if bCode[x] == '>': #move pointer to left
        		pointer += 1
        		if pointer >= len(bCode):
        			print("Wrong format of Brainfuck code!! Last char int your code is to move to next cell, but there is no reason to do that, cause this is last piece of code!! Keep the code clean")
        	elif bCode[x] == '<': #move pointer to rigth
        		pointer -= 1
        		if i >= len(bCode):
        			print("Wrong format of Brainfuck code!! Last char int your code is to move to previous cell, but there is no reason to do that, cause this is last piece of code!! Keep the code clean")
        	elif bCode[x] == '+': #increment of the actual cell
        		array[pointer] += 1
        	elif bCode[x] == '-': #decrement of the actual cell
        		array[pointer] -= 1
        	elif bCode[x] == '.': #actual printing of the actual cell value
        		print(chr(array[i]), end="")
        	elif bCode[x] == ',':
        		array[pointer] == input();




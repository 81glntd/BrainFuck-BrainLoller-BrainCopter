#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
class BrainFuck:
    """Interpret of brainfuck."""
    
    def __init__(self, data, memory=b'\x00', memory_pointer=0):
        """Initialization of brainfuck interpreter."""
        
        # data of program
        self.data = data
        
        # initializcodeation of varialbles
        self.memory = bytearray(memory)
        self.memory_pointer = memory_pointer
        
        # DEBUG and tests
        # a) output memory
        self.output = ''

        try:
            with open(data, mode='r') as f:
                self.c = f.read()
        except:
            self.c = data

        self._interpret(self.c)
    
    #
    # for test purposes
    #
    def get_memory(self):
        # Do not forget to change this acording to your implementation
        return self.memory

    def _interpret(self, c):
        """This is where the magic is going on"""

        c_i = 0
        while c_i < len(c):

            #incrementation
            if c[c_i] == '+':
                self.memory[self.memory_pointer] += 1
                #too much
                if self.memory[self.memory_pointer] == 256:
                    self.memory[self.memory_pointer] = 0

            #decrementation
            elif c[c_i] == '-':
                self.memory[self.memory_pointer] -= 1
                if self.memory[self.memory_pointer] == -1:
                    self.memory[self.memory_pointer] = 255

            #right shift
            elif c[c_i] == '>':
                self.memory_pointer += 1
                #make bigger
                if len(self.memory) == self.memory_pointer:
                    self.memory += bytearray([0])

            #left shift
            elif c[c_i] == '<':
                if self.memory_pointer > 0:
                    self.memory_pointer -= 1

            #read input
            elif c[c_i] == ',':
                self.memory[self.memory_pointer] = ord(sys.stdin.read(1))

            elif c[c_i] == '[':
                if self.memory[self.memory_pointer] == 0:
                    loop_counter = 1
                    while loop_counter > 0:
                        c_i += 1
                        helper = c[c_i]
                        if helper == '[':
                            loop_counter += 1
                        elif helper == ']':
                            loop_counter -= 1
            elif c[c_i] == ']':
                loop_counter = 1
                while loop_counter > 0:
                    c_i -= 1
                    helper = c[c_i]
                    if helper == '[':
                        loop_counter -= 1
                    elif helper == ']':
                        loop_counter += 1
                c_i -= 1
            elif c[c_i] == '.':
                print(chr(self.memory[self.memory_pointer]), end=r'')
            c_i += 1


class BrainLoller():
    """Class for managing brainloller."""
    
    def __init__(self, filename):
        """Initialization of brainloller"""
        
        # self.data contains parsed brainfuck code
        self.data = ''
        # ..which we give to interpreter
        self.program = BrainFuck(self.data)


class BrainCopter():
    """Class for managing braincopter."""
    
    def __init__(self, filename):
        """Initialization of braincopter."""
        
        # self.data contains parsed brainfuck code
        self.data = ''
        # ..which we give to interpreter
        self.program = BrainFuck(self.data)



#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class BrainFuck:
    """Interpret of brainfuck."""
    
    def __init__(self, data, memory=b'\x00', memory_pointer=0):
        """Initialization of brainfuck interpreter."""
        
        # data of program
        self.data = data
        
        # initialization of varialbles
        self.memory = memory
        self.memory_pointer = memory_pointer
        
        # DEBUG and tests
        # a) output memory
        self.output = ''
    
    #
    # for test purposes
    #
    def get_memory(self):
        # Do not forget to change this acording to your implementation
        return self.memory


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



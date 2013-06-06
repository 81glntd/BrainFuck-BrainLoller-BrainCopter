#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class BrainFuck:
    """Interpret of brainfuck."""
    
    def __init__(self, data, memory=b'\x00', memory_pointer=0):
        """Initialization of brainfuck interpreter."""
        
        # data of program
        self.data = data
        
        # initialization of varialbles
        self.memory = bytearray(memory)
        self.memory_pointer = memory_pointer
        
        # DEBUG and tests
        # a) output memory
        self.output = ''

        try:
            with open(data, mode='r') as f:
                self.code = f.read()
        except:
            self.code = data
    
    #
    # for test purposes
    #
    def get_memory(self):
        # Do not forget to change this acording to your implementation
        return self.memory

    def _interpret(self, code):
        """This is where the magic is going on"""
        i = 0
        while p < len(code):
            if source[source_position] == '+':
            output.increase()
        elif source[source_position] == '-':
            output.decrease()
        elif source[source_position] == '>':
            output.move_right()
        elif source[source_position] == '<':
            output.move_left()
        elif source[source_position] == ',':
            output.set(ord(sys.stdin.read(1)))
        elif source[source_position] == '[':
            if output.get() == 0:
                loop_counter = 1
                while loop_counter > 0:
                    source_position += 1
                    helper = source[source_position]
                    if helper == '[':
                        loop_counter += 1
                    elif helper == ']':
                        loop_counter -= 1
        elif source[source_position] == ']':
            loop_counter = 1
            while loop_counter > 0:
                source_position -= 1
                helper = source[source_position]
                if helper == '[':
                    loop_counter -= 1
                elif helper == ']':
                    loop_counter += 1
            source_position -= 1
        elif source[source_position] == '.':
            print(chr(output.get()), end=r'')
        elif source[source_position] == ',':
            if 0 <= source_position < 30000:
                x = input()
                output.set(x)
                source_position += 1
        source_position += 1


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



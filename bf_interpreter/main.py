"""
This is new branch to fix the fucking errors i have no idea where they came from !!!
"""



__author__ = 'Tomas Sykora sykorto6@fit.cvut.cz'
import sys


class Output():
    def __init__(self):
        self.actual_output = [0] * 30000
        self.positon = 0

    def get(self):
        return self.actual_output[self.positon]

    def set(self, value):
        self.actual_output[self.positon] = value

    def increase(self):
        self.actual_output[self.positon] += 1

    def decrease(self):
        self.actual_output[self.positon] -= 1

    def move_right(self):
        self.positon += 1
        if self.positon > len(self.actual_output):
            print("!!! Error you have reached maximum size of BrainFuck working array !!!")

    def move_left(self):
        self.positon -= 1
        if self.positon < 0:
            print("!!! Error you have reached outside of BrainFuck working array !!!")




def file_source(filename):
    with open(filename, encoding='utf-8') as bf_source_file:
        source = bf_source_file.read()
        return source


def prompt_source():
    print("You have not chosen any file please enter BrainFuck code manually")
    source = input()
    return source


def get_input():
    NONARGV = []
    if sys.argv[1:] == NONARGV:
        source = prompt_source()
        return source
    elif sys.argv[1] == '-f':
        return file_source(sys.argv[2])


def execute_interpreter(source):

    output = Output()
    source_position = 0
    loop_open = 0
    loop_close = 0
    while len(source) >= source_position:
        #current = source[source_position]
        if source[source_position] == '':
            print("Jsi v piči")
            return
        elif source[source_position] == '+':
            output.increase()
        elif source[source_position] == '-':
            output.decrease()
        elif source[source_position] == '>':
            output.move_right()
        elif source[source_position] == '<':
            output.move_left()
        elif source[source_position] == '[':
            loop_open = source_position
        elif source[source_position] == ']':
            if output.get() > 0:
                source_position = loop_open
        elif source[source_position] == '.':
            #print(output.actual_output)
            print(chr(output.get()), end=r'')
        source_position += 1






if __name__ == "__main__":
    code = get_input()
    print(code)
    execute_interpreter(code)





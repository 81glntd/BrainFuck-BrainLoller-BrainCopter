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
    """
    Returns variable source which contains BrainFuck source code
    file_source is handling BrainFuck source code from file using 'switcher' -f
    :param filename:
    """
    with open(filename, encoding='utf-8') as bf_source_file:
        source = bf_source_file.read()
        print(source)


def prompt_source():
    print("You have not chosen any file please enter BrainFuck code manually")
    source = input()
    print(source)
    return source


def get_input():
    NONARGV = []
    if sys.argv[1:] == NONARGV:
        source = prompt_source()
    elif sys.argv[1] == '-f':
        file_source(sys.argv[2])
    return source


def plus(bf_output, position, value):
    bf_output[position] += value
    return bf_output


def minus(bf_output, position, value):
    bf_output[position] += value
    return bf_output


def execute_interpreter(source):
    output = Output()
    print(output.actual_output)
    while len(source):
        source_position = 0
        loop_open = 0
        loop_close = 0
        if source[source_position] == '[':
            loop_open = source_position





if __name__ == "__main__":
    execute_interpreter(get_input())





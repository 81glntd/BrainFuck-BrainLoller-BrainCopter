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

    def increase






def file_source(filename):
    """
    Returns variable source which contains brainfuck source code
    file_source is handling brainfuck source code from file using 'switcher' -f
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
    bf_output = [0] * 30000
    print(bf_output.count(0))
    for source_position in range(0, len(source)):
        if source[source]:



if __name__ == "__main__":
    execute_interpreter(get_input())





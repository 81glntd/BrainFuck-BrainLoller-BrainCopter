__author__ = 'Tomas Sykora sykorto6@fit.cvut.cz'
import sys


def file_source(filename):
    """
    Returns variable source which contains brainfuck source code
    file_source is handling brainfuck source code from file using 'switcher' -f
    :param filename:
    """
    with open(filename, encoding='utf-8') as bf_source_file:
        source = bf_source_file.read()
        print(source)


if __name__ == "__main__":
    NONARGV = []
    if sys.argv[1:] == NONARGV:
        print("You have not chosen any file please enter BrainFuck code manualy")
        source = input()
        print(source)
    else: #sys.argv[1] == '-f':
        file_source(sys.argv[2])

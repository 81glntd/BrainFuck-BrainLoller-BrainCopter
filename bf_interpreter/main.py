__author__ = 'Tomas Sykora sykorto6@fit.cvut.cz'
import sys

def file_source(filename):
    with open(sys.argv, encoding='utf-8') as bf_source_file:
        source = bf_source_file.read()
        print(source)


if __name__ == "__main__":
    if sys.argv:
        file_source(sys.argv[1])

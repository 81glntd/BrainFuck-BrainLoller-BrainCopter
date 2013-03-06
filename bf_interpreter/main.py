__author__ = 'Tomas Sykora sykorto6@fit.cvut.cz'
import sys

def file_source(filename):
    with open(filename, encoding='utf-8') as bf_source_file:
        source = bf_source_file.read()
        print(source)


if __name__ == "__main__":
    if sys.argv[1] == '-f':
        file_source(sys.argv[2])
    elif sys.argv[1] == None:
        print("neni soubor")
        source = input()
        print(source)

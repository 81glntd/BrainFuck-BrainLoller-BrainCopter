#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class PNGWrongHeaderError(Exception):
    """Výjimka oznamující, že načítaný soubor zřejmě není PNG-obrázkem."""
    pass


class PNGNotImplementedError(Exception):
    """Výjimka oznamující, že PNG-obrázek má strukturu, kterou neumíme zpracovat."""
    pass


class PngReader():
    """Třída pro práci s PNG-obrázky."""
    
    def __init__(self, filepath):
        with open(filepath, mode='rb') as f:
            self.png_source = f.read()

        #check if the file is PNG
        if self.png_source[:8] != b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a':
            raise PNGWrongHeaderError()

    def _read_png(self):
        pointer = 8
        self.chunks = []
        while pointer < len(self.png_source):
            h = self.png_source[pointer:pointer+4]
            chunk_size = h[0] * 256 ** 3 + h[1] * 256 ** 2 + h[2] * 256 + h[3]
            self.chunks += [{'type': self.png_source[pointer + 4:pointer + 8],
                             'data': self.png_source[pointer + 8: pointer + 8 + chunk_size]}]
            pointer += 12 + chunk_size

        
        # RGB-data obrázku jako seznam seznamů řádek,
        #   v každé řádce co pixel, to trojce (R, G, B)
        self.rgb = []


if __name__ == "__main__":
    PngReader(filepath="test_data/sachovnice.png")
    print("1 done")
    PngReader(filepath="test_data/sachovnice.jpg")
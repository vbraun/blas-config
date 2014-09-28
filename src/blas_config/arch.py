# -*- coding: utf-8 -*-
"""
Architecture-Dependent Settings
"""

import sys
import platform


class BinaryFormat(object):
    
    instance = None

    def __init__(self):
        if BinaryFormat.instance is not None:
            raise RuntimeError('the BinaryFormat class is a singleton')
        BinaryFormat.instance = self
        if sys.platform.startswith('linux'):
            self.__class__ = BinFmtELF
        elif sys.platform.startswith('darwin'):
            self.__class__ = BinFmtMACHO
        elif sys.platform.startswith('win32'):
            self.__class__ = BinFmtPE
        elif sys.platform.startswith('cygwin'):
            self.__class__ = BinFmtPE
        else:
            raise NotImplementedError('unknown platform')


class BinFmtELF(BinaryFormat):

    def shlib_ext(self):
        return '.so'


class BinFmtMACHO(BinaryFormat):

    def shlib_ext(self):
        return '.dylib'


class BinFmtPE(BinaryFormat):

    def shlib_ext(self):
        return '.dll'


binary_format = BinaryFormat()



class Bitwidth(object):
    
    instance = None

    BIT_32 = '32bit'
    BIT_64 = '64bit'

    def __init__(self):
        if Bitwidth.instance is not None:
            raise RuntimeError('the Bitwidth class is a singleton')
        Bitwidth.instance = self
        if sys.maxsize > 2**32:
            self._bitwidth = self.BIT_64
        else:
            self._bitwidth = self.BIT_32

    def override(self, bitwidth):
        if bitwidth == 32:
            self._bitwidth = self.BIT_32
        elif bitwidth == 64:
            self._bitwidth = self.BIT_64
        else:
            raise ValueError('unknown bitwidth: {0}, must be 32 or 64'
                             .format(bitwidth))

    def is_32(self):
        return self._bitwidth == self.BIT_32

    def is_64(self):
        return self._bitwidth == self.BIT_64


bitwidth = Bitwidth()

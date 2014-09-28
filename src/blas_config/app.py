# -*- coding: utf-8 -*-
"""
Main entry point
"""

import sys
import os


CBLAS_TEMPLATE = """
prefix=/usr
libdir=/usr/lib64
exec_prefix=${prefix}
includedir=${prefix}/include

Name: cblas
Description: C Basic Linear Algebra Subprograms (CBLAS)
Version: 1.0
URL: http://www.gnu.org/software/gsl
Libs: -L${libdir} -lblas
Libs.private: -lm
Cflags: -I${includedir}
"""


def write_cblas_pc(path):
    name = 'cblas.pc'
    os.makedirs(path)
    with open(os.path.join(path, name), 'wt') as f:
        f.write(CBLAS_TEMPLATE)



class Application(object):
    
    def cblas(self, prefer=None):
        if prefer is None:
            prefer = []
        else:
            prefer = str(prefer).split(',')
        from factory_cblas import cblas
        pc = cblas.favourite(*prefer)
        print('Using CBLAS: {0}'.format(pc.get_name()))
        return pc
    

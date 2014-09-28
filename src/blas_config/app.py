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
    
    def __init__(self, pkg_config_path, version):
        self._pkg_config_path = pkg_config_path
        self._version = version

    def cblas(self, prefer=None):
        if prefer is None:
            prefer = []
        else:
            prefer = str(prefer).split(',')
        from blas_config.factory_cblas import cblas
        pc = cblas.favourite(*prefer)
        print('Using CBLAS: {0}'.format(pc.get_name()))
        return pc

    def f77blas(self, prefer=None):
        if prefer is None:
            prefer = []
        else:
            prefer = str(prefer).split(',')
        from factory_f77blas import f77blas
        pc = f77blas.favourite(*prefer)
        print('Using F77BLAS: {0}'.format(pc.get_name()))
        return pc
    
    def write_pc(self, pc):
        path = self._pkg_config_path
        try:
            os.makedirs(path)
        except OSError:
            pass  # exists already?
        with open(os.path.join(path, pc.name_pc), 'wt') as f:
            f.write(pc.to_string())
        
    def initial_setup(self, search, prefer):
        """
        Initial setup

        This is called at the end of "make install".
        """
        self.write_pc(self.cblas(prefer))
        self.write_pc(self.f77blas(prefer))

        

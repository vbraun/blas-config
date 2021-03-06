# -*- coding: utf-8 -*-
"""
Main entry point
"""

import sys
import os
from blas_config.factory import FactoryCBLAS, FactoryF77BLAS



class Application(object):
    
    def __init__(self, pkg_config_path, version):
        self._pkg_config_path = pkg_config_path
        self._version = version

    def cblas(self, search=None, prefer=None):
        if prefer is None:
            prefer = []
        else:
            prefer = str(prefer).split(',')
        cblas = FactoryCBLAS(override_prefix=search)
        pc = cblas.favourite(*prefer)
        if pc is None:
            print('Error: No CBLAS implementation found')
        else:
            print('Using CBLAS: {0}'.format(pc.get_name()))
        return pc

    def f77blas(self, search=None, prefer=None):
        if prefer is None:
            prefer = []
        else:
            prefer = str(prefer).split(',')
        f77blas = FactoryF77BLAS(override_prefix=search)
        pc = f77blas.favourite(*prefer)
        if pc is None:
            print('Error: No F77BLAS implementation found')
        else:
            print('Using F77BLAS: {0}'.format(pc.get_name()))
        return pc
    
    def write_pc(self, pc):
        if pc is None:
            print('Error: No implementation found, aborting')
            sys.exit(1)
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
        print('Initial setup')
        if search is not None:
            print('Searching at {0}'.format(search))
        if prefer is not None:
            print('Preferring the following installations: {0}'.format(prefer))
        cblas_pc = self.cblas(search, prefer)
        if cblas_pc is None and search is not None:
            print('Searching for system CBLAS installations instead...')
            cblas_pc = self.cblas(None, prefer)

        f77blas_pc = self.f77blas(search, prefer)
        if f77blas_pc is None and search is not None:
            print('Searching for system F77BLAS installations instead...')
            f77blas_pc = self.f77blas(None, prefer)

        self.write_pc(cblas_pc)
        self.write_pc(f77blas_pc)

        

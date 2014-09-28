# -*- coding: utf-8 -*-
"""
Factory for PkgConfig instances
"""

import os
import glob

import logging
log = logging.getLogger()

from blas_config.base import Description, BlasConfigException, PkgConfig
from blas_config.arch import shlib_ext


class Factory(object):

    def __init__(self, name_pc):
        self.name_pc = name_pc
        self.valid_configurations = list()
        self.named_configurations = dict()

    def __repr__(self):
        return '\n'.join(map(repr, self.valid_configurations))

    def favourite(self):
        return self.valid_configurations[0]

    def shlib_ext(self):
        

    def resolve_glob(self, filename_glob):
        """
        Resolve a filename glob to an absolute path that we can use
        """
        filename_glob = filename_glob.format(shlib=shlib_ext())
        log.debug('looking for %s', filename_glob)
        for path in glob.glob(filename_glob):
            path = os.path.abspath(path)
            log.debug('using %s', path)
            return path
        log.debug('no match found')
        raise BlasConfigException('no match found for {0}'.format(filename_glob))
        
    def guess_prefix(self, paths):
        """
        Extract the common path prefix
        """
        prefix = os.path.commonprefix(paths)
        return prefix

    def search(self, identifier, description, 
               header_globs, library_globs, cflags=None):
        try:
            headers = map(self.resolve_glob, header_globs)
            libraries = map(self.resolve_glob, library_globs)
        except BlasConfigException:
            log.debug('cannot find %s, ignoring', identifier)
            return
        prefix = self.guess_prefix(headers + libraries)
        pc = PkgConfig(self.name_pc, description, 
                       prefix)
        self.named_configurations[identifier] = pc
        self.valid_configurations.append(pc)




cblas = Factory('cblas.pc')



mkl = cblas.search(
    'intel_mkl', 
    Description(
        'Intel-MKL',
        'Intel Math Kernel Library', 
        'http://www.intel.com', 
        '11.2.0.090'), 
    [], ['/opt/intel/composer*/mkl/lib/*/libmkl_gnu_thread*.{shlib}']
)



# -*- coding: utf-8 -*-
"""
Base Class for Compile/Link information
"""

import os

import logging
log = logging.getLogger()

from blas_config.arch import binary_format


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



PKG_CONFIG_TEMPLATE = """
prefix={prefix}
exec_prefix=${{prefix}}
libdir={libdir}
includedir={includedir}

{body}
"""



class BlasConfigException(Exception):
    """
    Exception to be thrown if something is not a usable BLAS.
    """


class FileSystemObjects(object):

    def __init__(self, path, filenames):
        self.path = path
        self.filenames = tuple(filenames)

    def make_expander(self, prefix):
        raise NotImplementedError

    def expand(self, prefix):
        expander = self.make_expander(prefix)
        self.path = expander(self.path)
        self.filenames = tuple(map(expander, self.filenames))


    def validate_file(self, filename):
        """
        Hook for additional validation of a file
        """
        return True

    def validate(self):
        for filename in self.filenames:
            if not os.path.isabs(filename):
                filename = os.path.join(self.path, filename)
            if not os.path.exists(filename):
                log.debug('does not exist: %s', filename)
                return False
            if not self.validate_file(filename):
                log.debug('does not validate: %s', filename)
                return False
            log.debug('found: %s', filename)
        return True

class Includes(FileSystemObjects):

    def make_expander(self, prefix):
        path = self.path.format(prefix=prefix)
        shlib = binary_format.shlib_ext()
        def expand_one(name):
            return name.format(prefix=prefix, includedir=path, shlib=shlib)
        return expand_one

class Libs(FileSystemObjects):

    def make_expander(self, prefix):
        path = self.path.format(prefix=prefix)
        shlib = binary_format.shlib_ext()
        def expand_one(name):
            return name.format(prefix=prefix, libdir=path, shlib=shlib)
        return expand_one


class PkgConfig(object):
    
    def __init__(self, name_pc,
                 prefix, libdir, includedir,
                 body):
        self.name_pc = name_pc
        self.prefix = prefix
        self.libdir = libdir
        self.includedir = includedir
        self.body = body

    def __repr__(self):
        return '[{0:<10}] {1}'.format(self.name_pc, self.get_name())

    def get_name(self):
        for line in self.body.splitlines():
            line = line.strip()
            if line.startswith('Name:'):
                return line[5:].strip()
        raise ValueError('no name in body')

    def to_string(self):
        return PKG_CONFIG_TEMPLATE.format(
            prefix=self.prefix,
            libdir=self.libdir,
            includedir=self.includedir,
            body=self.body,
        )

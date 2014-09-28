# -*- coding: utf-8 -*-
"""
Base Class for Compile/Link information
"""

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



PKG_CONFIG_TEMPLATE = """
prefix={prefix}
exec_prefix=${{prefix}}

Name: {name}
Description: C Basic Linear Algebra Subprograms (CBLAS)
Version: 1.0
URL: http://www.gnu.org/software/gsl
Libs: -L${libdir} -lblas
Libs.private: -lm
Cflags: -I${includedir}
"""



class BlasConfigException(Exception):
    """
    Exception to be thrown if something is not a usable BLAS.
    """


class Description(object):
    
    def __init__(self, name, description, url, version=None):
        self.name = name
        self.description = description
        self.url = url
        self.version = version if version else 'unknown version'

    def __repr__(self):
        return '{0} ({1})'.format(self.name, self.version)


class PkgConfig(object):
    
    def __init__(self, name_pc, description, 
                 prefix, libdir=None, exec_prefix=None, includedir=None,
                 libs=None, libs_private=None, cflags=None):
        self.metadata = description
        self.name_pc = name_pc
        if libdir is None:
            libdir = os.path.join(prefix, 'lib')
        if exec_prefix is None:
            exec_prefix = prefix
        if includedir is None:
            includedir = os.path.join(prefix, 'include')
        if libs is None:
            libs = ''
        if libs_private is None:
            libs_private = ''
        if cflags is None:
            cflags = ''

    def __repr__(self):
        return '[{0:<10}] {1}'.format(self.name_pc, self.description)

    def to_string(self):
        return PKG_CONFIG_TEMPLATE.format(
            prefix=self.prefix,
            name=self.metadata.name,
            description=self.metadata.description,
            url=self.metadata.url,
            version=self.metadata.version,
            libs=self.libs,
            libs_private=self.libs_private,
            cflags=self.cflags,
        )

# -*- coding: utf-8 -*-
"""
Factory for PkgConfig instances
"""

import os
import glob
import textwrap

import logging
log = logging.getLogger()

from blas_config.base import PkgConfig, Includes, Libs
from blas_config.arch import bitwidth


class FactoryBase(object):

    def __init__(self, name_pc, override_prefix=None, version=None):
        self.name_pc = name_pc
        self.override_prefix = override_prefix
        self.valid_configurations = list()
        self.version = version if version is not None else '1.0'

    def __repr__(self):
        return '\n'.join(map(repr, self.valid_configurations))

    def favourite(self, *prefer):
        if len(self.valid_configurations) == 0:
            return None
        remaining = self.valid_configurations
        for keyword in prefer:
            keyword = keyword.lower().strip()
            good = []
            for config in remaining:
                if keyword in config.get_name().lower():
                    good.append(config)
            if len(good) == 0:
                pass  # ignore that keyword
            elif len(good) == 1:
                return good[0]
            else:
                remaining = good  # restrict search
        return remaining[0]

    def search(self, prefix, includes, libs, body):
        if self.override_prefix is not None:
            prefix = self.override_prefix
        includes.expand(prefix)
        libs.expand(prefix)
        if not includes.validate():
            return
        if not libs.validate():
            return
        pc = PkgConfig(self.name_pc, self.version, 
                       prefix, libs.path, includes.path, 
                       textwrap.dedent(body).strip())
        self.valid_configurations.append(pc)

    def search32(self, *args):
        if bitwidth.is_32():
            self.search(*args)

    def search64(self, *args):
        if bitwidth.is_64():
            self.search(*args)



class FactoryCBLAS(FactoryBase):

    def __init__(self, override_prefix=None, version=None):
        super(FactoryCBLAS, self).__init__(
            'cblas.pc', override_prefix=override_prefix, version=version)
        from blas_config.factory_cblas import build
        build(self)


class FactoryF77BLAS(FactoryBase):

    def __init__(self, override_prefix=None, version=None):
        super(FactoryF77BLAS, self).__init__(
            'f77blas.pc', override_prefix=override_prefix, version=version)
        from blas_config.factory_f77blas import build
        build(self)


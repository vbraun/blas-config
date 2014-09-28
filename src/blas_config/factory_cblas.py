# -*- coding: utf-8 -*-
"""
CBLAS PkgConfig Build Data
"""

import os
import logging
log = logging.getLogger()

from blas_config.base import Includes, Libs


def build(cblas):

    cblas.search64(
        # /opt/intel/mkl/tools/mkl_link_tool -p no -c gnu_c -a intel64 -opts
        # /opt/intel/mkl/tools/mkl_link_tool -p no -c gnu_c -a intel64 -libs
        '/opt/intel/mkl',
        Includes('{prefix}/include', [
            '{includedir}/mkl.h',
        ]),
        Libs('{prefix}/lib/intel64', [
            'libmkl_gf_lp64{shlib}', 
            'libmkl_sequential{shlib}', 
            'libmkl_core{shlib}',
        ]),
        """    
        Name: Intel-MKL Sequential
        Description: Intel Math Kernel Library
        Version: {version}
        URL: https://software.intel.com/en-us/intel-mkl
        Libs: -L${libdir} -Wl,--no-as-needed -lmkl_gf_lp64 -lmkl_sequential -lmkl_core ${rpath}
        Libs.private: -lpthread -lm
        Cflags: -m64 -I${includedir}
        """,
    )

    cblas.search32(
        # /opt/intel/mkl/tools/mkl_link_tool -p no -c gnu_c -a ia-32 -opts
        # /opt/intel/mkl/tools/mkl_link_tool -p no -c gnu_c -a ia-32 -libs
        '/opt/intel/mkl',
        Includes('{prefix}/include', [
            '{includedir}/mkl.h',
        ]),
        Libs('{prefix}/lib/ia32', [
            'libmkl_gf{shlib}', 
            'libmkl_sequential{shlib}', 
            'libmkl_core{shlib}',
        ]),
        """    
        Name: Intel-MKL Sequential
        Description: Intel Math Kernel Library
        Version: {version}
        URL: https://software.intel.com/en-us/intel-mkl
        Libs: -L${libdir} -Wl,--no-as-needed -lmkl_gf_lp64 -lmkl_sequential -lmkl_core ${rpath}
        Libs.private: -lpthread -lm
        Cflags: -m32 -I${includedir}
        """,
    )
    

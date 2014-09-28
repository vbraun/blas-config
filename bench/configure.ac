# Boilerplate
AC_PREREQ([2.69])
AC_INIT([blas-benchmark], [1.0], [vbraun.name@gmail.com])
AM_INIT_AUTOMAKE

# We need a working C compiler
AC_PROG_CC

# These headers must be available
AC_CHECK_HEADERS([memory.h stdlib.h string.h sys/time.h unistd.h])

# Standard functions
AC_FUNC_MALLOC
AC_CHECK_FUNCS([gettimeofday])

# Standard libraries
AC_CHECK_LIB(m, sqrt)
AC_CHECK_LIB(rt, clock_gettime)

# Use cblas.pc to set CBLAS_CFLAGS and CBLAS_LIBS variables. See
# src/Makefile.am for how to use them in the compiler calls
PKG_CHECK_MODULES([CBLAS], [cblas])

# Paths and files
AC_CONFIG_MACRO_DIR([m4])
AC_CONFIG_SRCDIR([src/bench.h])
AC_CONFIG_HEADERS([src/config.h])

AC_CONFIG_FILES([
  Makefile
  src/Makefile
])

# Write output, last statement
AC_OUTPUT

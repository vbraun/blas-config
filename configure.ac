# Boilerplate
AC_PREREQ([2.69])
AC_INIT([blas-config], [1.0], [vbraun.name@gmail.com])
AM_INIT_AUTOMAKE

# Require Python 2.6 or later
AM_PATH_PYTHON([2.6])

# Paths and files
AC_CONFIG_MACRO_DIR([m4])
AC_CONFIG_SRCDIR([src/blas_config])
AC_CONFIG_FILES([
  Makefile
  src/Makefile
  src/blas_config/Makefile
])


AC_ARG_VAR(
    BLAS_CONFIG_SEARCH, 
    [Directory to search for libraries instead of the default
     prefix. Use this if your BLAS installation lives in a
     non-standard location (e.g. anywhere inside the user home
     directory). Matches will take precedence over system
     installations.]
)


AC_ARG_VAR(
    BLAS_CONFIG_PREFER, 
    [Comma-separated list of preferred BLAS implementations.]
)

# Write output, last statement
AC_OUTPUT


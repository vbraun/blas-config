SUBDIRS = blas_config

bin_SCRIPTS = blas-config
CLEANFILES = $(bin_SCRIPTS)
EXTRA_DIST = blas-config.in

pkgconfigdir = $(libdir)/pkgconfig
do_substitution = \
	sed -e 's,[@]pythondir[@],$(pythondir),g' \
            -e 's,[@]pkgconfigdir[@],$(pkgconfigdir),g' \
	    -e 's,[@]PYTHON[@],$(PYTHON),g' \
	    -e 's,[@]PACKAGE[@],$(PACKAGE),g' \
	    -e 's,[@]VERSION[@],$(VERSION),g' 

blas-config: blas-config.in Makefile
	$(do_substitution) < $(srcdir)/blas-config.in > blas-config
	chmod +x blas-config

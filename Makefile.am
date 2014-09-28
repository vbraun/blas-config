ACLOCAL_AMFLAGS = -I m4
SUBDIRS = src

pkgconfigdir = $(libdir)/pkgconfig
install-exec-hook:
	$(bindir)/blas-config initial-setup \
	    --search=$(BLAS_CONFIG_SEARCH) \
	    --prefer=$(BLAS_CONFIG_PREFER)
	cd bench && PKG_CONFIG_LIBDIR=$(pkgconfigdir) \
	    ./configure \
	        --prefix=$(prefix)
	cd bench && make
	cd bench && make -j1 install
	$(bindir)/blas-benchmark

mostlyclean-local:
	cd $(srcdir)/bench \
	    && (test -f Makefile || PKG_CONFIG_PATH=`pwd`/dummy_pkgconfig ./configure ) \
	    && make mostlyclean

clean-local: mostlyclean-local
	cd $(srcdir)/bench \
	    && (test -f Makefile || PKG_CONFIG_PATH=`pwd`/dummy_pkgconfig ./configure ) \
	    && make clean

distclean-local: clean-local
	cd $(srcdir)/bench \
	    && (test -f Makefile || PKG_CONFIG_PATH=`pwd`/dummy_pkgconfig ./configure ) \
	    && make distclean

maintainer-clean-local: distclean-local
	cd $(srcdir)/bench \
	    && (test -f Makefile || PKG_CONFIG_PATH=`pwd`/dummy_pkgconfig ./configure ) \
	    && make maintainer-clean

EXTRA_DIST = bench

dist-hook:
	cd $(distdir)/bench \
	    && PKG_CONFIG_PATH=`pwd`/dummy_pkgconfig ./configure \
	    && make distclean 
	find $(distdir) -name "*~" -exec rm {} \;

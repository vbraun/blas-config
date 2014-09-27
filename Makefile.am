ACLOCAL_AMFLAGS = -I m4
SUBDIRS = src

pkgconfigdir = $(libdir)/pkgconfig
install-exec-hook:
	$(bindir)/blas-config
	cd bench && PKG_CONFIG_LIBDIR=$(pkgconfigdir) \
	    ./configure \
	        --prefix=$(prefix)
	cd bench && make
	cd bench && make -j1 install
	$(bindir)/blas-benchmark

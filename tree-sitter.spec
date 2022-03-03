#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tree-sitter
Version  : 0.20.6
Release  : 3
URL      : https://github.com/tree-sitter/tree-sitter/archive/v0.20.6/tree-sitter-0.20.6.tar.gz
Source0  : https://github.com/tree-sitter/tree-sitter/archive/v0.20.6/tree-sitter-0.20.6.tar.gz
Summary  : An incremental parsing system for programming tools
Group    : Development/Tools
License  : MIT
Requires: tree-sitter-lib = %{version}-%{release}
Requires: tree-sitter-license = %{version}-%{release}

%description
# tree-sitter
[![Build Status](https://github.com/tree-sitter/tree-sitter/workflows/CI/badge.svg)](https://github.com/tree-sitter/tree-sitter/actions)
[![Build status](https://ci.appveyor.com/api/projects/status/vtmbd6i92e97l55w/branch/master?svg=true)](https://ci.appveyor.com/project/maxbrunsfeld/tree-sitter/branch/master)
[![DOI](https://zenodo.org/badge/14164618.svg)](https://zenodo.org/badge/latestdoi/14164618)

%package dev
Summary: dev components for the tree-sitter package.
Group: Development
Requires: tree-sitter-lib = %{version}-%{release}
Provides: tree-sitter-devel = %{version}-%{release}
Requires: tree-sitter = %{version}-%{release}

%description dev
dev components for the tree-sitter package.


%package lib
Summary: lib components for the tree-sitter package.
Group: Libraries
Requires: tree-sitter-license = %{version}-%{release}

%description lib
lib components for the tree-sitter package.


%package license
Summary: license components for the tree-sitter package.
Group: Default

%description license
license components for the tree-sitter package.


%prep
%setup -q -n tree-sitter-0.20.6
cd %{_builddir}/tree-sitter-0.20.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1646329060
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
make  %{?_smp_mflags}  PREFIX=/usr LIBDIR=/usr/lib64


%install
export SOURCE_DATE_EPOCH=1646329060
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tree-sitter
cp %{_builddir}/tree-sitter-0.20.6/LICENSE %{buildroot}/usr/share/package-licenses/tree-sitter/0d88b1fe204b8601d0cf7c9de8c2bc4d64a627a6
%make_install PREFIX=/usr LIBDIR=/usr/lib64

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/tree_sitter/api.h
/usr/include/tree_sitter/parser.h
/usr/lib64/libtree-sitter.so
/usr/lib64/pkgconfig/tree-sitter.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libtree-sitter.so.0
/usr/lib64/libtree-sitter.so.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tree-sitter/0d88b1fe204b8601d0cf7c9de8c2bc4d64a627a6

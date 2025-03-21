#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: fbbd4e3
#
# Source0 file verified with key 0x2C8DF587A6D4AAC1 (nicolas.fella@kde.org)
#
Name     : kded
Version  : 6.12.0
Release  : 240
URL      : https://download.kde.org/stable/frameworks/6.12/kded-6.12.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.12/kded-6.12.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.12/kded-6.12.0.tar.xz.sig
Source2  : 2C8DF587A6D4AAC1.pkey
Summary  : Extensible deamon for providing system level services
Group    : Development/Tools
License  : CC0-1.0 LGPL-2.0
Requires: kded-bin = %{version}-%{release}
Requires: kded-data = %{version}-%{release}
Requires: kded-license = %{version}-%{release}
Requires: kded-man = %{version}-%{release}
Requires: kded-services = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KDED
Central daemon of KDE work spaces
## Introduction
KDED stands for KDE Daemon which isn't very descriptive.
KDED runs in the background and performs a number of small tasks.
Some of these tasks are built in, others are started on demand.

%package bin
Summary: bin components for the kded package.
Group: Binaries
Requires: kded-data = %{version}-%{release}
Requires: kded-license = %{version}-%{release}
Requires: kded-services = %{version}-%{release}

%description bin
bin components for the kded package.


%package data
Summary: data components for the kded package.
Group: Data

%description data
data components for the kded package.


%package dev
Summary: dev components for the kded package.
Group: Development
Requires: kded-bin = %{version}-%{release}
Requires: kded-data = %{version}-%{release}
Provides: kded-devel = %{version}-%{release}
Requires: kded = %{version}-%{release}

%description dev
dev components for the kded package.


%package license
Summary: license components for the kded package.
Group: Default

%description license
license components for the kded package.


%package man
Summary: man components for the kded package.
Group: Default

%description man
man components for the kded package.


%package services
Summary: services components for the kded package.
Group: Systemd services
Requires: systemd

%description services
services components for the kded package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 2C8DF587A6D4AAC1' gpg.status
%setup -q -n kded-6.12.0
cd %{_builddir}/kded-6.12.0
pushd ..
cp -a kded-6.12.0 buildavx2
popd

%build
## build_prepend content
# Make sure the package only builds if kdoctools has been updated first
sed -i -r -e 's,(KF.?DocTools \$\{KF.?_DEP_VERSION\})(.*\))$,\1 REQUIRED \2,' CMakeLists.txt || :
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1742517512
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
## build_prepend content
# Make sure the package only builds if kdoctools has been updated first
sed -i -r -e 's,(KF.?DocTools \$\{KF.?_DEP_VERSION\})(.*\))$,\1 REQUIRED \2,' CMakeLists.txt || :
## build_prepend end
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1742517512
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kded
cp %{_builddir}/kded-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kded/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kded-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kded/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kded-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kded/20079e8f79713dce80ab09774505773c926afa2a || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kded6
/usr/bin/kded6

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kded6.desktop
/usr/share/dbus-1/interfaces/org.kde.kded6.xml
/usr/share/dbus-1/services/org.kde.kded6.service
/usr/share/qlogging-categories6/kded.categories
/usr/share/qlogging-categories6/kded.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/lib64/cmake/KF6KDED/KF6KDEDConfig.cmake
/usr/lib64/cmake/KF6KDED/KF6KDEDConfigVersion.cmake

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kded/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kded/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0

%files man
%defattr(0644,root,root,0755)
/usr/share/man/ca/man8/kded6.8
/usr/share/man/es/man8/kded6.8
/usr/share/man/fr/man8/kded6.8
/usr/share/man/it/man8/kded6.8
/usr/share/man/man8/kded6.8
/usr/share/man/nl/man8/kded6.8
/usr/share/man/sl/man8/kded6.8
/usr/share/man/tr/man8/kded6.8
/usr/share/man/uk/man8/kded6.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/plasma-kded6.service

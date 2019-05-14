#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kded
Version  : 5.58.0
Release  : 16
URL      : https://download.kde.org/stable/frameworks/5.58/kded-5.58.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.58/kded-5.58.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.58/kded-5.58.0.tar.xz.sig
Summary  : Extensible deamon for providing system level services
Group    : Development/Tools
License  : LGPL-2.0 LGPL-2.1
Requires: kded-bin = %{version}-%{release}
Requires: kded-data = %{version}-%{release}
Requires: kded-lib = %{version}-%{release}
Requires: kded-license = %{version}-%{release}
Requires: kded-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : qtbase-dev mesa-dev

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
Requires: kded-lib = %{version}-%{release}
Requires: kded-bin = %{version}-%{release}
Requires: kded-data = %{version}-%{release}
Provides: kded-devel = %{version}-%{release}
Requires: kded = %{version}-%{release}
Requires: kded = %{version}-%{release}

%description dev
dev components for the kded package.


%package lib
Summary: lib components for the kded package.
Group: Libraries
Requires: kded-data = %{version}-%{release}
Requires: kded-license = %{version}-%{release}

%description lib
lib components for the kded package.


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


%prep
%setup -q -n kded-5.58.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557796132
mkdir -p clr-build
pushd clr-build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1557796132
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kded
cp COPYING.LGPL-2 %{buildroot}/usr/share/package-licenses/kded/COPYING.LGPL-2
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/kded/COPYING.LIB
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kded5

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kded5.desktop
/usr/share/dbus-1/interfaces/org.kde.kded5.xml
/usr/share/dbus-1/services/org.kde.kded5.service
/usr/share/kservicetypes5/kdedmodule.desktop
/usr/share/xdg/kded.categories

%files dev
%defattr(-,root,root,-)
/usr/lib64/cmake/KDED/KDEDConfig.cmake
/usr/lib64/cmake/KDED/KDEDConfigVersion.cmake
/usr/lib64/cmake/KDED/KDEDTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KDED/KDEDTargets.cmake

%files lib
%defattr(-,root,root,-)
/usr/lib64/libkdeinit5_kded5.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kded/COPYING.LGPL-2
/usr/share/package-licenses/kded/COPYING.LIB

%files man
%defattr(0644,root,root,0755)
/usr/share/man/ca/man8/kded5.8
/usr/share/man/de/man8/kded5.8
/usr/share/man/es/man8/kded5.8
/usr/share/man/it/man8/kded5.8
/usr/share/man/man8/kded5.8
/usr/share/man/nl/man8/kded5.8
/usr/share/man/pt/man8/kded5.8
/usr/share/man/pt_BR/man8/kded5.8
/usr/share/man/ru/man8/kded5.8
/usr/share/man/sv/man8/kded5.8
/usr/share/man/uk/man8/kded5.8

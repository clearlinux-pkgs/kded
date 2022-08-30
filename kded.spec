#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kded
Version  : 5.97.0
Release  : 96
URL      : https://download.kde.org/stable/frameworks/5.97/kded-5.97.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.97/kded-5.97.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.97/kded-5.97.0.tar.xz.sig
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
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : kdoctools-dev
BuildRequires : kservice-dev

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

%description services
services components for the kded package.


%prep
%setup -q -n kded-5.97.0
cd %{_builddir}/kded-5.97.0

%build
## build_prepend content
# Make sure the package only builds if kdoctools has been updated first
sed -i -r -e 's,(KF.?DocTools \$\{KF.?_DEP_VERSION\})(.*\))$,\1 REQUIRED \2,' CMakeLists.txt
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1661879753
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1661879753
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kded
cp %{_builddir}/kded-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kded/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kded-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kded/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kded-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kded/20079e8f79713dce80ab09774505773c926afa2a || :
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
/usr/share/qlogging-categories5/kded.categories
/usr/share/qlogging-categories5/kded.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/lib64/cmake/KDED/KDEDConfig.cmake
/usr/lib64/cmake/KDED/KDEDConfigVersion.cmake

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kded/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kded/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0

%files man
%defattr(0644,root,root,0755)
/usr/share/man/ca/man8/kded5.8
/usr/share/man/ca@valencia/man8/kded5.8
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

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/plasma-kded.service

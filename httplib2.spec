#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : httplib2
Version  : 0.17.2
Release  : 57
URL      : https://files.pythonhosted.org/packages/1b/f0/a35a448afea308aeb6a1430dbcfb46f4cef11360cbc18f22af6e567bb847/httplib2-0.17.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/1b/f0/a35a448afea308aeb6a1430dbcfb46f4cef11360cbc18f22af6e567bb847/httplib2-0.17.2.tar.gz
Summary  : A comprehensive HTTP client library.
Group    : Development/Tools
License  : MIT
Requires: httplib2-python = %{version}-%{release}
Requires: httplib2-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
Introduction
============
httplib2 is a comprehensive HTTP client library, httplib2.py supports many
features left out of other HTTP libraries.

%package python
Summary: python components for the httplib2 package.
Group: Default
Requires: httplib2-python3 = %{version}-%{release}

%description python
python components for the httplib2 package.


%package python3
Summary: python3 components for the httplib2 package.
Group: Default
Requires: python3-core
Provides: pypi(httplib2)

%description python3
python3 components for the httplib2 package.


%prep
%setup -q -n httplib2-0.17.2
cd %{_builddir}/httplib2-0.17.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1586810373
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python python2/httplib2test.py || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

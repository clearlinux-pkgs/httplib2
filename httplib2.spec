#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : httplib2
Version  : 0.9.1
Release  : 10
URL      : https://pypi.python.org/packages/source/h/httplib2/httplib2-0.9.1.tar.gz
Source0  : https://pypi.python.org/packages/source/h/httplib2/httplib2-0.9.1.tar.gz
Summary  : A comprehensive HTTP client library.
Group    : Development/Tools
License  : MIT
Requires: httplib2-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
No detailed description available

%package python
Summary: python components for the httplib2 package.
Group: Default

%description python
python components for the httplib2 package.


%prep
%setup -q -n httplib2-0.9.1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
python python2/httplib2test.py || :
%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*

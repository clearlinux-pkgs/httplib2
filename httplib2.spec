#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : httplib2
Version  : 0.11.3
Release  : 38
URL      : http://pypi.debian.net/httplib2/httplib2-0.11.3.tar.gz
Source0  : http://pypi.debian.net/httplib2/httplib2-0.11.3.tar.gz
Summary  : A comprehensive HTTP client library.
Group    : Development/Tools
License  : MIT
Requires: httplib2-python3
Requires: httplib2-python
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : setuptools

%description
A comprehensive HTTP client library, ``httplib2`` supports many features left out of other HTTP libraries.
        
        **HTTP and HTTPS**
          HTTPS support is only available if the socket module was compiled with SSL support.
        
        
        **Keep-Alive**
          Supports HTTP 1.1 Keep-Alive, keeping the socket open and performing multiple requests over the same connection if possible.
        
        
        **Authentication**
          The following three types of HTTP Authentication are supported. These can be used over both HTTP and HTTPS.
        
          * Digest
          * Basic
          * WSSE
        
        **Caching**

%package python
Summary: python components for the httplib2 package.
Group: Default
Requires: httplib2-python3

%description python
python components for the httplib2 package.


%package python3
Summary: python3 components for the httplib2 package.
Group: Default
Requires: python3-core

%description python3
python3 components for the httplib2 package.


%prep
%setup -q -n httplib2-0.11.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523289783
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python python2/httplib2test.py || :
%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
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

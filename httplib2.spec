#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : httplib2
Version  : 0.12.0
Release  : 41
URL      : https://files.pythonhosted.org/packages/ce/ed/803905d670b52fa0edfdd135337e545b4496c2ab3a222f1449b7256eb99f/httplib2-0.12.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/ce/ed/803905d670b52fa0edfdd135337e545b4496c2ab3a222f1449b7256eb99f/httplib2-0.12.0.tar.gz
Summary  : A comprehensive HTTP client library.
Group    : Development/Tools
License  : MIT
Requires: httplib2-python = %{version}-%{release}
Requires: httplib2-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

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
Requires: httplib2-python3 = %{version}-%{release}

%description python
python components for the httplib2 package.


%package python3
Summary: python3 components for the httplib2 package.
Group: Default
Requires: python3-core

%description python3
python3 components for the httplib2 package.


%prep
%setup -q -n httplib2-0.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542174130
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python python2/httplib2test.py || :
%install
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

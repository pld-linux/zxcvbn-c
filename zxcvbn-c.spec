Summary:	C/C++ implementation of the zxcvbn password strength estimation
Summary(pl.UTF-8):	Implementacja C/C++ algorytmu zxcvbn estymacji jakości haseł
Name:		zxcvbn-c
Version:	2.5
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/tsyrogit/zxcvbn-c/releases
Source0:	https://github.com/tsyrogit/zxcvbn-c/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	cdc0f679b10b195ad3883f8adf16babc
Patch0:		%{name}-install.patch
URL:		https://github.com/tsyrogit/zxcvbn-c
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C/C++ implementation of the zxcvbn password strength estimation.

%description -l pl.UTF-8
Implementacja C/C++ algorytmu zxcvbn estymacji jakości haseł.

%package devel
Summary:	Header files for zxcvbn library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki zxcvbn
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for zxcvbn library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki zxcvbn.

%package static
Summary:	Static zxcvbn library
Summary(pl.UTF-8):	Statyczna biblioteka zxcvbn
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static zxcvbn library.

%description static -l pl.UTF-8
Statyczna biblioteka zxcvbn.

%prep
%setup -q
%patch0 -p1

%build
CC="%{__cc}" \
CFLAGS="%{rpmcflags} -Wall -Wextra -Wdeclaration-after-statement" \
CPPFLAGS="%{rpmcppflags}" \
CXX="%{__cxx}" \
CXXFLAGS="%{rpmcxxflags} -Wall -Wextra" \
%{__make} package

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.md
%attr(755,root,root) %{_bindir}/zxcvbn-dictgen
%attr(755,root,root) %{_libdir}/libzxcvbn.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libzxcvbn.so.0
%{_datadir}/zxcvbn

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libzxcvbn.so
%{_includedir}/zxcvbn

%files static
%defattr(644,root,root,755)
%{_libdir}/libzxcvbn.a

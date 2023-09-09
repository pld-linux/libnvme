Summary:	C Library for NVM Express on Linux
Summary(pl.UTF-8):	Biblioteka C do obsługi NVM Express na Linuksie
Name:		libnvme
Version:	1.5
Release:	2
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://github.com/linux-nvme/libnvme/releases
Source0:	https://github.com/linux-nvme/libnvme/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	8289e988a3244a35cc326aa564a7a727
URL:		https://github.com/linux-nvme/libnvme
BuildRequires:	dbus-devel
BuildRequires:	json-c-devel >= 0.13
BuildRequires:	keyutils-devel
BuildRequires:	meson >= 0.50.0
BuildRequires:	ninja >= 1.5
BuildRequires:	openssl-devel >= 1.1.0
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3.6
BuildRequires:	python3-devel >= 1:3.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	swig-python >= 2
Requires:	json-c >= 0.13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libnvme provides type definitions for NVMe specification structures,
enumerations, and bit fields, helper functions to construct, dispatch,
and decode commands and payloads, and utilities to connect, scan, and
manage nvme devices on a Linux system.

%description -l pl.UTF-8
libnvme dostarcza definicje typów, struktur, wartości liczbowych i pól
bitowych, funkcje pomocnicze do tworzenia, przesyłania i dekodowania
poleceń oraz danych oraz narzędzia do dołączania, wyszukiwania i
zarządzania urządzeniami nvme w systemie Linux.

%package devel
Summary:	Header files for libnvme
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libnvme
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-devel
Requires:	json-c-devel >= 0.13
Requires:	keyutils-devel
Requires:	openssl-devel >= 1.1.0

%description devel
Header files for libnvme.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libnvme.

%package static
Summary:	Static libnvme library
Summary(pl.UTF-8):	Statyczna biblioteka libnvme
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libnvme library.

%description static -l pl.UTF-8
Statyczna biblioteka libnvme.

%package -n python3-libnvme
Summary:	libnvme Python bindings
Summary(pl.UTF-8):	Wiązania Pythona do libnvme
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python3-libs >= 1:3.6

%description -n python3-libnvme
libnvme Python bindings.

%description -n python3-libnvme -l pl.UTF-8
Wiązania Pythona do libnvme.

%prep
%setup -q

%build
%meson build \
	-Ddocs=man \
	-Djson-c=enabled \
	-Dkeyutils=enabled \
	-Dlibdbus=enabled \
	-Dpython=enabled

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%py3_comp $RPM_BUILD_ROOT%{py3_sitedir}
%py3_ocomp $RPM_BUILD_ROOT%{py3_sitedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_libdir}/libnvme.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnvme.so.1
%attr(755,root,root) %{_libdir}/libnvme-mi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnvme-mi.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnvme.so
%attr(755,root,root) %{_libdir}/libnvme-mi.so
%{_includedir}/libnvme.h
%{_includedir}/libnvme-mi.h
%dir %{_includedir}/nvme
%{_includedir}/nvme/*.h
%{_pkgconfigdir}/libnvme.pc
%{_pkgconfigdir}/libnvme-mi.pc
%{_mandir}/man2/nbft_*.2*
%{_mandir}/man2/nvme_*.2*
%{_mandir}/man2/nvmf_*.2*

%files static
%defattr(644,root,root,755)
%{_libdir}/libnvme.a
%{_libdir}/libnvme-mi.a

%files -n python3-libnvme
%defattr(644,root,root,755)
%dir %{py3_sitedir}/libnvme
%{py3_sitedir}/libnvme/__init__.py
%{py3_sitedir}/libnvme/nvme.py
%{py3_sitedir}/libnvme/__pycache__
%attr(755,root,root) %{py3_sitedir}/libnvme/_nvme.cpython-*.so

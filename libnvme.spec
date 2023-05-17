Summary:	C Library for NVM Express on Linux
Name:		libnvme
Version:	1.4
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://github.com/linux-nvme/libnvme/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	7877177dd736950b4115455d99f1d386
URL:		https://github.com/linux-nvme/libnvme
BuildRequires:	dbus-devel
BuildRequires:	json-c-devel >= 0.13
BuildRequires:	keyutils-devel
BuildRequires:	meson >= 0.50.0
BuildRequires:	ninja
BuildRequires:	openssl-devel >= 1.1.0
BuildRequires:	pkgconfig
BuildRequires:	python3
BuildRequires:	python3-devel
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	swig-python
Requires:	json-c >= 0.13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libnvme provides type definitions for NVMe specification structures,
enumerations, and bit fields, helper functions to construct, dispatch,
and decode commands and payloads, and utilities to connect, scan, and
manage nvme devices on a Linux system.

%package devel
Summary:	Header files for libnvme
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libnvme.

%package static
Summary:	Static libnvme library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libnvme library.

%package -n python3-libnvme
Summary:	libnvme Python bindings
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python3

%description -n python3-libnvme
libnvme Python bindings.

%prep
%setup -q

%build
%meson build \
	-Djson-c=enabled \
	-Dkeyutils=enabled \
	-Dlibdbus=enabled \
	-Dpython=enabled

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

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

%files static
%defattr(644,root,root,755)
%{_libdir}/libnvme.a
%{_libdir}/libnvme-mi.a

%files -n python3-libnvme
%defattr(644,root,root,755)
%dir %{py3_sitedir}/libnvme
%{py3_sitedir}/libnvme/__init__.py
%attr(755,root,root) %{py3_sitedir}/libnvme/_nvme.cpython*.so
%{py3_sitedir}/libnvme/nvme.py

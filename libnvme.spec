Summary:	C Library for NVM Express on Linux
Name:		libnvme
Version:	1.2
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://github.com/linux-nvme/libnvme/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a549200fe692449d46802081da514cd0
URL:		https://github.com/linux-nvme/libnvme
BuildRequires:	json-c-devel >= 0.13
BuildRequires:	meson >= 0.48.0
BuildRequires:	ninja
BuildRequires:	openssl-devel >= 1.1.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	systemd-devel
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

%prep
%setup -q

%build
%meson build

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

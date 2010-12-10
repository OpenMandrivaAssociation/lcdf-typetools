Summary: Programs for manipulating PostScript Type 1 fonts
Name: lcdf-typetools
Version: 2.59
Release: %mkrel 5
Source: http://www.lcdf.org/type/%{name}-%{version}.tar.bz2
URL: http://www.lcdf.org/type/
Group: Publishing
License: GPL
BuildRequires: tetex-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description 
The LCDF Typetools package contains several programs for manipulating
PostScript Type 1, Type 1 multiple master, and PostScript-flavored
OpenType fonts.  LCDF Typetools includes the mmafm and mmpfb programs,
which were formerly distributed as part of a different package
(mminstance).

%prep
%setup

%build
%configure2_5x
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc NEWS README COPYING
%attr(0755,root,root) %{_bindir}/*
%attr(0644,root,root) %{_mandir}/man1/*
%{_datadir}/lcdf-typetools/*



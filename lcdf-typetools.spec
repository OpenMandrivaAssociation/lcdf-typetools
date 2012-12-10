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




%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 2.59-5mdv2011.0
+ Revision: 620057
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 2.59-4mdv2010.0
+ Revision: 429705
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 2.59-3mdv2009.0
+ Revision: 248323
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.59-1mdv2008.1
+ Revision: 136535
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Feb 24 2007 Giuseppe GhibÃ² <ghibo@mandriva.com> 2.59-1mdv2007.0
+ Revision: 125393
- %%mkrel.
- %%mkrel.
- Release: 2.59.
- Import lcdf-typetools

* Thu Jan 26 2006 Giusepp eGhibò <ghibo@mandriva.com> 2.37-1mdk
- Release: 2.37.

* Sat Aug 06 2005 Giuseppe Ghibò <ghibo@mandriva.com> 2.34-1mdk
- Release: 2.34.

* Sat Feb 12 2005 Giuseppe Ghibò <ghibo@mandrakesoft.com> 2.20-1mdk
- Release: 2.20.

* Sat Aug 28 2004 Giuseppe Ghibò <ghibo@mandrakesoft.com> 2.12-1mdk
- Release: 2.12.

* Tue Aug 10 2004 Giuseppe Ghibò <ghibo@mandrakesoft.com> 2.8-1mdk
- Release: 2.8.

* Tue Jul 20 2004 Giuseppe Ghibò <ghibo@mandrakesoft.com> 2.6-1mdk
- Release: 2.6.


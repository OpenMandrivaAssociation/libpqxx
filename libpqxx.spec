Summary:	The official C++ client API for PostgreSQL
Name:		libpqxx
Version:	4.0
Release:	2
Source:		http://pqxx.org/download/software/libpqxx/%name-%version.tar.gz
License:	GPLv2+
Group:		Development/Databases
Url:		http://pqxx.org/
BuildRequires:	postgresql-devel
BuildRequires:  xmlto
BuildRequires:  doxygen
BuildRequires:  pkgconfig
Obsoletes:	%mklibname pqxx 2

%description
This library works on top of the C-level API library, libpq. You will need
libpq in order to use libpqxx. 
The first thing you're likely to notice in programming with libpqxx is that
unlike other libraries, it revolves entirely around transactions. Transactions
are a central concept in database management systems, but they are widely
underappreciated among application developers. Another well-known open source
database system, MySQL, never even got around to implementing them at all in
their own engine, relying on a third-party replacement engine (now owned by
Oracle) to provide this functionality instead.

%package devel
Summary:        Headers for developing programs that will use %{name}
Group:          Development/C++
Requires:       %{name} = %{version}-%{release}
Obsoletes:	%mklibname pqxx 2 -d

%description devel
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q

%build
%configure2_5x \
    --enable-shared \
    --disable-static
%make

%install

%makeinstall_std

# cleanup
rm -f %{buildroot}%{_libdir}/*.la

%files
%_libdir/libpqxx-*.so

%files devel
%_bindir/pqxx-config
%_includedir/pqxx/*
%_libdir/libpqxx.so
%_libdir/pkgconfig/libpqxx.pc


%changelog
* Sat Feb 11 2012 Oden Eriksson <oeriksson@mandriva.com> 4.0-2
+ Revision: 773287
- various fixes

* Mon Nov 28 2011 Alexander Khrukin <akhrukin@mandriva.org> 4.0-1
+ Revision: 734993
- version update 4.0

* Mon May 02 2011 Funda Wang <fwang@mandriva.org> 3.1-3
+ Revision: 661756
- fix build with gcc 4.6

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 3.1-2mdv2011.0
+ Revision: 602596
- rebuild

* Tue Feb 16 2010 Funda Wang <fwang@mandriva.org> 3.1-1mdv2010.1
+ Revision: 506436
- drop old patches
- new version 3.1

* Wed Dec 09 2009 Funda Wang <fwang@mandriva.org> 3.0.2-1mdv2010.1
+ Revision: 475325
- new version 3.0.2

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.6.9-7mdv2010.0
+ Revision: 425690
- rebuild

* Sun Dec 21 2008 Oden Eriksson <oeriksson@mandriva.com> 2.6.9-6mdv2009.1
+ Revision: 317030
- rebuild

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 2.6.9-5mdv2009.0
+ Revision: 264890
- rebuild early 2009.0 package (before pixel changes)

* Thu Jun 12 2008 Anssi Hannula <anssi@mandriva.org> 2.6.9-4mdv2009.0
+ Revision: 218535
- fix undefined symbol errors by making freemem_result_data public (P4
  from upstream)
- fix tests for cleaned gcc 4.3 c++ headers (P3)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed May 21 2008 Oden Eriksson <oeriksson@mandriva.com> 2.6.9-3mdv2009.0
+ Revision: 209722
- added a gcc43 patch from fedora

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 2.6.9-2mdv2008.1
+ Revision: 170954
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- fix description-line-too-long

* Sat Feb 02 2008 Funda Wang <fwang@mandriva.org> 2.6.9-1mdv2008.1
+ Revision: 161377
- New version 2.6.9
- Move main.so into main package

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Sat Jan 13 2007 Olivier Thauvin <nanardon@mandriva.org> 2.6.8-4mdv2007.0
+ Revision: 108358
- rebuild for latest libpq

* Mon Dec 11 2006 Nicolas Lécureuil <neoclust@mandriva.org> 2.6.8-3mdv2007.1
+ Revision: 94800
- Add BuildRequires
- Rebuild

* Thu Nov 16 2006 Laurent Montel <lmontel@mandriva.com> 2.6.8-2mdv2007.1
+ Revision: 84676
- Add buildrequires
- Import libpqxx


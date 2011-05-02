Summary:	The official C++ client API for PostgreSQL
Name:		libpqxx
Version:	3.1
Release:	%mkrel 3
Source:		http://pqxx.org/download/software/libpqxx/%name-%version.tar.gz
Patch0:		libpqxx-3.1-gcc46.patch
License:	GPLv2+
Group:		Development/Databases
Url:		http://pqxx.org/
BuildRequires:	postgresql-devel
BuildRequires:  xmlto
BuildRequires:  doxygen
BuildRequires:  pkgconfig
Obsoletes:	%mklibname pqxx 2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%patch0 -p0

%build
%configure2_5x \
    --enable-shared \
    --disable-static
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%_libdir/libpqxx-*.so

%files devel
%defattr(-,root,root)
%_bindir/pqxx-config
%_includedir/pqxx/*
%_libdir/libpqxx.la
%_libdir/libpqxx.so
%_libdir/pkgconfig/libpqxx.pc

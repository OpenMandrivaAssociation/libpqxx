%define major %(echo %{version} |cut -d. -f1-2)
%define libname	%mklibname pqxx
%define devname	%mklibname pqxx -d

Summary:	The official C++ client API for PostgreSQL
Name:		libpqxx
Version:	7.9.2
Release:	1
License:	GPLv2+
Group:		Development/Databases
Url:		https://pqxx.org/
Source0:	https://github.com/jtv/libpqxx/archive/refs/tags/%{version}.tar.gz
Source100:	libpqxx.rpmlintrc
BuildRequires:  doxygen
BuildRequires:  xmlto
BuildRequires:	postgresql-devel
BuildRequires:	pkgconfig(python2)

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

%package -n %{libname}
Summary:        Headers for developing programs that will use %{name}
Group:          System/Libraries
Obsoletes:	libpqxx < 4.0-4

%description -n %{libname}
This package contains the shared library for %{name}.

%package -n %{devname}
Summary:        Headers for developing programs that will use %{name}
Group:          Development/C++
Requires:       %{libname} = %{version}-%{release}
Obsoletes:	libpqxx-devel < 4.0-4

%description -n %{devname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%autosetup -p1
# fix spurious permissions
chmod -x COPYING

export CXXFLAGS="%{optflags} -std=gnu++20"
%configure --enable-shared --disable-static

%build
%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/libpqxx-%{major}.so

%files -n %{devname}
%{_includedir}/pqxx/*
%{_libdir}/libpqxx.so
%{_libdir}/pkgconfig/libpqxx.pc

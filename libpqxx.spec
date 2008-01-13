%define name		libpqxx
%define version		2.6.8

%define lib_name %mklibname pqxx 2


%define __libtoolize /bin/true

Summary:	Libpqxx is the official C++ client API for PostgreSQL
Name:		%{name}
Version:	%{version}
Release:	%mkrel 5
Source:		%name-%version.tar.bz2
License:	GPL
Group:		Graphical desktop/KDE
Url:		http://thaiopensource.org/development/libpqxx
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	postgresql-devel
BuildRequires:  xmlto
BuildRequires:  doxygen
BuildRequires:  pkgconfig

%description
This library works on top of the C-level API library, libpq. You will need libpq 
in order to use libpqxx. 
The first thing you're likely to notice in programming with libpqxx is that unlike 
other libraries, it revolves entirely around transactions. Transactions are a 
central concept in database management systems, but they are widely 
underappreciated among application developers. Another well-known open source 
database system, MySQL, never even got around to implementing them at all in their 
own engine, relying on a third-party replacement engine (now owned by Oracle) to 
provide this functionality instead.

%prep
%setup -q

%build

%configure2_5x \
		--disable-debug \
		--enable-shared \
		--disable-static \
%if "%{_lib}" != "lib"
    --enable-libsuffix="%(A=%{_lib}; echo ${A/lib/})" \
%endif
		--disable-rpath 
		#--enable-final

%make

%install
rm -Rf %{buildroot}

%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%package -n %{lib_name}
Summary:        Main library for %{name}
Group:          System/Libraries
Provides:       %{name} = %{version}-%{release}


%description -n %{lib_name}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n %{lib_name}-devel
Summary:        Headers for developing programs that will use %{name}
Group:          Development/C++
Requires:       %{lib_name} = %{version}-%{release}
Provides:       pqxx-devel = %{version}-%{release}

%description -n %{lib_name}-devel
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%post -n %{lib_name} -p /sbin/ldconfig

%postun -n %{lib_name} -p /sbin/ldconfig

%files -n %{lib_name}
%defattr(-,root,root)
%_libdir/libpqxx-2.6.8.so

%files -n %{lib_name}-devel
%defattr(-,root,root)
%_bindir/pqxx-config
%_includedir/pqxx/*
%_libdir/libpqxx.la
%_libdir/libpqxx.so
%_libdir/pkgconfig/libpqxx.pc




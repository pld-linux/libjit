Summary:	Just-In-Time Compiler Library
Summary(pl):	Biblioteka kompilatora do interpretacji kodu
Name:		libjit
Version:	0.0.4
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://www.southern-storm.com.au/download/%{name}-%{version}.tar.gz
# Source0-md5:	eda01981d60a996434d3d4e36c84d6c2
URL:		http://www.southern-storm.com.au/libjit.html
BuildRequires:	autoconf
BuildRequires:	automake >= 1.6
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libjit library has an extensive set of routines that takes care of
the bulk of the Just-In-Time compilation process, without tying the
programmer down with language or bytecode specifics.

Unlike other systems such as the JVM, .NET, Parrot, and LLVM, libjit
is not a virtual machine in its own right. It is the foundation upon
which a number of different virtual machines, dynamic scripting
languages, etc, can be built.

%description -l pl
Biblioteka libjit posiada rozszerzalny zestaw bibliotek bior±cych
udzia³ w procesie kompilacji Just-In-Time, bez zmuszania programisty
do zni¿ania siê do poziomu jêzyka lub bytecodu.

W przeciwieñstwie do innych systemów jak JVM, .NET, Parrot lub LLVM,
libjit nie jest normaln± maszyn± wirtualn±. Bazuje na ró¿nych
maszynach wirtualnych, dynamicznych jêzykach skryptowych które mo¿e
budowaæ.

%package devel
Summary:	Just-In-Time Compiler Library - development files
Summary(pl):	Biblioteka kompilatora do interpretacji kodu - pliki dla programistów
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description devel
Just-In-Time Compiler Library - development files.

%description devel -l pl
Biblioteka kompilatora do interpretacji kodu - pliki dla programistów.

%package static
Summary:	Just-In-Time Compiler Library - static files
Summary(pl):	Biblioteka kompilatora do interpretacji kodu - wersja statyczna
Group:		Development/Languages
Requires:	%{name}-devel = %{version}-%{release}

%description static
Just-In-Time Compiler Library - static libraries.

%description static -l pl
Biblioteka kompilatora do interpretacji kodu - biblioteka statyczna.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}
%{__make} check

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc README NEWS ChangeLog AUTHORS
%attr(755,root,root) %{_libdir}/libjit*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libjit*.so
%{_libdir}/libjit*.la
%{_includedir}/jit
%{_mandir}/man?/*
%{_infodir}/libjit.info*

%files static
%defattr(644,root,root,755)
%{_libdir}/libjit*.a

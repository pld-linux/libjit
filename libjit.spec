#
# Conditional build:
%bcond_without	tests	# "make check"
#
Summary:	Just-In-Time Compiler Library
Summary(pl.UTF-8):	Biblioteka kompilatora do interpretacji kodu
Name:		libjit
Version:	0.1.0
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://download.savannah.gnu.org/releases/dotgnu-pnet/%{name}-%{version}.tar.gz
# Source0-md5:	d6e3f83ad74ebfc20cc47d1c8913b343
Patch0:		%{name}-format.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-am.patch
URL:		http://www.gnu.org/software/dotgnu/pnet.html
BuildRequires:	autoconf
BuildRequires:	automake >= 1.6
BuildRequires:	libtool
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libjit library has an extensive set of routines that takes care of
the bulk of the Just-In-Time compilation process, without tying the
programmer down with language or bytecode specifics.

Unlike other systems such as the JVM, .NET, Parrot, and LLVM, libjit
is not a virtual machine in its own right. It is the foundation upon
which a number of different virtual machines, dynamic scripting
languages, etc., can be built.

%description -l pl.UTF-8
Biblioteka libjit posiada rozszerzalny zestaw bibliotek biorących
udział w procesie kompilacji Just-In-Time, bez zmuszania programisty
do zniżania się do poziomu specyfiki języka lub bajtkodu.

W przeciwieństwie do innych systemów (takich jak JVM, .NET, Parrot czy
LLVM), libjit nie jest pełnoprawną maszyną wirtualną. Jest to baza, na
której można zbudować wiele różnych maszyn wirtualnych, dynamicznych
języków skryptowych itp.

%package devel
Summary:	Just-In-Time Compiler Library - development files
Summary(pl.UTF-8):	Biblioteka kompilatora do interpretacji kodu - pliki dla programistów
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Just-In-Time Compiler Library - development files.

%description devel -l pl.UTF-8
Biblioteka kompilatora do interpretacji kodu - pliki dla programistów.

%package static
Summary:	Just-In-Time Compiler Library - static files
Summary(pl.UTF-8):	Biblioteka kompilatora do interpretacji kodu - wersja statyczna
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Just-In-Time Compiler Library - static libraries.

%description static -l pl.UTF-8
Biblioteka kompilatora do interpretacji kodu - biblioteka statyczna.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%if %{with tests}
%{__make} check
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc README NEWS ChangeLog AUTHORS
%attr(755,root,root) %{_libdir}/libjit.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libjit.so.0
%attr(755,root,root) %{_libdir}/libjitdynamic.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libjitdynamic.so.0
%attr(755,root,root) %{_libdir}/libjitplus.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libjitplus.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libjit.so
%attr(755,root,root) %{_libdir}/libjitdynamic.so
%attr(755,root,root) %{_libdir}/libjitplus.so
%{_libdir}/libjit.la
%{_libdir}/libjitdynamic.la
%{_libdir}/libjitplus.la
%{_includedir}/jit
%{_mandir}/man3/libjit.3*
%{_infodir}/libjit.info*

%files static
%defattr(644,root,root,755)
%{_libdir}/libjit.a
%{_libdir}/libjitdynamic.a
%{_libdir}/libjitplus.a

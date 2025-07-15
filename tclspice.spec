Summary:	TclSpice - improved version of Berkeley Spice
Summary(pl.UTF-8):	TclSpice - ulepszona wersja Berkeley Spice
Name:		tclspice
Version:	0.2.15
Release:	1
License:	BSD
Group:		Applications/Engineering
Source0:	http://dl.sourceforge.net/tclspice/%{name}-%{version}.tar.gz
# Source0-md5:	aa69a0289f63183dc6e1306ef54da1e0
Patch0:		%{name}-ac_fuckery_fix.patch
URL:		http://tclspice.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	blt-devel > 2.4u-11
BuildRequires:	tcl-devel >= 8.3.4
BuildRequires:	tclreadline-devel > 2.1.0-1
Obsoletes:	ngspice-rework
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TclSpice is an improved version of Berkeley Spice designed to be used
with the Tcl/Tk scripting language. The project is open-source (BSD
license) and based upon the NG-Spice source code base with many
improvements.

%description -l pl.UTF-8
TclSpice to ulepszona wersja Berkeley Spice zaprojektowana do używania
z językiem skryptowym Tcl/Tk. Projekt ma otwarte źródła (na licencji
BSD) i jest oparty na kodzie źródłowym NG-Spice z wieloma
ulepszeniami.

%prep
%setup -q -n %{name}
%patch -P0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	CPPFLAGS="%{rpmcflags} -I/usr/include/ncurses" \
	--disable-debug \
	--enable-xspice \
	--with-tcl

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install contrib/scripts/liblook $RPM_BUILD_ROOT%{_bindir}/%{name}-liblook
install contrib/scripts/libprm $RPM_BUILD_ROOT%{_bindir}/%{name}-libprm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS DEVICES FAQ NEWS NOTES README contrib/scripts/*_readme contrib/ChangeLog
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/helpdir
%{_datadir}/%{name}/helpdir/*.idx
%{_datadir}/%{name}/helpdir/*.txt
%dir %{_datadir}/%{name}/scripts
%attr(755,root,root) %{_datadir}/%{name}/scripts/*
%{_datadir}/info/*.gz
%{_mandir}/man1/*.1*
#%{_desktopdir}/tkcvs.desktop
#%{_pixmapsdir}/tkcvs.png

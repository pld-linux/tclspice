Summary:	TclSpice - improved version of Berkeley Spice
Summary(pl):	TclSpice - ulepszona wersja Berkeley Spice
Name:		tclspice
Version:	0.2.15
Release:	1
License:	BSD
Group:		Applications/Engineering
Source0:	http://dl.sourceforge.net/tclspice/%{name}-%{version}.tar.gz
# Source0-md5:	aa69a0289f63183dc6e1306ef54da1e0
URL:		http://tclspice.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TclSpice is an improved version of Berkeley Spice designed to be
used with the Tcl/Tk scripting language. The project is open-source
(BSD license) and based upon the NG-Spice source code base with many
improvements.

%description -l pl
TclSpice to ulepszona wersja Berkeley Spice zaprojektowana do u¿ywania
z jêzykiem skryptowym Tcl/Tk. Projekt ma otwarte ¼ród³a (na licencji
BSD) i jest oparty na kodzie ¼ród³owym NG-Spice z wieloma
ulepszeniami.

%prep
%setup -q -n %{name}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	CPPFLAGS="%{rpmcflags} -I%{_includedir}/ncurses" \
	--disable-debug

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

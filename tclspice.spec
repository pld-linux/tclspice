Summary:	Tk interface for CVS
Summary(pl):	Interfejs Tk dla CVS
Name:		tclspice
Version:	0.2.15
Release:	1
License:	GPL
Group:		Applications/Engineering
Source0:	http://dl.sourceforge.net/tclspice/%{name}-%{version}.tar.gz
# Source0-md5:	aa69a0289f63183dc6e1306ef54da1e0
URL:		http://rtwo.sourceforge.net/SpiceWish.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TkCVS is a Tcl/Tk-based graphical interface to the CVS configuration
management system. It displays the status of the files in the current
working directory, and provides buttons and menus to execute CVS
commands on the selected files. TkDiff is included for browsing and
merging your changes.

%description -l pl
TkCVS jest opartym o Tcl/Tk graficznym interfejsem do systemu
zarz±dania wersjami CVS. Program wy¶wietla stan plików w aktualnym
katalogu roboczym, potrafi wy¶wietkiæ historiê wybranego pliku w
postaci wykresu oraz pozwala na wykonywanie poleceñ CVS przy u¿yciu
menu i guzików. W sk³ad pakietu wchodzi TkDiff - narzêdzie do
przegl±dania i ³±czenia naniesionych modyfikacji.

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
#install -d $RPM_BUILD_ROOT{%{_applnkdir}/Scientific,%{_pixmapsdir}}

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
#%{_applnkdir}/Development/tkcvs.desktop
#%{_pixmapsdir}/tkcvs.png

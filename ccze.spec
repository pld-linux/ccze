Summary:	A robust log colorizer
Summary(pl):	Program w C do kolorowania logów
Name:		ccze
Version:	0.2.1
Release:	1
Epoch:		1
License:	GPL
Group:		Aplikacje/Tekst
######		Unknown group!
Vendor:		PLD
Source0:	ftp://bonehunter.rulez.org/pub/ccze/stable/%{name}-%{version}.tar.gz
# Source-md5:	221966bce7c5f011eca38157241a0432
URL:		http://bonehunter.rulez.org/CCZE.html
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	pcre-devel >= 3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CCZE is a roboust and modular log colorizer, with plugins for apm,
exim, fetchmail, httpd, postfix, procmail, squid, syslog, ulogd,
vsftpd, xferlog and more.

%description -l pl
CCZE jest programem napisanym w C. Umo¿liwia kolorowanie logów
systemowych, ftp, www i mail. Posiada wtyczki, mo¿e korzystaæ z plików
konfiguracyjnych, umie generowaæ wyniki w postaci kolorowej strony
html.

%prep
%setup -q

%build
%configure --with-builtins=all
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_sysconfdir}
src/ccze-dump >%{buildroot}/%{_sysconfdir}/cczerc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog ChangeLog-0.1 NEWS README THANKS FAQ
%config %{_sysconfdir}/cczerc
%attr(755,root,root) %{_bindir}/ccze
%attr(755,root,root) %{_bindir}/ccze-cssdump
%{_includedir}/ccze.h
%{_mandir}/man1/ccze.1*
%{_mandir}/man1/ccze-cssdump.1*
%{_mandir}/man7/ccze-plugin.7*

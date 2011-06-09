# TODO:
# - fix outdated url
Summary:	A robust log colorizer
Summary(pl.UTF-8):	Program w C do kolorowania logów
Name:		ccze
Version:	0.2.1
Release:	3
Epoch:		1
License:	GPL
Group:		Applications/Text
Source0:	ftp://bonehunter.rulez.org/pub/ccze/stable/%{name}-%{version}.tar.gz
# Source0-md5:	221966bce7c5f011eca38157241a0432
Patch0:		%{name}-ldflags.patch
Patch1:		%{name}-segfault.patch
Patch2:		%{name}-fbsd.patch
Patch3:		%{name}-Wmulticharacter.patch
Patch4:		%{name}-error.patch
Patch5:		%{name}-tinfo.patch
Patch6:		%{name}-debian.patch
URL:		http://bonehunter.rulez.org/CCZE.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	pcre-devel >= 3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

#define		filterout_ld	-Wl,--as-needed

%description
CCZE is a roboust and modular log colorizer, with plugins for apm,
exim, fetchmail, httpd, postfix, procmail, squid, syslog, ulogd,
vsftpd, xferlog and more.

%description -l pl.UTF-8
CCZE jest programem napisanym w C. Umożliwia kolorowanie logów
systemowych, FTP, WWW i mail. Posiada wtyczki, może korzystać z plików
konfiguracyjnych, umie generować wyniki w postaci kolorowej strony
html.

%package devel
Summary:	Header file for CCZE plugins
Summary(pl.UTF-8):	Plik nagłówkowy dla wtyczek CCZE
Group:		Development/Libraries
Requires:	ncurses-devel >= 5.0
Requires:	pcre-devel >= 3.1
# doesn't require base

%description devel
Header file for CCZE plugins.

%description devel -l pl.UTF-8
Plik nagłówkowy dla wtyczek CCZE.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
%{__aclocal}
%{__autoheader}
%{__autoconf}
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
%configure \
	--with-builtins=all

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

src/ccze-dump >$RPM_BUILD_ROOT%{_sysconfdir}/cczerc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog ChangeLog-0.1 NEWS README THANKS FAQ
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/cczerc
%attr(755,root,root) %{_bindir}/ccze
%attr(755,root,root) %{_bindir}/ccze-cssdump
%{_mandir}/man1/ccze.1*
%{_mandir}/man1/ccze-cssdump.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/ccze.h
%{_mandir}/man7/ccze-plugin.7*

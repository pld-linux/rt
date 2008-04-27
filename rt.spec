# TODO:
# - check file permissions
# - check files in /usr/share/rt3/
# - check BuildRequires
# - check Requires (meta-packages for configurations with mod_perl/fcgi,
#   apache[12]/standalone server...?)
# - separate standalone server
#
%include	/usr/lib/rpm/macros.perl
Summary:	Request Tracker
Summary(pl.UTF-8):	Request Tracker - system do śledzenia zleceń
Name:		rt
Version:	3.6.6
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://download.bestpractical.com/pub/rt/release/%{name}-%{version}.tar.gz
# Source0-md5:	b626c906e7b33c8d1879c15ed744f7e3
Source1:	%{name}-apache_dir.conf
Source2:	%{name}-apache_vhost.conf
Patch0:		%{name}-layout.patch
Patch1:		%{name}-config.patch
URL:		http://www.bestpractical.com/rt/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	perl-Apache-Session >= 1.53
BuildRequires:	perl-CGI >= 2.78
BuildRequires:	perl-CGI-SpeedyCGI
BuildRequires:	perl-Cache-Cache
BuildRequires:	perl-Class-ReturnValue
BuildRequires:	perl-DBD-mysql
BuildRequires:	perl-DBI >= 1.18
BuildRequires:	perl-DBIx-DataSource >= 0.02
BuildRequires:	perl-DBIx-SearchBuilder >= 0.47
BuildRequires:	perl-Exception-Class
BuildRequires:	perl-File-Spec >= 0.8
BuildRequires:	perl-File-Temp
BuildRequires:	perl-FreezeThaw
BuildRequires:	perl-HTML-Mason >= 0.896
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-Locale-Maketext >= 1.06
BuildRequires:	perl-Locale-Maketext-Fuzzy
BuildRequires:	perl-Locale-Maketext-Lexicon
BuildRequires:	perl-Log-Dispatch >= 1.6
BuildRequires:	perl-MIME-tools >= 5.411
BuildRequires:	perl-MLDBM
BuildRequires:	perl-MailTools >= 1.20
BuildRequires:	perl-Params-Validate >= 0.02
BuildRequires:	perl-Storable
BuildRequires:	perl-Term-ReadKey
BuildRequires:	perl-Test-Inline
BuildRequires:	perl-Text-Autoformat
BuildRequires:	perl-Text-Quoted
BuildRequires:	perl-Text-Template
BuildRequires:	perl-Text-Wrapper
BuildRequires:	perl-Tie-IxHash
BuildRequires:	perl-Time-HiRes
BuildRequires:	perl-Time-modules
BuildRequires:	perl-TimeDate
BuildRequires:	perl-WWW-Mechanize
BuildRequires:	perl-base >= 5.8.0
BuildRequires:	perl-libnet
Requires:	perl-Calendar-Simple
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# workarounds for bug in perl.req ("perl()") and ,,famous'' rpm's feature (RT::*)
%define		_noautoreq	'perl().*' 'perl(RT.*)' 'perl(Encode::compat)' 'perl(CGI::Fast)

%define		_sysconfdir	/etc/rt3
%define		_libdir		%{perl_vendorlib}
%define		htmldir		%{_datadir}/rt3/html
%define		masonstatedir	%{_localstatedir}/cache/mason_data
%define		masonsessiondir	%{_localstatedir}/cache/session_data

%description
RT is an enterprise-grade ticketing system which enables a group of
people to intelligently and efficiently manage tasks, issues, and
requests submitted by a community of users.

%description -l pl.UTF-8
RT to profesjonalnej klasy system biletowy pozwalający grupie ludzi
inteligentnie i wydajnie zarządzać zadaniami, problemami i zleceniami
składanymi przez użytkowników.

%package cli
Summary:	Command-line interface to RT
Summary(pl.UTF-8):	Interfejs linii poleceń dla RT
Group:		Applications

%description cli
This package contains /usr/bin/rt, a command-line interface to RT 3.

It allows you to interact with an RT server over HTTP, and offers an
interface to RT's functionality that is better-suited to automation
and integration with other tools.

%description cli -l pl.UTF-8
Ten pakiet zawiera /usr/bin/rt - interfejs linii poleceń do RT 3.

Umożliwia on współdziałanie z serwerem RT po HTTP i oferuje interfejs
do funkcjonalności RT bardziej dopasowany do automatyki i intergracji
z innymi narzędziami.

%prep
%setup -q
%patch0 -p0
%patch1 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
%configure \
	--enable-layout=FHS \
	htmldir=%{htmldir} \
	exp_htmldir=%{htmldir} \
	masonstatedir=%{masonstatedir} \
	masonsessiondir=%{masonstatedir} \
	--with-speedycgi=%{_bindir}/speedycgi \
	--with-my-user-group \
	--with-db-type=mysql

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir} \
	$RPM_BUILD_ROOT%{masonstatedir} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# *.in, tests
find $RPM_BUILD_ROOT -type f -name \*.in -exec rm '{}' \;
rm -r $RPM_BUILD_ROOT%{_libdir}/t

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* UPGRADING Changelog docs
%attr(755,root,root) %dir %{_sysconfdir}
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/mason_handler.*
%attr(755,root,root) %{_bindir}/rt-*
%attr(755,root,root) %{_bindir}/standalone_httpd
%attr(755,root,root) %{_bindir}/webmux.pl
%attr(755,root,root) %{_sbindir}/rt-*
%dir %{_datadir}/rt3
%{_datadir}/rt3/html
%{_libdir}/*
%dir %attr(770,root,http) %{masonstatedir}
%{_examplesdir}/%{name}-%{version}

%files cli
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rt

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
Summary(pl):	Request Tracker - system do �ledzenia zlece�
Name:		rt
Version:	3.2.2
Release:	0.4
License:	GPL v2
Group:		Aplications
Source0:	http://download.bestpractical.com/pub/rt/release/%{name}-%{version}.tar.gz
# Source0-md5:	3c74baff2c43e939d7ec3a367d7181a0
# Source0-size:	1229103
Source1:	%{name}-apache_dir.conf
Source2:	%{name}-apache_vhost.conf
Patch0:		%{name}-layout.patch
URL:		http://www.bestpractical.com/rt/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	perl-Apache-Session >= 1.53
BuildRequires:	perl-CGI >= 2.78
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
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# workarounds for bug in perl.req ("perl()") and ,,famous'' rpm's feature (RT::*)
%define		_noautoreq	'perl().*' 'perl(RT::.*)' 'perl(Encode::compat)'

%define		_sysconfdir	/etc/rt3
%define		_libdir		%{_datadir}/rt3
%define		htmldir		%{_datadir}/rt3/html
%define		masonstatedir	%{_localstatedir}/cache/mason_data
%define		masonsessiondir	%{_localstatedir}/cache/session_data

%description
RT is an enterprise-grade ticketing system which enables a group of
people to intelligently and efficiently manage tasks, issues, and
requests submitted by a community of users.

%description -l pl
RT to profesjonalnej klasy system biletowy pozwalaj�cy grupie ludzi
inteligentnie i wydajnie zarz�dza� zadaniami, problemami i zleceniami
sk�adanymi przez u�ytkownik�w.

%package cli
Summary:	Command-line interface to RT
#Summary(pl):	
Group:		Applications

%description cli
This package contains /usr/bin/rt, a command-line interface to RT 3.

It allows you to interact with an RT server over HTTP, and offers an
interface to RT's functionality that is better-suited to automation and
integration with other tools.

#%description cli -l pl
#TODO

%package test
Summary:	Command-line tool for testing RT's configuration for dependencies
#Summary(pl):	[ Ma kto� pomys� na lepsze Summary?  I grup�...? ]
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description test
rt-test-dependencies is a tool for RT that will tell you if you've got
all the modules RT depends on properly installed.

#%description test -l pl
#TODO

%prep
%setup -q
%patch0 -b .bak -p0

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

# *.in
find $RPM_BUILD_ROOT -type f -name \*.in -exec rm '{}' \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README HOWTO
%attr(755,root,root) %dir %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/mason_handler.*
%attr(755,root,root) %{_bindir}/rt-*
%attr(755,root,root) %{_bindir}/standalone_httpd
%attr(755,root,root) %{_bindir}/webmux.pl
%attr(755,root,root) %{_sbindir}/rt-setup-database
%dir %{_datadir}/rt3
%{_datadir}/rt3/RT*
%{_datadir}/rt3/html
%dir %attr(660,root,http) %{masonstatedir}
%{_examplesdir}/%{name}-%{version}

%files cli
%attr(755,root,root) %{_bindir}/rt

%files test
%attr(755,root,root) %{_sbindir}/rt-test-dependencies
%{_datadir}/rt3/t

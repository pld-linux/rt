# TODO:
# - check file permissions
# - check files in /usr/share/rt/
# - check Requires (meta-packages for configurations with mod_perl/fcgi,
#   apache[12]/standalone server...?)
# - separate standalone server
#
%define	perl_ver				5.8.3
%define	perl_apache_session_ver			1.53
%define	perl_cgi_ver				4.00
%define	perl_class_returnvalue_ver		0.40
%define	perl_css_squish_ver			0.06
%define perl_date_extract_ver                   0.07
%define	perl_dbd_mysql				2.1018
%define	perl_dbi_ver				1.37
%define	perl_dbix_searchbuilder_ver		1.76
%define	perl_devel_stacktrace_ver		1.19
%define	perl_digest_md5_ver			2.27
%define	perl_gd_ver				1.48
%define	perl_html_mason_ver			3:1.43
%define	perl_html_rewriteattributes_ver		0.05
%define	perl_html_scrubber_ver			0.08
%define	perl_http_server_simple_mason_ver	0.09
%define	perl_http_server_simple_ver		0.34
%define	perl_locale_maketext_lexicon_ver	0.32
%define	perl_locale_maketext_ver		1.06
%define	perl_log_dispatch_ver			2.30
%define	perl_mailtools_ver			2.12
%define	perl_mime_tools_ver			5.425
%define	perl_module_versions_report_ver		1.05
%define	perl_cgi_psgi				0.12
%define	perl_plack_ver				1.0002
%define	perl_starlet_ver			0.20
%define	perl_storable_ver			2.08
%define	perl_symbol_global_name_ver		0.05
%define	perl_text_quoted_ver			2.07
%define	perl_text_wikiformat_ver		0.76
%define	perl_tree_simple_ver			1.18
%define	perl_text_template_ver			1.45
%define	perl_xml_rss_ver			1.05
#
%bcond_with	testdeps	# used for checking dependencies
#
Summary:	Request Tracker
Summary(pl.UTF-8):	Request Tracker - system do śledzenia zleceń
Name:		rt
Version:	5.0.4
Release:	1
License:	GPL v2
Group:		Applications
# https://bestpractical.com/download-page
Source0:	http://download.bestpractical.com/pub/rt/release/%{name}-%{version}.tar.gz
# Source0-md5:	c1165d83363dd8c50c4e5aa9e5a84384
Source1:	%{name}-apache_dir.conf
Source2:	%{name}-apache_vhost.conf
Source3:	%{name}-apache.conf
Source4:	%{name}.logrotate
Source5:	lighttpd.conf
Patch0:		%{name}-layout.patch
Patch1:		%{name}-config.patch
Patch2:		rt-timeworked.patch
URL:		http://www.bestpractical.com/rt/
BuildRequires:	autoconf
BuildRequires:	automake
%if %{with testdeps}
BuildRequires:	perl-Alien-Base
BuildRequires:	perl-Apache-Session >= %{perl_apache_session_ver}
BuildRequires:	perl-Business-Hours
BuildRequires:	perl-CGI >= %{perl_cgi_ver}
BuildRequires:	perl-CGI-Emulate-PSGI
BuildRequires:	perl-CGI-PSGI >= %{perl_cgi_psgi}
BuildRequires:	perl-CGI-SpeedyCGI
BuildRequires:	perl-CSS-Minifier
BuildRequires:	perl-CSS-Minifier-XS
BuildRequires:	perl-CSS-Squish >= %{perl_css_squish_ver}
BuildRequires:	perl-Cache-Cache
BuildRequires:	perl-Calendar-Simple
BuildRequires:	perl-Class-ISA
BuildRequires:	perl-Class-ReturnValue >= %{perl_class_returnvalue_ver}
BuildRequires:	perl-Convert-Color
BuildRequires:	perl-Crypt-Eksblowfish
BuildRequires:	perl-Crypt-SSLeay
BuildRequires:	perl-Crypt-X509
BuildRequires:	perl-DBD-mysql >= %{perl_dbd_mysql}
BuildRequires:	perl-DBI >= %{perl_dbi_ver}
BuildRequires:	perl-DBIx-DataSource >= 0.02
BuildRequires:	perl-DBIx-SearchBuilder >= %{perl_dbix_searchbuilder_ver}
BuildRequires:	perl-Data-GUID
BuildRequires:	perl-Data-ICal
BuildRequires:	perl-Date-Extract
BuildRequires:	perl-Date-Manip
BuildRequires:  perl-Data-Page
BuildRequires:	perl-Data-Page-Pageset
BuildRequires:  perl-Date-Extract => %{perl_date_extract_ver}
BuildRequires:	perl-DateTime-Format-Natural
BuildRequires:	perl-Devel-GlobalDestruction
BuildRequires:	perl-Devel-StackTrace >= %{perl_devel_stacktrace_ver}
BuildRequires:	perl-Digest-MD5 >= %{perl_digest_md5_ver}
BuildRequires:	perl-Email-Address
BuildRequires:	perl-Email-Address-List
BuildRequires:	perl-Encode-Detect
BuildRequires:	perl-Encode-HanExtra
BuildRequires:	perl-Exception-Class
BuildRequires:	perl-FCGI
BuildRequires:	perl-FCGI-ProcManager
BuildRequires:	perl-File-ShareDir
BuildRequires:	perl-File-Temp
BuildRequires:	perl-File-Which
BuildRequires:	perl-FreezeThaw
BuildRequires:	perl-GD >= %{perl_gd_ver}
BuildRequires:	perl-GD-Graph
BuildRequires:	perl-GD-TextUtil
BuildRequires:	perl-GnuPG-Interface
BuildRequires:	perl-GraphViz2
BuildRequires:	perl-HTML-FormatExternal
BuildRequires:	perl-HTML-FormatText-WithLinks-AndTables
BuildRequires:	perl-HTML-Gumbo
BuildRequires:	perl-HTML-Mason >= %{perl_html_mason_ver}
BuildRequires:	perl-HTML-Mason-PSGIHandler
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-HTML-Quoted
BuildRequires:	perl-HTML-RewriteAttributes >= %{perl_html_rewriteattributes_ver}
BuildRequires:	perl-HTML-Scrubber >= %{perl_html_scrubber_ver}
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-HTTP-Server-Simple >= %{perl_http_server_simple_ver}
BuildRequires:	perl-HTTP-Server-Simple-Mason >= %{perl_http_server_simple_mason_ver}
BuildRequires:	perl-IPC-Run3
BuildRequires:	perl-JSON
BuildRequires:	perl-JavaScript-Minifier
BuildRequires:	perl-JavaScript-Minifier-XS
BuildRequires:	perl-LWP-Protocol-https
BuildRequires:	perl-Locale-Maketext >= %{perl_locale_maketext_ver}
BuildRequires:	perl-Locale-Maketext-Fuzzy
BuildRequires:	perl-Locale-Maketext-Lexicon >= %{perl_locale_maketext_lexicon_ver}
BuildRequires:	perl-Log-Dispatch >= %{perl_log_dispatch_ver}
BuildRequires:	perl-MIME-Types
BuildRequires:	perl-MIME-tools >= %{perl_mime_tools_ver}
BuildRequires:	perl-MLDBM
BuildRequires:	perl-MailTools >= %{perl_mailtools_ver}
BuildRequires:	perl-Module-Path
BuildRequires:	perl-Module-Versions-Report >= %{perl_module_versions_report_ver}
BuildRequires:	perl-Moose
BuildRequires:	perl-MooseX-NonMoose
BuildRequires:	perl-MooseX-Role-Parameterized
BuildRequires:	perl-Mozilla-CA
BuildRequires:	perl-Net-CIDR
BuildRequires:	perl-Net-IP
BuildRequires:	perl-Net-Server >= 0.34
BuildRequires:	perl-PSGI
BuildRequires:	perl-Parallel-ForkManager
BuildRequires:	perl-Params-Validate >= 0.02
BuildRequires:	perl-Path-Dispatcher
BuildRequires:	perl-PerlIO-eol
BuildRequires:	perl-Plack >= %{perl_plack_ver}
BuildRequires:	perl-Regexp-Common
BuildRequires:	perl-Regexp-Common-net-CIDR
BuildRequires:	perl-Regexp-IPv6
BuildRequires:	perl-Role-Basic
BuildRequires:	perl-Scope-Upper
BuildRequires:	perl-Starlet >= %{perl_starlet_ver}
BuildRequires:	perl-Storable >= %{perl_storable_ver}
BuildRequires:	perl-String-ShellQuote
BuildRequires:	perl-Sub-Identify
BuildRequires:	perl-Symbol-Global-Name >= %{perl_symbol_global_name_ver}
BuildRequires:	perl-Term-ReadKey
BuildRequires:	perl-Test-Inline
BuildRequires:	perl-Text-Autoformat
BuildRequires:	perl-Text-Password-Pronounceable
BuildRequires:	perl-Text-Quoted >= %{perl_text_quoted_ver}
BuildRequires:	perl-Text-Template >= %{perl_text_template_ver}
BuildRequires:	perl-Text-WikiFormat >= %{perl_text_wikiformat_ver}
BuildRequires:	perl-Text-WordDiff
BuildRequires:	perl-Text-Wrapper
BuildRequires:	perl-Tie-IxHash
BuildRequires:	perl-Time-HiRes
BuildRequires:	perl-Time-modules
BuildRequires:	perl-TimeDate
BuildRequires:	perl-Tree-Simple >= %{perl_tree_simple_ver}
BuildRequires:	perl-Type-Tiny
BuildRequires:	perl-UNIVERSAL-require
BuildRequires:	perl-WWW-Mechanize
BuildRequires:	perl-Web-Machine
BuildRequires:	perl-XML-RSS >= %{perl_xml_rss_ver}
BuildRequires:	perl-libnet
%endif
BuildRequires:	perl-base >= %{perl_ver}
BuildRequires:	rpm-perlprov
Requires:	fonts-TTF-Google-Droid
Requires:	perl-Apache-Session >= %{perl_apache_session_ver}
Requires:	perl-Business-Hours
Requires:	perl-CGI >= %{perl_cgi_ver}
Requires:	perl-CGI-Emulate-PSGI
Requires:	perl-CGI-PSGI >= %{perl_cgi_psgi}
Requires:	perl-CSS-Minifier
Requires:	perl-CSS-Minifier-XS
Requires:	perl-CSS-Squish >= %{perl_css_squish_ver}
Requires:	perl-Cache-Cache
Requires:	perl-Calendar-Simple
Requires:	perl-Class-ISA
Requires:	perl-Class-ReturnValue >= %{perl_class_returnvalue_ver}
Requires:	perl-Convert-Color
Requires:	perl-Crypt-Eksblowfish
Requires:	perl-Crypt-SSLeay
Requires:	perl-Crypt-X509
Requires:	perl-DBD-mysql >= %{perl_dbd_mysql}
Requires:	perl-DBI >= %{perl_dbi_ver}
Requires:	perl-DBIx-SearchBuilder >= %{perl_dbix_searchbuilder_ver}
Requires:	perl-Data-GUID
Requires:	perl-Data-ICal
Requires:	perl-Date-Extract >= %{perl_date_extract_ver}
Requires:	perl-Date-Manip
Requires:	perl-Data-Page
Requires:	perl-Data-Page-Pageset
Requires:	perl-DateTime-Format-Natural
Requires:	perl-Devel-GlobalDestruction
Requires:	perl-Devel-StackTrace >= %{perl_devel_stacktrace_ver}
Requires:	perl-Digest-MD5 >= %{perl_digest_md5_ver}
Requires:	perl-Email-Address-List
Requires:	perl-Encode >= 1:2.64
Requires:	perl-Encode-HanExtra
Requires:	perl-FCGI-ProcManager
Requires:	perl-File-Which
Requires:	perl-GD >= %{perl_gd_ver}
Requires:	perl-GD-Graph
Requires:	perl-GnuPG-Interface >= 1.02
Requires:	perl-GraphViz2
Requires:	perl-HTML-FormatExternal
Requires:	perl-HTML-FormatText-WithLinks-AndTables
Requires:	perl-HTML-Gumbo
Requires:	perl-HTML-Mason >= %{perl_html_mason_ver}
Requires:	perl-HTML-Mason-PSGIHandler
Requires:	perl-HTML-Quoted
Requires:	perl-HTML-RewriteAttributes >= %{perl_html_rewriteattributes_ver}
Requires:	perl-HTML-Scrubber >= %{perl_html_scrubber_ver}
Requires:	perl-HTTP-Server-Simple >= %{perl_http_server_simple_ver}
Requires:	perl-HTTP-Server-Simple-Mason >= %{perl_http_server_simple_mason_ver}
Requires:	perl-IPC-Run3
Requires:	perl-JSON
Requires:	perl-JavaScript-Minifier
Requires:	perl-JavaScript-Minifier-XS
Requires:	perl-LWP-Protocol-https
Requires:	perl-Locale-Maketext >= %{perl_locale_maketext_ver}
Requires:	perl-Locale-Maketext-Fuzzy
Requires:	perl-Locale-Maketext-Lexicon >= %{perl_locale_maketext_lexicon_ver}
Requires:	perl-Locale-PO
Requires:	perl-Log-Dispatch >= %{perl_log_dispatch_ver}
Requires:	perl-MIME-tools >= %{perl_mime_tools_ver}
Requires:	perl-MailTools >= %{perl_mailtools_ver}
Requires:	perl-Module-Path
Requires:	perl-Module-Versions-Report >= %{perl_module_versions_report_ver}
Requires:	perl-Moose
Requires:	perl-MooseX-NonMoose
Requires:	perl-MooseX-Role-Parameterized
Requires:	perl-Mozilla-CA
Requires:	perl-Net-CIDR
Requires:	perl-Net-IP
Requires:	perl-PSGI
Requires:	perl-Path-Dispatcher >= 1.07
Requires:	perl-PerlIO-eol
Requires:	perl-Plack >= %{perl_plack_ver}
Requires:	perl-Regexp-Common-net-CIDR
Requires:	perl-Regexp-IPv6
Requires:	perl-Role-Basic
Requires:	perl-Scope-Upper
Requires:	perl-Starlet >= %{perl_starlet_ver}
Requires:	perl-Storable >= %{perl_storable_ver}
Requires:	perl-String-ShellQuote
Requires:	perl-Symbol-Global-Name >= %{perl_symbol_global_name_ver}
Requires:	perl-Text-Password-Pronounceable
Requires:	perl-Text-Quoted >= %{perl_text_quoted_ver}
Requires:	perl-Text-WikiFormat >= %{perl_text_wikiformat_ver}
Requires:	perl-Tree-Simple >= %{perl_tree_simple_ver}
Requires:	perl-Type-Tiny
Requires:	perl-UNIVERSAL-require
Requires:	perl-Web-Machine
Requires:	perl-XML-RSS >= %{perl_xml_rss_ver}
Requires:	perl-base >= %{perl_ver}
Requires:	webapps
Suggests:	perl-FCGI
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# workarounds for bug in perl.req ("perl()") and ,,famous'' rpm's feature (RT::*)
%define		_noautoreq		perl().* perl(RT.*)
%define		_noautoreq_perl		Encode::compat CGI::Fast Exception::Class::Base HTML::Mason::Request::PSGI

%define         _webapps        /etc/webapps
%define         _webapp         %{name}
%define         _webappsdir     %{_webapps}/%{_webapp}
%define		_sysconfdir	/etc/rt
%define		_libdir		%{perl_vendorlib}
%define		htmldir		%{_datadir}/rt/html
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

%package apache
Summary:	Apache support files for RT
Summary(pl.UTF-8):	Pliki wspomagające używanie RT z Apache
Group:		Applications
Requires:	%{name} = %{version}-%{release}
Requires:	apache-base >= 2.2.0
Requires:	apache-mod_authz_host >= 2.2.0
Requires:	apache-mod_perl >= 2.0
Requires:	webapps
Conflicts:	apache-base < 2.4.0-1

%description apache
Apache support files for RT.

%description apache -l pl.UTF-8
Pliki wspomagające używanie RT z Apache.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

mv aclocal.m4 acinclude.m4

sed -i -e 's#libdir:.*#libdir:	%{_libdir}#g' config.layout

# prevent configure from using git
sed -i -e 's#git describe --tags#false#g' configure.ac

%build
%{__aclocal}
%{__autoconf}
USER=$(id -un) \
%configure \
	--enable-layout=PLDFHS \
	htmldir=%{htmldir} \
	exp_htmldir=%{htmldir} \
	masonstatedir=%{masonstatedir} \
	masonsessiondir=%{masonstatedir} \
	--with-my-user-group \
	--with-db-type=mysql \
	--with-web-handler=fastcgi,modperl2

%{?with_testdeps:%{__make} testdeps}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/{logrotate.d,cron.daily},%{_libdir}} \
	$RPM_BUILD_ROOT%{masonstatedir} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version} \
	$RPM_BUILD_ROOT%{_webappsdir} \
	$RPM_BUILD_ROOT%{_datadir}/rt/html/Callbacks

install -d $RPM_BUILD_ROOT%{perl_vendorlib}/RT/Extension

# this is make install minus fixperms
%{__make} config-install dirs files-install instruct \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install %{SOURCE3} $RPM_BUILD_ROOT%{_webappsdir}/httpd.conf
install %{SOURCE5} $RPM_BUILD_ROOT%{_webappsdir}/lighttpd.conf
install %{SOURCE4} $RPM_BUILD_ROOT/etc/logrotate.d/%{name}

ln -s ../../%{_sbindir}/rt-clean-sessions $RPM_BUILD_ROOT/etc/cron.daily/rt-clean-sessions

# unneeded in installed copy
rm $RPM_BUILD_ROOT%{_sbindir}/rt-test-dependencies
rm -r $RPM_BUILD_ROOT%{_datadir}/doc

# we use fonts-TTF-Google-Droid
rm -r $RPM_BUILD_ROOT%{_datadir}/fonts/TTF

# *.in, tests
find $RPM_BUILD_ROOT -type f -name \*.in -exec rm '{}' \;

%triggerin apache -- apache-base
%webapp_register httpd %{_webapp}

%triggerun apache -- apache-base
%webapp_unregister httpd %{_webapp}

%triggerin -- lighttpd
%webapp_register lighttpd %{_webapp}

%triggerun -- lighttpd
%webapp_unregister lighttpd %{_webapp}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* docs

%dir %{_sysconfdir}
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/[a-z]*
# this is local config
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/RT_SiteConfig.pm
# this is generic config that SHOULDN'T BE TOUCHED. Change settings in your local (site) config.
%attr(640,root,http) %config %{_sysconfdir}/RT_Config.pm
%attr(750,root,http) %dir %{_webappsdir}
# web server configs with no separate deps (so no need for subpackage)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_webappsdir}/lighttpd.conf

%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/%{name}
%attr(755,root,root) /etc/cron.daily/rt-clean-sessions
%attr(755,root,root) %{_bindir}/rt-*
%attr(755,root,root) %{_sbindir}/standalone_httpd
%attr(755,root,root) %{_sbindir}/rt-*
%dir %{_datadir}/rt
%{_datadir}/rt/html
%{_datadir}/rt/po
%{_datadir}/rt/static
%{_libdir}/*
%attr(770,root,http) %dir %{masonstatedir}
%{_examplesdir}/%{name}-%{version}

%files cli
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rt

%files apache
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_webappsdir}/httpd.conf

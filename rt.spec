# TODO:
# - check file permissions
# - check files in /usr/share/rt3/
# - check BuildRequires
# - check Requires (meta-packages for configurations with mod_perl/fcgi,
#   apache[12]/standalone server...?)
# - separate standalone server
#
%define	perl_apache_session_ver			1.53
%define	perl_cgi_ver				3.38
%define	perl_class_returnvalue_ver		0.40
%define	perl_css_squish_ver			0.06
%define	perl_dbd_mysql				2.1018
%define	perl_dbi_ver				1.37
%define	perl_dbix_searchbuilder_ver		1.54
%define	perl_devel_stacktrace_ver		1.19
%define	perl_digest_md5_ver			2.27
%define	perl_file_spec_ver			0.8
%define	perl_html_mason_ver			1.36
%define	perl_html_rewriteattributes_ver		0.02
%define	perl_html_scrubber_ver			0.08
%define	perl_http_server_simple_mason_ver	0.09
%define	perl_http_server_simple_ver		0.34
%define	perl_locale_maketext_lexicon_ver	0.32
%define	perl_locale_maketext_ver		1.06
%define	perl_log_dispatch_ver			2.0
%define	perl_mailtools_ver			1.57
%define	perl_mime_tools_ver			5.425
%define	perl_module_versions_report_ver		1.05
%define	perl_storable_ver			2.08
%define	perl_text_quoted_ver			2.02
%define	perl_text_wikiformat_ver		0.76
%define	perl_tree_simple_ver			1.04
%define	perl_text_template_ver			1.45
%define	perl_xml_rss_ver			1.05
#
%include	/usr/lib/rpm/macros.perl
Summary:	Request Tracker
Summary(pl.UTF-8):	Request Tracker - system do śledzenia zleceń
Name:		rt
Version:	3.8.2
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://download.bestpractical.com/pub/rt/release/%{name}-%{version}.tar.gz
# Source0-md5:	100b1fd791e229c4338c0d056c65c12f
Source1:	%{name}-apache_dir.conf
Source2:	%{name}-apache_vhost.conf
Patch0:		%{name}-layout.patch
Patch1:		%{name}-config.patch
URL:		http://www.bestpractical.com/rt/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	perl-Apache-Session >= %{perl_apache_session_ver}
BuildRequires:	perl-CGI >= %{perl_cgi_ver}
BuildRequires:	perl-CGI-SpeedyCGI
BuildRequires:	perl-CSS-Squish >= %{perl_css_squish_ver}
BuildRequires:	perl-Cache-Cache
BuildRequires:	perl-Calendar-Simple
BuildRequires:	perl-Class-ReturnValue >= %{perl_class_returnvalue_ver}
BuildRequires:	perl-DBD-mysql >= %{perl_dbd_mysql}
BuildRequires:	perl-DBI >= %{perl_dbi_ver}
BuildRequires:	perl-DBIx-DataSource >= 0.02
BuildRequires:	perl-DBIx-SearchBuilder >= %{perl_dbix_searchbuilder_ver}
BuildRequires:	perl-Data-ICal
BuildRequires:	perl-Devel-StackTrace >= %{perl_devel_stacktrace_ver}
BuildRequires:	perl-Digest-MD5 >= %{perl_digest_md5_ver}
BuildRequires:	perl-Email-Address
BuildRequires:	perl-Exception-Class
BuildRequires:	perl-FCGI
BuildRequires:	perl-File-ShareDir
BuildRequires:	perl-File-Spec >= %{perl_file_spec_ver}
BuildRequires:	perl-File-Temp
BuildRequires:	perl-FreezeThaw
BuildRequires:	perl-GD
BuildRequires:	perl-GD-Graph
BuildRequires:	perl-GD-TextUtil
BuildRequires:	perl-GnuPG-Interface
BuildRequires:	perl-HTML-Mason >= %{perl_html_mason_ver}
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-HTML-RewriteAttributes >= %{perl_html_rewriteattributes_ver}
BuildRequires:	perl-HTML-Scrubber >= %{perl_html_scrubber_ver}
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-HTTP-Server-Simple >= %{perl_http_server_simple_ver}
BuildRequires:	perl-HTTP-Server-Simple-Mason >= %{perl_http_server_simple_mason_ver}
BuildRequires:	perl-Locale-Maketext >= %{perl_locale_maketext_ver}
BuildRequires:	perl-Locale-Maketext-Fuzzy
BuildRequires:	perl-Locale-Maketext-Lexicon >= %{perl_locale_maketext_lexicon_ver}
BuildRequires:	perl-Log-Dispatch >= %{perl_log_dispatch_ver}
BuildRequires:	perl-MIME-Types
BuildRequires:	perl-MIME-tools >= %{perl_mime_tools_ver}
BuildRequires:	perl-MLDBM
BuildRequires:	perl-MailTools >= %{perl_mailtools_ver}
BuildRequires:	perl-Module-Versions-Report >= %{perl_module_versions_report_ver}
BuildRequires:	perl-Net-Server >= 0.34
BuildRequires:	perl-Params-Validate >= 0.02
BuildRequires:	perl-PerlIO-eol
BuildRequires:	perl-Regexp-Common
BuildRequires:	perl-Storable >= %{perl_storable_ver}
BuildRequires:	perl-Term-ReadKey
BuildRequires:	perl-Test-Inline
BuildRequires:	perl-Text-Autoformat
BuildRequires:	perl-Text-Quoted >= %{perl_text_quoted_ver}
BuildRequires:	perl-Text-Template >= %{perl_text_template_ver}
BuildRequires:	perl-Text-WikiFormat >= %{perl_text_wikiformat_ver}
BuildRequires:	perl-Text-Wrapper
BuildRequires:	perl-Tie-IxHash
BuildRequires:	perl-Time-HiRes
BuildRequires:	perl-Time-modules
BuildRequires:	perl-TimeDate
BuildRequires:	perl-Tree-Simple >= %{perl_tree_simple_ver}
BuildRequires:	perl-UNIVERSAL-require
BuildRequires:	perl-WWW-Mechanize
BuildRequires:	perl-XML-RSS >= %{perl_xml_rss_ver}
BuildRequires:	perl-base >= 5.8.0
BuildRequires:	perl-libnet
Requires:	perl-Apache-Session >= %{perl_apache_session_ver}
Requires:	perl-CGI >= %{perl_cgi_ver}
Requires:	perl-CSS-Squish >= %{perl_css_squish_ver}
Requires:	perl-CSS-Squish >= 0.06
Requires:	perl-Calendar-Simple
Requires:	perl-Class-ReturnValue >= %{perl_class_returnvalue_ver}
Requires:	perl-DBD-mysql >= %{perl_dbd_mysql}
Requires:	perl-DBI >= %{perl_dbi_ver}
Requires:	perl-DBIx-SearchBuilder >= %{perl_dbix_searchbuilder_ver}
Requires:	perl-Data-ICal
Requires:	perl-Devel-StackTrace >= %{perl_devel_stacktrace_ver}
Requires:	perl-Digest-MD5 >= %{perl_digest_md5_ver}
Requires:	perl-File-Spec >= %{perl_file_spec_ver}
Requires:	perl-GD-Graph
Requires:	perl-HTML-Mason >= %{perl_html_mason_ver}
Requires:	perl-HTML-RewriteAttributes >= %{perl_html_rewriteattributes_ver}
Requires:	perl-HTML-Scrubber >= %{perl_html_scrubber_ver}
Requires:	perl-HTTP-Server-Simple >= %{perl_http_server_simple_ver}
Requires:	perl-HTTP-Server-Simple-Mason >= %{perl_http_server_simple_mason_ver}
Requires:	perl-Locale-Maketext >= %{perl_locale_maketext_ver}
Requires:	perl-Locale-Maketext-Fuzzy
Requires:	perl-Locale-Maketext-Lexicon >= %{perl_locale_maketext_lexicon_ver}
Requires:	perl-Log-Dispatch >= %{perl_log_dispatch_ver}
Requires:	perl-MIME-tools >= %{perl_mime_tools_ver}
Requires:	perl-MailTools >= %{perl_mailtools_ver}
Requires:	perl-Module-Versions-Report >= %{perl_module_versions_report_ver}
Requires:	perl-PerlIO-eol
Requires:	perl-Storable >= %{perl_storable_ver}
Requires:	perl-Text-Quoted >= %{perl_text_quoted_ver}
Requires:	perl-Text-WikiFormat >= %{perl_text_wikiformat_ver}
Requires:	perl-Tree-Simple >= %{perl_tree_simple_ver}
Requires:	perl-XML-RSS >= %{perl_xml_rss_ver}
Suggests:	perl-FCGI
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl().*' 'perl(RT.*)' 'perl(Encode::compat)' 'perl(CGI::Fast)' 'perl(Exception::Class::Base)'
# workarounds for bug in perl.req ("perl()") and ,,famous'' rpm's feature (RT::*)

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

mv aclocal.m4 acinclude.m4

sed -i -e 's#libdir:.*#libdir:	%{_libdir}#g' config.layout

%build
%{__aclocal} -I m4
%{__autoconf}
%configure \
	--enable-layout=PLDFHS \
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

# unneeded in installed copy
rm -f $RPM_BUILD_ROOT%{_sbindir}/rt-test-dependencies

# *.in, tests
find $RPM_BUILD_ROOT -type f -name \*.in -exec rm '{}' \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* UPGRADING docs
%dir %{_sysconfdir}
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

# TODO:
# - check file permissions
# - add apache alias for /rt /usr/share/rt/
# - check files in /usr/share/rt/
# - check BuildRequires

%include	/usr/lib/rpm/macros.perl
%define	ver	3.2.1
%define	orgver	%(echo %{ver} | tr . -)
Summary:	Request Tracker
Summary(pl):	Request Tracker - system do ¶ledzenia zleceñ
Name:		rt
Version:	%{ver}
Release:	0.2
License:	GPL
Group:		Aplications
Source0:	http://download.bestpractical.com/pub/rt/release/%{name}-%{ver}.tar.gz
# Source0-md5:	adf0c77827c8f84829bb44e28752a1d8
URL:		http://www.bestpractical.com/rt/
BuildRequires:	perl-base >= 5.8.0
BuildRequires:	perl-Cache-Cache
BuildRequires:	perl-Exception-Class
BuildRequires:	perl-HTML-Mason >= 0.896
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-Test-Inline
BuildRequires:	perl-Class-ReturnValue
BuildRequires:	perl-DBI >= 1.18
BuildRequires:	perl-DBIx-DataSource >= 0.02
BuildRequires:	perl-DBIx-SearchBuilder >= 0.47
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-Locale-Maketext >= 1.06
BuildRequires:	perl-Locale-Maketext-Lexicon
BuildRequires:	perl-Locale-Maketext-Fuzzy
BuildRequires:	perl-MLDBM
BuildRequires:	perl-libnet
BuildRequires:	perl-CGI >= 2.78
BuildRequires:	perl-Params-Validate >= 0.02
BuildRequires:	perl-Apache-Session >= 1.53
BuildRequires:	perl-MIME-tools >= 5.411
BuildRequires:	perl-MailTools >= 1.20
BuildRequires:	perl-Tie-IxHash
BuildRequires:	perl-TimeDate
BuildRequires:	perl-Time-HiRes
BuildRequires:	perl-Time-modules
BuildRequires:	perl-Text-Wrapper
BuildRequires:	perl-Text-Quoted
BuildRequires:	perl-Text-Template
BuildRequires:	perl-Text-Autoformat
BuildRequires:	perl-Term-ReadKey
BuildRequires:	perl-File-Spec >= 0.8
BuildRequires:	perl-FreezeThaw
BuildRequires:	perl-Storable
BuildRequires:	perl-File-Temp
BuildRequires:	perl-Log-Dispatch >= 1.6
BuildRequires:	perl-WWW-Mechanize
BuildRequires:	perl-DBD-mysql
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# workarounds for bug in perl.req ("perl()") and ,,famous'' rpm's feature (RT::*)
%define		_noautoreq	'perl().*' 'perl(RT::.*)' 'perl(Encode::compat)'

%define		varpath		%{_sharedstatedir}/rt
%define		_sysconfdir	/etc/%{name}
%define		_libdir		%{_prefix}/lib/%{name}

%description
RT is an enterprise-grade ticketing system which enables a group of
people to intelligently and efficiently manage tasks, issues, and
requests submitted by a community of users.

%description -l pl
RT to profesjonalnej klasy system biletowy pozwalaj±cy grupie ludzi
inteligentnie i wydajnie zarz±dzaæ zadaniami, problemami i zleceniami
sk³adanymi przez u¿ytkowników.

%prep
%setup -q -n %{name}-%{ver}

%build
%configure \
	--with-speedycgi=%{_bindir}/speedycgi \
	--with-my-user-group \
	--with-db-type=mysql

%{__make} \
	RT_VAR_PATH=%{varpath} \
	RT_ETC_PATH=%{_sysconfdir} \
	CONFIG_FILE_PATH=%{_sysconfdir}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	CONFIG_FILE_PATH=%{_sysconfdir} \
	RT_LIB_PATH=%{_libdir} \
	MASON_HTML_PATH=%{_datadir}/rt
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc etc/{a*,i*,s*}

%attr(755,root,root) %dir %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_libdir}
%{_datadir}

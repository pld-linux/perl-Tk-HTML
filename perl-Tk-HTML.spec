#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Tk
%define	pnam	HTML
Summary:	Tk::HTML Perl module
Summary(pl):	Modu³ Perla Tk::HTML
Name:		perl-Tk-HTML
Version:	3.003
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8ef339ccb5fba4f5aef61e59e3e81b19
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-Tk
BuildRequires:	perl-URI
BuildRequires:	perl-libwww
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tk::HTML Perl module.

%description -l pl
Modu³ Perla Tk::HTML.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/tkweb
%{perl_vendorlib}/Tk/*.pm
%{perl_vendorlib}/Tk/HTML
%dir %{perl_vendorlib}/auto/Tk
%{perl_vendorlib}/auto/Tk/HTML
%{perl_vendorlib}/auto/Tk/Web
%{_mandir}/man[13]/*

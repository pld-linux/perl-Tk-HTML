%include	/usr/lib/rpm/macros.perl
%define		pdir	Tk
%define		pnam	HTML
Summary:	Tk::HTML Perl module
Summary(pl):	Modu³ Perla Tk::HTML
Name:		perl-Tk-HTML
Version:	3.002
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-Tk
BuildRequires:	perl-URI
BuildRequires:	perl-libwww
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tk::HTML Perl module.

%description -l pl
Modu³ Perla Tk::HTML.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

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
%{perl_sitelib}/Tk/*.pm
%{perl_sitelib}/Tk/HTML
%dir %{perl_sitelib}/auto/Tk
%{perl_sitelib}/auto/Tk/HTML
%{perl_sitelib}/auto/Tk/Web
%{_mandir}/man[13]/*

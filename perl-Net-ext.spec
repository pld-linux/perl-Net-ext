%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	ext
Summary:	Net::ext perl module
Summary(pl):	Modu³ perla Net::ext
Name:		perl-Net-ext
Version:	1.011
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::ext contains modules: Net::Gen, Net::Inet, Net::TCP, Net::UDP,
Net::UNIX, Net::TCP::Server, and Net::UNIX::Server.

%description -l pl
Net::ext zawiera modu³y: Net::Gen, Net::Inet, Net::TCP, Net::UDP,
Net::UNIX, Net::TCP::Server, and Net::UNIX::Server.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_sitearch}/Net/*.pm
%{perl_sitearch}/Net/TCP
%{perl_sitearch}/Net/UNIX
%{perl_sitearch}/auto/Net/UNIX
%{perl_sitearch}/auto/Net/Inet
%{perl_sitearch}/auto/Net/UDP
%dir %{perl_sitearch}/auto/Net/Gen
%{perl_sitearch}/auto/Net/Gen/*.al
%{perl_sitearch}/auto/Net/Gen/autosplit.ix
%{perl_sitearch}/auto/Net/Gen/Gen.bs
%attr(755,root,root) %{perl_sitearch}/auto/Net/Gen/Gen.so
%{_mandir}/man3/*

%include	/usr/lib/rpm/macros.perl
Summary:	Net-ext perl module
Summary(pl):	Modu³ perla Net-ext
Name:		perl-Net-ext
Version:	0.91
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/Net-ext-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net-ext contains modules: Net::Gen, Net::Inet, Net::TCP, Net::UDP,
Net::UNIX, Net::TCP::Server, and Net::UNIX::Server.

%description -l pl
Net-ext zawiera modu³y: Net::Gen, Net::Inet, Net::TCP, Net::UDP,
Net::UNIX, Net::TCP::Server, and Net::UNIX::Server.

%prep
%setup -q -n Net-ext-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{?debug:-O -g}%{!?debug:$RPM_OPT_FLAGS}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
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

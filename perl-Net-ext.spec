#
# Conditional build:
%bcond_with	tests	# perform "make test" (uses network!)
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	ext
Summary:	Net::ext perl module
Summary(pl):	Modu³ perla Net::ext
Name:		perl-Net-ext
Version:	1.011
Release:	2
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8be68650bef6769212127d2118b44736
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorarch}/Net/*.pm
%{perl_vendorarch}/Net/TCP
%{perl_vendorarch}/Net/UNIX
%{perl_vendorarch}/auto/Net/UNIX
%{perl_vendorarch}/auto/Net/Inet
%{perl_vendorarch}/auto/Net/UDP
%dir %{perl_vendorarch}/auto/Net/Gen
%{perl_vendorarch}/auto/Net/Gen/*.al
%{perl_vendorarch}/auto/Net/Gen/autosplit.ix
%{perl_vendorarch}/auto/Net/Gen/Gen.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Net/Gen/Gen.so
%{_mandir}/man3/*

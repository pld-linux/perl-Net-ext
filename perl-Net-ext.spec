#
# Conditional build:
%bcond_with	tests	# perform "make test" (uses network!)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	ext
Summary:	Net::ext Perl modules - socket interfaces
Summary(pl.UTF-8):	Moduły perla Net::ext - interfejsy do gniazd
Name:		perl-Net-ext
Version:	1.011
Release:	23
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8be68650bef6769212127d2118b44736
URL:		http://search.cpan.org/dist/Net-ext/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::ext contains the following modules:
- Net::Gen - generic socket interface handling,
- Net::Inet - Internet socket interface module,
- Net::TCP - TCP sockets interface module,
- Net::TCP::Server - TCP sockets interface module for listeners and
  servers,
- Net::UDP - UDP sockets interface module,
- Net::UNIX - UNIX-domain sockets interface module,
- Net::UNIX::Server - UNIX-domain sockets interface module for
  listeners.

%description -l pl.UTF-8
Net::ext zawiera następujące moduły:
- Net::Gen - obsługa ogólnego interfejsu gniazd,
- Net::Inet - moduł interfejsu do gniazd internetowych,
- Net::TCP - moduł interfejsu do gniazd TCP,
- Net::TCP::Server - moduł interfejsu do gniazd TCP dla nasłuchujących
  i serwerów,
- Net::UDP - moduł interfejsu do gniazd UDP,
- Net::UNIX - moduł interfejsu do gniazd uniksowych,
- Net::UNIX::Server - moduł interfejsu do gniazd uniksowych dla
  nasłuchujących.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
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
%{perl_vendorarch}/attrs.pm
%{perl_vendorarch}/Net/*.pm
%{perl_vendorarch}/Net/TCP
%{perl_vendorarch}/Net/UNIX
%{perl_vendorarch}/auto/Net/UNIX
%{perl_vendorarch}/auto/Net/Inet
%{perl_vendorarch}/auto/Net/UDP
%dir %{perl_vendorarch}/auto/Net/Gen
%{perl_vendorarch}/auto/Net/Gen/*.al
%{perl_vendorarch}/auto/Net/Gen/autosplit.ix
%attr(755,root,root) %{perl_vendorarch}/auto/Net/Gen/Gen.so
%{_mandir}/man3/*

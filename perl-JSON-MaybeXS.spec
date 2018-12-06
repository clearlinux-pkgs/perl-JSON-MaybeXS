#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-JSON-MaybeXS
Version  : 1.004000
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/H/HA/HAARG/JSON-MaybeXS-1.004000.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/H/HA/HAARG/JSON-MaybeXS-1.004000.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libj/libjson-maybexs-perl/libjson-maybexs-perl_1.004000-1.debian.tar.xz
Summary  : 'Use L<Cpanel::JSON::XS> with a fallback to L<JSON::XS> and L<JSON::PP>'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-JSON-MaybeXS-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Cpanel::JSON::XS)

%description
NAME
JSON::MaybeXS - Use Cpanel::JSON::XS with a fallback to JSON::XS and
JSON::PP

%package dev
Summary: dev components for the perl-JSON-MaybeXS package.
Group: Development
Provides: perl-JSON-MaybeXS-devel = %{version}-%{release}

%description dev
dev components for the perl-JSON-MaybeXS package.


%package license
Summary: license components for the perl-JSON-MaybeXS package.
Group: Default

%description license
license components for the perl-JSON-MaybeXS package.


%prep
%setup -q -n JSON-MaybeXS-1.004000
cd ..
%setup -q -T -D -n JSON-MaybeXS-1.004000 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/JSON-MaybeXS-1.004000/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-JSON-MaybeXS
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-JSON-MaybeXS/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/JSON/MaybeXS.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/JSON::MaybeXS.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-JSON-MaybeXS/deblicense_copyright

Name:           perl-Unicode-Collate
Version:        1.29
Release:        1%{?dist}
Summary:        Unicode Collation Algorithm
# Collate/allkeys.txt:  Unicode (the file contains a link to
#                       <http://www.unicode.org/terms_of_use.html>)
# other files:          GPL+ or Artistic
License:        (GPL+ or Artistic) and Unicode
URL:            https://metacpan.org/release/Unicode-Collate
Source0:        https://cpan.metacpan.org/authors/id/S/SA/SADAHIRO/Unicode-Collate-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Unicode::Normalize)
BuildRequires:  perl(XSLoader)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Unicode::Normalize)
Conflicts:      perl < 4:5.22.0-347

%description
This package is Perl implementation of Unicode Technical Standard #10 (Unicode
Collation Algorithm).

%prep
%setup -q -n Unicode-Collate-%{version}

# Remove pregenerated files
rm Collate/Locale/*
# Collate/CJK/Korean.pm is an input for the mklocale script, do not remove it

%build
# Regenerate code from Collate/allkeys.txt whose authority is
# <http://www.unicode.org/Public/UCA/latest/allkeys.txt>
perl mklocale
mv Locale/*.pl Collate/Locale
mv Korean.pm Collate/CJK

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Unicode*
%{_mandir}/man3/*

%changelog
* Tue Sep 29 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.29-1
- 1.29 bump

* Wed Sep 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.28-1
- 1.28 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-457
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.27-456
- Increase release to favour standalone package

* Thu Feb 06 2020 Tom Stellard <tstellar@redhat.com> - 1.27-441
- Spec file cleanups: Use make_build and make_install macros
- https://docs.fedoraproject.org/en-US/packaging-guidelines/#_parallel_make
- https://fedoraproject.org/wiki/Perl/Tips#ExtUtils::MakeMake

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-440
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-439
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.27-438
- Increase release to favour standalone package

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 03 2019 Petr Pisar <ppisar@redhat.com> - 1.27-1
- 1.27 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-417
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.25-416
- Increase release to favour standalone package

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 23 2017 Petr Pisar <ppisar@redhat.com> - 1.25-1
- 1.25 bump

* Tue Nov 21 2017 Petr Pisar <ppisar@redhat.com> - 1.24-1
- 1.24 bump

* Mon Nov 13 2017 Petr Pisar <ppisar@redhat.com> - 1.23-1
- 1.23 bump

* Mon Nov 06 2017 Petr Pisar <ppisar@redhat.com> - 1.21-1
- 1.21 bump

* Fri Nov 03 2017 Petr Pisar <ppisar@redhat.com> - 1.20-1
- 1.20 bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-394
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.19-393
- Perl 5.26 rebuild

* Mon May 15 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.19-3
- Fixes for removal '.' from @INC in Perl 5.26

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 05 2016 Petr Pisar <ppisar@redhat.com> - 1.19-1
- 1.19 bump

* Tue Nov 08 2016 Petr Pisar <ppisar@redhat.com> - 1.18-1
- 1.18 bump

* Mon Oct 31 2016 Petr Pisar <ppisar@redhat.com> - 1.17-1
- 1.17 bump

* Wed Oct 26 2016 Petr Pisar <ppisar@redhat.com> - 1.16-1
- 1.16 bump

* Mon Oct 24 2016 Petr Pisar <ppisar@redhat.com> - 1.15-1
- 1.15 bump

* Mon Sep 19 2016 Petr Pisar <ppisar@redhat.com> - 1.14-366
- License corrected to ((GPL+ or Artistic) and Unicode)

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.14-365
- Increase release to favour standalone package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 13 2015 Petr Pisar <ppisar@redhat.com> - 1.14-1
- 1.14 bump

* Thu Jul 02 2015 Petr Pisar <ppisar@redhat.com> 1.12-348
- Specfile autogenerated by cpanspec 1.78.
- Run mklocale only if not bootstrapping

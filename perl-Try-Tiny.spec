%define upstream_name    Try-Tiny
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Minimal try/catch with proper localization of $@
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Try/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module provides bare bones 'try'/'catch' statements that are designed
to minimize common mistakes with eval blocks, and NOTHING else.

This is unlike the TryCatch manpage which provides a nice syntax and avoids
adding another call stack layer, and supports calling 'return' from the try
block to return from the parent subroutine. These extra features come at a
cost of a few dependencies, namely the Devel::Declare manpage and the
Scope::Upper manpage which are occasionally problematic, and the additional
catch filtering uses the Moose manpage type constraints which may not be
desirable either.

The main focus of this module is to provide simple and reliable error
handling for those having a hard time installing the TryCatch manpage, but
who still want to write correct 'eval' blocks without 5 lines of
boilerplate each time.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.70.0-3mdv2012.0
+ Revision: 764300
- rebuilt for perl-5.14.x

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.70.0-2
+ Revision: 657857
- rebuild for updated spec-helper

* Sat Nov 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.70.0-1mdv2011.0
+ Revision: 594261
- update to new version 0.07

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2011.0
+ Revision: 552691
- update to 0.06

* Sun Jan 24 2010 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.1
+ Revision: 495434
- update to 0.04

* Wed Sep 16 2009 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.0
+ Revision: 443488
- import perl-Try-Tiny


* Wed Sep 16 2009 cpan2dist 0.02-1mdv
- initial mdv release, generated with cpan2dist

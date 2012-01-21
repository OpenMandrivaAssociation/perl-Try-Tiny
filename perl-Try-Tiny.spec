%define upstream_name    Try-Tiny
%define upstream_version 0.07

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:    Minimal try/catch with proper localization of $@
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Try/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/*



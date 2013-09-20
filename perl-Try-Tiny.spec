%define modname	Try-Tiny
%define modver	0.11

Summary:	Minimal try/catch with proper localization of $@
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	4
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Try/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

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
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*


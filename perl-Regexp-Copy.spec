%define real_name Regexp-Copy

Summary:	Regexp::Copy - copy Regexp objects
Name:		perl-%{real_name}
Version:	0.06
Release: %mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Regexp/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Regexp::Copy allows you to copy the contents of one Regexp object
to another.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES
%dir %{perl_vendorlib}/*/auto/Regexp/Copy
%{perl_vendorlib}/*/Regexp/*
%{perl_vendorlib}/*/auto/Regexp/Copy/*
%{_mandir}/*/*


%define upstream_name    Regexp-Copy
%define upstream_version 0.06

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:	4

Summary:	Regexp::Copy - copy Regexp objects
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Regexp-Copy
Source0:	https://cpan.metacpan.org/authors/id/J/JD/JDUNCAN/Regexp-Copy-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Regexp::Copy allows you to copy the contents of one Regexp object
to another.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
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

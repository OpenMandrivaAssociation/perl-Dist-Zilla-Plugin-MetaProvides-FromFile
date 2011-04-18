%define upstream_name    Dist-Zilla-Plugin-MetaProvides-FromFile
%define upstream_version 1.11034201

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    In the event nothing else works, pull in hand-crafted metadata from a specified file
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Config::INI::Reader)
BuildRequires: perl(Dist::Zilla::App::Tester)
BuildRequires: perl(Dist::Zilla::MetaProvides::ProvideRecord)
BuildRequires: perl(Dist::Zilla::Plugin::MetaProvides)
BuildRequires: perl(Dist::Zilla::Role::MetaProvider::Provider)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Moose)
BuildRequires: perl(Moose::Autobox)
BuildRequires: perl(Test::More)
BuildRequires: perl(namespace::autoclean)
BuildRequires: perl(Module::Build)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
no description found

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor

./Build

%check
./Build test

%install
rm -rf %buildroot
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE META.json META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*



%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%define p4_ver      r12.2 
%define p4_build    2012.2.525804

Name:       p4ruby
Version:    %{p4_ver}
Release:    1%{?dist}
License:    Propiatory
URL:        http://www.perforce.com
Summary:    Perforce-Ruby API
Group:      Development/Languages
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:   ruby(abi) = 1.9.1

BuildRequires:  ruby19-devel

Source0: ftp://ftp.perforce.com/perforce/%{p4_ver}/bin.linux26x86_64/p4api.tgz
Source1: ftp://ftp.perforce.com/perforce/%{p4_ver}/bin.tools/p4ruby.tgz

%description
p4ruby is the perforce-ruby api.

%prep
%setup -q -b 1 -n p4ruby-%{p4_build}

%build
export CFLAGS="$RPM_OPT_FLAGS -Wall -fno-strict-aliasing"

ruby1.9 p4conf.rb --apidir %{_builddir}/p4api-%{p4_build}
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%attr(644, root, root) %{ruby_sitelib}/P4.rb
%attr(755, root, root) %{ruby_sitearch}/P4.so

%changelog
* Mon Nov 26 2012 Björn Henkel <bjoern.henkel@google.com> - r12.2-1
- Initial package

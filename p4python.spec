%if 0%{?rhel} && 0%{?rhel} <= 5
%{!?python_sitelib: %global python_sitelib %(%{python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%define python python26
%else
%define python python
%endif

%define p4_ver         r12.2 
%define p4_api_build   2012.2.525804
%define p4_py_build    2012.2.549493

Name:       p4python
Version:    %{p4_ver}
Release:    1%{?dist}
License:    Proprietary
URL:        http://www.perforce.com
Summary:    Perforce-Ruby API
Group:      Development/Languages
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:   %{python}

BuildRequires:  %{python}-devel

Source0: ftp://ftp.perforce.com/perforce/%{p4_ver}/bin.linux26x86_64/p4api.tgz
Source1: ftp://ftp.perforce.com/perforce/%{p4_ver}/bin.tools/%{name}.tgz

%description
p4python is the perforce-python api.

%prep
%setup -q -b 1 -n %{name}-%{p4_py_build}

%build
%{python} setup.py build --apidir %{_builddir}/p4api-%{p4_api_build}

%install
%{python} setup.py install --apidir %{_builddir}/p4api-%{p4_api_build} --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{python_sitearch}

%changelog
* Mon Dec 26 2012 Björn Henkel <bjoern.henkel@google.com> - r12.2-1
- Initial package

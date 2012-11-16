%define rubyxver    1.9
%define rubyyver    .3
%define rubyzver    p327
%define dist        bbh

Name:       ruby19
Version:    %{rubyxver}%{rubyyver}
Release:    %{rubyzver}%{?dist}
License:    Ruby License/GPL - see COPYING
URL:        http://www.ruby-lang.org/
Summary:    An interpreter of object-oriented scripting language
Group:      Development/Languages
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	readline readline-devel ncurses ncurses-devel glibc-devel tcl-devel autoconf gcc unzip openssl-devel db4-devel byacc libyaml-devel
Source0: ftp://ftp.ruby-lang.org/pub/ruby/%{rubyxver}/ruby-%{rubyxver}%{rubyyver}-%{rubyzver}.tar.gz

%description
Ruby is the interpreted scripting language for quick and easy
object-oriented programming. It has many features to process text
files and to do system management tasks (as in Perl). It is simple,
straight-forward, and extensible.

This package can be installed in parallel to an existing system ruby
package.

%package docs
Summary:	Manuals and FAQs for scripting language Ruby.
Group:		Documentation

%description docs
Manuals and FAQs for the object-oriented scripting language Ruby.

%package ri
Summary:	Ruby interactive reference
Group:		Documentation
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-rdoc = %{version}-%{release}

%description ri
ri is a command line tool that displays descriptions of built-in
Ruby methods, classes and modules. For methods, it shows you the calling
sequence and a description. For classes and modules, it shows a synopsis
along with a list of the methods the class or module implements.
%prep
%setup -n ruby-%{rubyxver}%{rubyyver}-%{rubyzver}

%build
export CFLAGS="$RPM_OPT_FLAGS -Wall -fno-strict-aliasing"

%configure \
  --enable-shared \
  --without-tk \
  --program-suffix=%{rubyxver}

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

# Don't need this
rm -rf $RPM_BUILD_ROOT/usr/src

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_bindir}
%{_includedir}
%{_mandir}
%{_libdir}

%files ri 
%defattr(-, root, root)
%doc %{_datadir}/ri

%files docs
%defattr(-, root, root)
%doc %{_defaultdocdir}

%changelog
* Fri Nov 16 2012 Björn Henkel <bjoern.henkel@gmail.com> - 1.9.3-p324
- Initial package

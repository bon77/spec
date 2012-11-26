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

%package devel
Summary:	A Ruby development environment.
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
conflicts: ruby-devel

%description devel
Header files and libraries for building a extension library for the
Ruby or an application embedded Ruby.

%prep
%setup -q -n ruby-%{rubyxver}%{rubyyver}-%{rubyzver}

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
rm -rf $RPM_BUILD_ROOT/usr/lib/ruby-1.9.3-p327/ext/ripper/defs/keywords
rm -rf $RPM_BUILD_ROOT/usr/lib/ruby-1.9.3-p327/ext/ripper/parse.c
rm -rf $RPM_BUILD_ROOT/usr/lib/ruby-1.9.3-p327/ext/syck/\<stdout\>
rm -rf $RPM_BUILD_ROOT/usr/lib/ruby-1.9.3-p327/ext/syck/bytecode.re
rm -rf $RPM_BUILD_ROOT/usr/lib/ruby-1.9.3-p327/ext/syck/gram.y
rm -rf $RPM_BUILD_ROOT/usr/lib/ruby-1.9.3-p327/ext/syck/implicit.re
rm -rf $RPM_BUILD_ROOT/usr/lib/ruby-1.9.3-p327/ext/syck/token.re

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_bindir}
%{_mandir}
%{_libdir}
%exclude %{_libdir}/libruby-static.a
%exclude %{_libdir}/libruby.so

%files ri
%defattr(-, root, root)
%doc %{_datadir}/ri

%files docs
%defattr(-, root, root)
%doc %{_defaultdocdir}

%files devel
%defattr(-, root, root)
%{_includedir}
%{_libdir}/libruby-static.a
%{_libdir}/libruby.so

%changelog
* Mon Nov 26 2012 Björn Henkel <bjoern.henkel@gmail.com> - 1.9.3-p324
- split off devel package, because it conflicts with system ruby-devel libs

* Fri Nov 16 2012 Björn Henkel <bjoern.henkel@gmail.com> - 1.9.3-p324
- Initial package

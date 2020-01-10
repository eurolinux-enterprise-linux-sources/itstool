Name:           itstool
Version:        1.2.0
Release:        4%{?dist}
Summary:        ITS-based XML translation tool

Group:          Development/Tools
License:        GPLv3+
URL:            http://itstool.org/
Source0:        http://files.itstool.org/itstool/%{name}-%{version}.tar.bz2

BuildArch:      noarch
Requires:       libxml2-python

%description
ITS Tool allows you to translate XML documents with PO files, using rules from
the W3C Internationalization Tag Set (ITS) to determine what to translate and
how to separate it into PO file messages.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc COPYING COPYING.GPL3 NEWS
%{_bindir}/itstool
%{_datadir}/itstool
%doc %{_mandir}/man1/itstool.1.gz

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.2.0-4
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 02 2012 Kalev Lember <kalevlember@gmail.com> 1.2.0-1
- Update to 1.2.0

* Wed Mar 21 2012 Kalev Lember <kalevlember@gmail.com> 1.1.2-1
- Update to itstool 1.1.2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 19 2011 Shaun McCance <shaunm@gnome.org> 1.1.1-1
- Update to itstool 1.1.1

* Sun Aug 07 2011 Rahul Sundaram <sundaram@fedoraproject.org> 1.1.0-2
- Add requires on libxml2-python since itstool uses it
- Drop redundant defattr
- Add NEWS to doc

* Mon Jun 27 2011 Shaun McCance <shaunm@gnome.org> 1.1.0-1
- Update to itstool 1.1.0

* Sun May 8 2011 Shaun McCance <shaunm@gnome.org> 1.0.1-1
- Initial packaging

%{?scl:%scl_package nodejs-chownr}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

Name:       %{?scl_prefix}nodejs-chownr
Version:    0.0.1
Release:    9%{?dist}
Summary:    Changes file permissions recursively
License:    BSD
Group:      System Environment/Libraries
URL:        https://github.com/isaacs/chownr
Source0:    http://registry.npmjs.org/chownr/-/chownr-%{version}.tgz
BuildRoot:  %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
Changes file permissions recursively, like `chown -R`.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{nodejs_sitelib}/chownr
cp -p chownr.js package.json %{buildroot}%{nodejs_sitelib}/chownr

%nodejs_symlink_deps

#%%check
#%%tap test/*.js

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/chownr
%doc README.md LICENCE

%changelog
* Thu Oct 17 2013 Tomas Hrcka <thrcka@redhat.com> - 0.0.1-9
- replace provides and requires with macro

* Thu Apr 11 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.0.1-8
- Add support for software collections

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.1-6
- rebuild with fresh tarball from upstream
- ship newly included LICENCE file

* Mon Jan 14 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.1-5
- correct license information

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.1-4
- add missing build section
- fix summary and description

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.1-3
- clean up for submission

* Fri Apr 27 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.1-2
- fix BuildRequires not present on <F17

* Thu Mar 29 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.1-1
- initial package


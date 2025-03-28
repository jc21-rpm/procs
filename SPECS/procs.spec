%global debug_package %{nil}

Name:           procs
Version:        0.14.10
Release:        1%{?dist}
Summary:        A modern replacement for ps written in Rust
Group:          Applications/System
License:        GPLv2
URL:            https://github.com/dalance/%{name}
Source:         https://github.com/dalance/%{name}/archive/v%{version}.tar.gz
BuildRequires:  cmake
%{?el7:BuildRequires: cargo, rust}

%description
Features
- Output by the colored and human-readable format
  - Automatic theme detection based on terminal background
- Keyword search over multi-column
- Some additional information which are not supported by ps
  - TCP/UDP port
  - Read/Write throughput
  - Docker container name
  - More memory information
- Pager support
- Watch mode like top
- Tree view

%prep
%setup -q -n %{name}-%{version}

%build
cargo build --release

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
install -D -m 755 target/release/procs %{buildroot}/usr/bin/procs

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE *.md
/usr/bin/procs

%changelog
* Fri Mar 28 2025 Jamie Curnow <jc@jc21.com> - 0.14.10-1
- https://github.com/dalance/procs/releases/tag/v0.14.10

* Thu Oct 24 2024 Jamie Curnow <jc@jc21.com> - 0.14.8-1
- https://github.com/dalance/procs/releases/tag/v0.14.8

* Tue Oct 22 2024 Jamie Curnow <jc@jc21.com> - 0.14.7-1
- https://github.com/dalance/procs/releases/tag/v0.14.7

* Tue Jun 25 2024 Jamie Curnow <jc@jc21.com> - 0.14.5-1
- https://github.com/dalance/procs/releases/tag/v0.14.5

* Fri Oct 20 2023 Jamie Curnow <jc@jc21.com> - 0.14.3-1
- https://github.com/dalance/procs/releases/tag/v0.14.3

* Thu Oct 19 2023 Jamie Curnow <jc@jc21.com> - 0.14.2-1
- https://github.com/dalance/procs/releases/tag/v0.14.2

* Mon Oct 9 2023 Jamie Curnow <jc@jc21.com> - 0.14.1-1
- https://github.com/dalance/procs/releases/tag/v0.14.1

* Thu Mar 9 2023 Jamie Curnow <jc@jc21.com> - 0.14.0-1
- https://github.com/dalance/procs/releases/tag/v0.14.0

* Fri Feb 3 2023 Jamie Curnow <jc@jc21.com> - 0.13.4-1
- https://github.com/dalance/procs/releases/tag/v0.13.4

* Tue Oct 18 2022 Jamie Curnow <jc@jc21.com> - 0.13.3-1
- https://github.com/dalance/procs/releases/tag/v0.13.3

* Wed Oct 5 2022 Jamie Curnow <jc@jc21.com> - 0.13.2-1
- https://github.com/dalance/procs/releases/tag/v0.13.2

* Wed Sep 21 2022 Jamie Curnow <jc@jc21.com> - 0.13.1-1
- https://github.com/dalance/procs/releases/tag/v0.13.1

* Mon Aug 1 2022 Jamie Curnow <jc@jc21.com> - 0.13.0-1
- https://github.com/dalance/procs/releases/tag/v0.13.0

* Wed May 25 2022 Jamie Curnow <jc@jc21.com> - 0.12.3-1
- https://github.com/dalance/procs/releases/tag/v0.12.3

* Thu May 5 2022 Jamie Curnow <jc@jc21.com> - 0.12.2-1
- https://github.com/dalance/procs/releases/tag/v0.12.2

* Mon Jan 31 2022 Jamie Curnow <jc@jc21.com> - 0.12.1-1
- https://github.com/dalance/procs/releases/tag/v0.12.1

* Wed Jan 19 2022 Jamie Curnow <jc@jc21.com> - 0.12.0-1
- https://github.com/dalance/procs/releases/tag/v0.12.0

* Sun Jan 2 2022 Jamie Curnow <jc@jc21.com> - 0.11.13-1
- https://github.com/dalance/procs/releases/tag/v0.11.13

* Wed Dec 15 2021 Jamie Curnow <jc@jc21.com> - 0.11.12-1
- https://github.com/dalance/procs/releases/tag/v0.11.12

* Tue Dec 14 2021 Jamie Curnow <jc@jc21.com> - 0.11.11-1
- https://github.com/dalance/procs/releases/tag/v0.11.11

* Wed Oct 20 2021 Jamie Curnow <jc@jc21.com> - 0.11.10-1
- https://github.com/dalance/procs/releases/tag/v0.11.10

* Tue Jun 22 2021 Jamie Curnow <jc@jc21.com> - 0.11.9-1
- https://github.com/dalance/procs/releases/tag/v0.11.9

* Mon Jun 21 2021 Jamie Curnow <jc@jc21.com> - 0.11.8-1
- https://github.com/dalance/procs/releases/tag/v0.11.8


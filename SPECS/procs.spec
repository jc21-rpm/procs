%global debug_package %{nil}

Name:           procs
Version:        0.11.9
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
* Tue Jun 22 2021 Jamie Curnow <jc@jc21.com> - 0.11.9-1
- https://github.com/dalance/procs/releases/tag/v0.11.9

* Mon Jun 21 2021 Jamie Curnow <jc@jc21.com> - 0.11.8-1
- https://github.com/dalance/procs/releases/tag/v0.11.8


Name:           osbuild-aboot
Version:        0.1
Release:        3%{?dist}
Summary:        osbuild integration of aboot (test version)

License:        GPLv2+
Source1:        org.osbuildtest.aboot.conf
Source2:        org.osbuildtest.aboot.update
Source3:        org.osbuildtest.write-device

Requires:       osbuild
BuildArch:      noarch

%description
Aboot support for osbuild

%prep
rm -rf %{name}-{%version}
mkdir %{name}-{%version}

%build
cd %{name}-{%version}

%install
cd %{name}-{%version}
mkdir -p %{buildroot}%{_prefix}/lib/osbuild/stages
install -m755 %{SOURCE1} %{buildroot}%{_prefix}/lib/osbuild/stages/org.osbuildtest.aboot.conf
install -m755 %{SOURCE2} %{buildroot}%{_prefix}/lib/osbuild/stages/org.osbuildtest.aboot.update
install -m755 %{SOURCE3} %{buildroot}%{_prefix}/lib/osbuild/stages/org.osbuildtest.write-device

%files
%{_prefix}/lib/osbuild/stages/org.osbuildtest.aboot.conf
%{_prefix}/lib/osbuild/stages/org.osbuildtest.aboot.update
%{_prefix}/lib/osbuild/stages/org.osbuildtest.write-device

%changelog
* Fri Aug 19 2022 Alexander Larsson <alexl@redhat.com>
- Initial version

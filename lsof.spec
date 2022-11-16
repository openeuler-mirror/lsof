Name:		lsof
Version:	4.96.4
Release:        2
Summary:	A tool for list open files
License:	zlib and Sendmail and LGPLv2+
URL:		https://people.freebsd.org/~abe/
Source0:	https://github.com/lsof-org/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:	gcc git libtirpc-devel libselinux-devel

%description
Lsof is a free, open-source, Unix administrative tool for displays information
about files open to Unix processes. It runs on many Unix dialects.

%package	help
Summary: 	Doc files for %{name}
BuildArch:	noarch
Requires:	man

%description 	help
The %{name}-help package contains doc files for %{name}.

%prep
%autosetup -n %{name}-%{version} -p1 -S git

%build
./Configure -n linux
%make_build DEBUG="%{build_cflags} -I/usr/include/tirpc" CFGL="%{build_ldflags} -L./lib -llsof -lselinux -ltirpc"
soelim -r Lsof.8 > lsof.1

%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 0755 lsof %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man1
install -p -m 0644 lsof.1 %{buildroot}/%{_mandir}/man1/lsof.1

%check
pushd tests
chmod u+w TestDB
./Add2TestDB
make test %{?_smp_mflags} DEBUG="%{optflags} -Wall -Wno-unused"
popd

%files
%doc 00CREDITS
%{_bindir}/%{name}

%files help
%doc 00README 00FAQ 00LSOF-L 00QUICKSTART
%{_mandir}/man*/*

%changelog
* Wed Nov 16 2022 dongyuzhen <dongyuzhen@h-partners.com> - 4.96.4-2
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix the format error in changelog

* Mon Nov 7 2022 Bin Hu <hubin73@huawei.com> - 4.96.4-1
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:update version 4.96.4

* Fri Aug 05 2022 renhongxun <renhongxun@h-partners.com> - 4.94.0-3
- fix spec so that man lsof can execute correctly

* Mon Jun 20 2022 renhongxun <renhongxun@h-partners.com> - 4.94.0-2
- enable check

* Sat Jan 23 2021 zoulin <zoulin13@huawei.com> - 4.94.0-1
- Type: enhancement
- ID: NA
- SUG: NA
- DESC: update version to 4.94.0

* Mon Oct 19 2020 yangshaoxing <yangshaoxing3@huawei.com> - 4.93.2-4
- Handle ffff:ffff in ipv6 addr correctly

* Fri Jan 10 2020 Yeqing Peng <pengyeqing@huawei.com> - 4.93.2-3
- delete unused file

* Mon Sep 30 2019 luhuaxin <luhuaxin@huawei.com> - 4.93.2-2
- Type: enhancement
- ID: NA
- SUG: NA
- DESC: package rebuild

* Tue Sep 3 2019 luhuaxin <luhuaxin@huawei.com> - 4.93.2-1
- Package init

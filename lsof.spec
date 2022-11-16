Name:		lsof
Version:	4.93.2
Release:        8
Summary:	A tool for list open files
License:	zlib and Sendmail and LGPLv2+
URL:		https://people.freebsd.org/~abe/
Source0:	https://github.com/lsof-org/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0: 	0050-endpoint-pipe-fix-list-the-same-fd-in-a-different-pr.patch
Patch1: 	0052-endpoint-pty-bug-fix-list-the-same-fd-in-a-different.patch
Patch2: 	0060-endpoint-pseudoterminal-bug-fix-fix-wrong-Unix98-PTY.patch
Patch3: 	Handle-ffff-ffff-in-ipv6-addr-correctly.patch
Patch4:		backport-Fill-the-buffer-using-pipe-communication-with-zero.patch

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

%files
%doc 00CREDITS
%{_bindir}/%{name}

%files help
%doc 00README 00FAQ 00LSOF-L 00QUICKSTART
%{_mandir}/man*/*

%changelog
* Wed Nov 16 2022 dongyuzhen <dongyuzhen@h-partners.com> - 4.93.2-8
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix the date error in changelog

* Tue Nov 15 2022 Bin Hu <hubin73@huawei.com> - 4.93.2-7
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix valgrind error write to uninitialized bytes

* Wed Aug 24 2022 yueyuankun <yueyuankun@kylinos.cn> - 4.93.2-6
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:Fix "man lsof" content error

* Wed Feb 10 2021 chenjialong <chenjialong@huawei.com> - 4.93.2-5
- Type:NA
- ID:NA
- SUG:NA
- DESC:rebuild.

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

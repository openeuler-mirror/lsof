Name:		lsof
Version:	4.93.2
Release:        2
Summary:	A tool for list open files
License:	zlib and Sendmail and LGPLv2+
URL:		https://people.freebsd.org/~abe/
Source0:	https://github.com/lsof-org/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:	upstream2downstream.sh
Patch0:         PATCH-FIX-OPENEULER-man-page-section.patch
Patch6002: 	0050-endpoint-pipe-fix-list-the-same-fd-in-a-different-pr.patch
Patch6003: 	0052-endpoint-pty-bug-fix-list-the-same-fd-in-a-different.patch
Patch6004: 	0060-endpoint-pseudoterminal-bug-fix-fix-wrong-Unix98-PTY.patch

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

%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 0755 lsof %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man1
install -p -m 0644 Lsof.8 %{buildroot}/%{_mandir}/man1/lsof.1

%files
%doc 00CREDITS
%{_bindir}/%{name}

%files help
%doc 00README 00FAQ 00LSOF-L 00QUICKSTART
%{_mandir}/man*/*

%changelog
* Mon Sep 30 2019 luhuaxin <luhuaxin@huawei.com> - 4.93.2-2
- Type: enhancement
- ID: NA
- SUG: NA
- DESC: package rebuild

* Tue Sep 3 2019 luhuaxin <luhuaxin@huawei.com> - 4.93.2-1
- Package init

#
# Conditional build:
%bcond_without	tests		# do not proceed cracking selftest (few minutes).
#
Summary:	Password recovery tool for Rar, 7z and Zip archives
Name:		rarcrack
Version:	0.2
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://downloads.sourceforge.net/project/rarcrack/rarcrack-%{version}/%5BUnnamed%20release%5D/%{name}-%{version}.tar.bz2
# Source0-md5:	62d0cf77c6c4edc7204305649f8b7362
Patch0:		%{name}-cflags.patch
Patch1:		%{name}-mime.patch
URL:		http://sourceforge.net/projects/rarcrack/
BuildRequires:	libxml2-devel
%if %{with tests}
BuildRequires:	p7zip
BuildRequires:	unrar
BuildRequires:	unzip
%endif
Requires:	file
Requires:	p7zip
Requires:	unrar
Requires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program uses a brute force algorithm to guess your encrypted
compressed file's password. If you forget your encrypted file
password, this program is the solution. This program can crack Zip, 7z
and Rar file passwords.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} CC="%{__cc}" CFLAGS="%{rpmcflags} %{rpmcppflags}"

%if %{with tests}
rm -f test.*.xml
# each test archive is encrypted with passwrd '100'.
./rarcrack test.7z
./rarcrack test.rar
./rarcrack test.zip
%endif

%install
rm -rf $RPM_BUILD_ROOT

install -D rarcrack $RPM_BUILD_ROOT%{_bindir}/rarcrack

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%attr(755,root,root) %{_bindir}/rarcrack

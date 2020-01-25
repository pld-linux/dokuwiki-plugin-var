%define		plugin		var
%define		php_min_version 5.0.0
Summary:	DokuWiki var plugin
Name:		dokuwiki-plugin-%{plugin}
Version:	20120624
Release:	3
License:	GPL v2
Group:		Applications/WWW
Source0:	https://github.com/dokufreaks/plugin-%{plugin}/tarball/master/%{plugin}-%{version}.tgz
# Source0-md5:	0e7b1e2428a53773f922eb020ca795b3
URL:		http://www.dokuwiki.org/plugin:var
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.520
Requires:	dokuwiki >= 20061106
Requires:	php(core) >= %{php_min_version}
Requires:	php(date)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
Displays some dynamic info about the current page, user or date. It
uses exactly the same syntax and variables as namespace templates.

%prep
%setup -qc
mv *-%{plugin}-*/* .

version=$(awk '/^date/{print $2}' plugin.info.txt)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
rm $RPM_BUILD_ROOT%{plugindir}/{COPYING,README}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{plugindir}
%{plugindir}/*.txt
%{plugindir}/*.php

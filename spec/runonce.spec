Summary: Run a script once on boot
Name: runonce
Version: 1.0.0
Release: 1
License: GPL
URL: http://www.shabazian.com
Group: System
Packager: Chip Shabazian
BuildRoot: ~/rpmbuild/
Requires: systemd

# Build with the following syntax:
# rpmbuild --target noarch -bb runonce.spec

%description
RunOnce will run a bash script that is located in /etc/local/runonce.d at boot then move that script to /etc/local/runonce.d/ran with a date/timestamp and create a logfile entry

%prep
echo "BUILDROOT = $RPM_BUILD_ROOT"
mkdir -p $RPM_BUILD_ROOT/usr/lib/systemd/system
mkdir -p $RPM_BUILD_ROOT/usr/local/sbin
cp ~/rpmbuild/runonce/usr/local/sbin/runonce.sh $RPM_BUILD_ROOT/usr/local/sbin/runonce.sh
cp ~/rpmbuild/runonce/usr/lib/systemd/system/runonce.service $RPM_BUILD_ROOT/usr/lib/systemd/system/runonce.service
exit

%files
%attr(0755, root, root) /usr/local/sbin/runonce.sh
%attr(0644, root, root) /usr/lib/systemd/system/runonce.service

%pre
mkdir -p /etc/local/runonce.d/ran

%post

%postun
systemctl daemon-reload

%clean
rm -rf $RPM_BUILD_ROOT/etc/*

%changelog
* Fri Jun 14 2019 Chip Shabazian <chip@shabazian.com>
  - Initial build


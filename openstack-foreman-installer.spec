%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global homedir /usr/share/openstack-foreman-installer

Name:	%{?scl_prefix}openstack-foreman-installer	
Version:	0.0.12
Release:	1%{?dist}
Summary:	Installer & Configuration tool for OpenStack

Group:		Applications/System
License:	GPLv2
URL:		https://github.com/jsomara/astapor
Source0: http://file.rdu.redhat.com:~/jomara/openstack-foreman-installer.tar.gz	

Requires: %{?scl_prefix}ruby-puppet
Requires:	packstack-modules-puppet
Requires: %{?scl_prefix}ruby
Requires: foreman >= 1.1
Requires: %{?scl_prefix}rubygem-foreman_openstack_simplify
# Requires: foreman-mysql >= 1.1
# Requires: foreman-installer >= 2.0
Requires: mysql-server

%description
Tools for configuring The Foreman for provisioning & configuration of
OpenStack.

%prep
%setup -q

%build

%install
install -d -m 0755 %{buildroot}%{homedir}
install -d -m 0755 %{buildroot}%{homedir}/bin
install -m 0755 bin/foreman-setup.rb %{buildroot}%{homedir}/bin
install -m 0755 bin/foreman_server.sh %{buildroot}%{homedir}/bin
install -m 0644 bin/foreman-params.json %{buildroot}%{homedir}/bin
install -d -m 0755 %{buildroot}%{homedir}/puppet/modules
cp -Rp puppet/* %{buildroot}%{homedir}/puppet/modules/
install -d -m 0755 %{buildroot}%{homedir}/config
install -m 0644 config/broker-ruby %{buildroot}%{homedir}/config
install -m 0644 config/database.yml %{buildroot}%{homedir}/config
install -m 0644 config/foreman-nightlies.repo %{buildroot}%{homedir}/config
install -m 0644 config/ruby193-passenger.conf %{buildroot}%{homedir}/config

%files
%{homedir}/
%{homedir}/bin/
%{homedir}/bin/foreman-setup.rb
%{homedir}/bin/foreman_server.sh
%{homedir}/bin/foreman-params.json
%{homedir}/puppet/
%{homedir}/puppet/*
%{homedir}/config/
%{homedir}/config/broker-ruby
%{homedir}/config/database.yml
%{homedir}/config/foreman-nightlies.repo
%{homedir}/config/ruby193-passenger.conf

%changelog
* Mon Jun 03 2013 Jordan OMara <jomara@redhat.com> 0.0.12-1
- tiny sed fix (cwolfe@redhat.com)
- Make openstack IP variables configurable rather than guessing.
  (cwolfe@redhat.com)
- tweaks to puppet modules needed for scl puppet 3.1. tweaks to pupet modules
  needed for client to work on scl puppet 3.1 (cwolfe@redhat.com)
- Merge pull request #9 from gildub/patch-2 (jsomara@gmail.com)
- Fixed missing comma in puppet crno (jomara@redhat.com)
- Copying packstack modules (jomara@redhat.com)
- Removing packstack puppet modules (jomara@redhat.com)
- Update readme with netowrk assumptions (gsutclif@redhat.com)
- fix BZ969531 - use scl to run puppet (gsutclif@redhat.com)
- Use CIDR for network ranges, numerical netmask doesn't work
  (gsutclif@redhat.com)
- Assume the controller node is on $(SECONDARY_NETWORK).3 (gsutclif@redhat.com)
- Allow gateway to be unset for private networks (gsutclif@redhat.com)
- Run db_sync as keystone user, or it produces root-owned log files
  (dcleal@redhat.com)
- Merge pull request #33 from domcleal/qpid-rpc (jsomara@gmail.com)
- Merge pull request #30 from cwolferh/subdir_cleanup (jsomara@gmail.com)
- Fix configuration of nova.conf and Qpid as RPC backend (dcleal@redhat.com)
- $FOREMAN_PROVISIONING - making foreman provisioning optional.
  (cwolfe@redhat.com)
- sanity check for $PUPPETMASTER (cwolfe@redhat.com)
- remove duplicated subdirs. (cwolfe@redhat.com)
- Commented apache - Puppet complains it's already defined! (gilles@redhat.com)

* Thu May 30 2013 Jordan OMara <jomara@redhat.com> 0.0.11-1
- Dynamic networking config (dcleal@redhat.com)
- Fix ordering (dcleal@redhat.com)

* Wed May 29 2013 Jordan OMara <jomara@redhat.com> 0.0.10-1
- fixing puppet module path (jomara@redhat.com)
- make the puppet agent on the server not be a service (cwolfe@redhat.com)

* Wed May 29 2013 Jordan OMara <jomara@redhat.com> 0.0.9-1
- puppet & script updates (jomara@redhat.com)

* Wed May 29 2013 Jordan OMara <jomara@redhat.com> 0.0.8-1
- tweaking foreman server (jomara@redhat.com)

* Wed May 29 2013 Jordan OMara <jomara@redhat.com> 0.0.7-1
- overriding custom repos (jomara@redhat.com)
- Adding the non custom puppet scripts (jomara@redhat.com)
- Removing submodules (jomara@redhat.com)

* Wed May 29 2013 Jordan OMara <jomara@redhat.com> 0.0.6-1
- Merge pull request #25 from GregSutcliffe/master (jsomara@gmail.com)
- Attempt to guess defaults for _all_ the params (gsutclif@redhat.com)
- Move trystack params to an common class, and use sed magic to put appropriate
  passwords in. (gsutclif@redhat.com)
- Parameterize trystack classes, remove old globals from JSON, style cleanup
  (gsutclif@redhat.com)
- updated locations of foreman installer puppet modules (cwolfe@redhat.com)
- foreman-installer submodules (cwolfe@redhat.com)
- Fix augtool as puppet.conf is in a non-standard location (dcleal@redhat.com)
- Adding db migrate script (jomara@redhat.com)
- Merge pull request #24 from domcleal/changeme (jsomara@gmail.com)
- Set each password differently to the last (dcleal@redhat.com)
- Fix broker-ruby location (dcleal@redhat.com)

* Tue May 28 2013 Jordan OMara <jomara@redhat.com> 0.0.5-1
- Merge remote-tracking branch 'origin/master' (jomara@redhat.com)
- bump submodule rev (cwolfe@redhat.com)
- Merge remote-tracking branch 'origin/master' (jomara@redhat.com)
- scl foreman-installer updates (cwolfe@redhat.com)
- Fixing some paths for SCL (jomara@redhat.com)
- SCL related stuff for generated client script (jistr@redhat.com)
- Include puppet::server in installer.pp (jistr@redhat.com)
- SCL paths for Puppet server configuration (jistr@redhat.com)

* Fri May 24 2013 Jordan OMara <jomara@redhat.com> 0.0.4-1
- Some fixes for 193 foreman (jomara@redhat.com)
- work in progress-- "puppet apply" tweaks.  note, no puppet::server
  (cwolfe@redhat.com)

* Fri May 24 2013 Jordan OMara <jomara@redhat.com> 0.0.3-1
- Changes for ruby193-foreman packages (jomara@redhat.com)

* Tue May 21 2013 Jordan OMara <jomara@redhat.com> 0.0.2-1
- new package built with tito

* Mon May 20 2013 Jordan OMara <jomara@redhat.com> 0.0.1-1
- initial packaging

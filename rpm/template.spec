Name:           ros-kinetic-swri-prefix-tools
Version:        2.3.0
Release:        0%{?dist}
Summary:        ROS swri_prefix_tools package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/swri-robotics/marti_common
Source0:        %{name}-%{version}.tar.gz

Requires:       python-psutil
BuildRequires:  ros-kinetic-catkin

%description
Contains scripts that are useful as prefix commands for nodes started by
roslaunch.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Fri May 25 2018 Elliot Johnson <elliot.johnson@swri.org> - 2.3.0-0
- Autogenerated by Bloom

* Fri May 11 2018 Elliot Johnson <elliot.johnson@swri.org> - 2.2.1-0
- Autogenerated by Bloom

* Mon Feb 12 2018 Elliot Johnson <elliot.johnson@swri.org> - 2.2.0-0
- Autogenerated by Bloom

* Fri Jan 26 2018 Elliot Johnson <elliot.johnson@swri.org> - 2.1.0-0
- Autogenerated by Bloom

* Mon Dec 18 2017 Elliot Johnson <elliot.johnson@swri.org> - 2.0.0-0
- Autogenerated by Bloom

* Fri Oct 13 2017 Elliot Johnson <elliot.johnson@swri.org> - 1.2.0-0
- Autogenerated by Bloom

* Thu Aug 31 2017 Elliot Johnson <elliot.johnson@swri.org> - 1.1.0-0
- Autogenerated by Bloom

* Thu Aug 03 2017 Elliot Johnson <elliot.johnson@swri.org> - 1.0.0-0
- Autogenerated by Bloom

* Tue Jun 20 2017 Elliot Johnson <elliot.johnson@swri.org> - 0.3.0-0
- Autogenerated by Bloom

* Tue Apr 11 2017 Elliot Johnson <elliot.johnson@swri.org> - 0.2.4-0
- Autogenerated by Bloom

* Fri Dec 09 2016 Elliot Johnson <elliot.johnson@swri.org> - 0.2.3-0
- Autogenerated by Bloom

* Wed Dec 07 2016 Elliot Johnson <elliot.johnson@swri.org> - 0.2.2-0
- Autogenerated by Bloom

* Sun Oct 23 2016 Elliot Johnson <elliot.johnson@swri.org> - 0.2.1-0
- Autogenerated by Bloom

* Tue Jun 21 2016 Elliot Johnson <elliot.johnson@swri.org> - 0.2.0-1
- Autogenerated by Bloom

* Tue Jun 21 2016 Elliot Johnson <elliot.johnson@swri.org> - 0.2.0-0
- Autogenerated by Bloom


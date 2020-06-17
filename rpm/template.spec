%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-swri-rospy
Version:        2.13.6
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS swri_rospy package

License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-rospy
Requires:       ros-noetic-std-msgs
Requires:       ros-noetic-std-srvs
BuildRequires:  python3-setuptools
BuildRequires:  ros-noetic-catkin
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
This package provides added functionality on top of rospy, including a single-
threaded callback queue.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Wed Jun 17 2020 P. J. Reed <preed@swri.edu> - 2.13.6-1
- Autogenerated by Bloom

* Wed Jun 17 2020 P. J. Reed <preed@swri.edu> - 2.13.5-1
- Autogenerated by Bloom

* Tue Jun 16 2020 P. J. Reed <preed@swri.edu> - 2.13.4-1
- Autogenerated by Bloom

* Fri Jun 12 2020 P. J. Reed <preed@swri.edu> - 2.13.3-1
- Autogenerated by Bloom

* Wed Jun 10 2020 P. J. Reed <preed@swri.edu> - 2.13.2-1
- Autogenerated by Bloom


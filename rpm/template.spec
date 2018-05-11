Name:           ros-indigo-swri-yaml-util
Version:        2.2.1
Release:        0%{?dist}
Summary:        ROS swri_yaml_util package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/swri-robotics/marti_common
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       yaml-cpp-devel
BuildRequires:  boost-devel
BuildRequires:  pkgconfig
BuildRequires:  ros-indigo-catkin
BuildRequires:  yaml-cpp-devel

%description
Provides wrappers around the yaml-cpp library for various utility functions and
to abstract out the API changes made to yaml-cpp between ubuntu:precise and
ubuntu:trusty.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri May 11 2018 Marc Alban <malban@swri.org> - 2.2.1-0
- Autogenerated by Bloom

* Mon Feb 12 2018 Marc Alban <malban@swri.org> - 2.2.0-0
- Autogenerated by Bloom

* Fri Jan 26 2018 Marc Alban <malban@swri.org> - 2.1.0-0
- Autogenerated by Bloom

* Mon Dec 18 2017 Marc Alban <malban@swri.org> - 2.0.0-0
- Autogenerated by Bloom

* Fri Oct 13 2017 Marc Alban <malban@swri.org> - 1.2.0-0
- Autogenerated by Bloom

* Thu Aug 31 2017 Marc Alban <malban@swri.org> - 1.1.0-0
- Autogenerated by Bloom

* Wed Aug 02 2017 Marc Alban <malban@swri.org> - 1.0.0-0
- Autogenerated by Bloom

* Tue Jun 20 2017 Marc Alban <malban@swri.org> - 0.3.0-0
- Autogenerated by Bloom

* Tue Apr 11 2017 Marc Alban <malban@swri.org> - 0.0.14-0
- Autogenerated by Bloom

* Sat Mar 18 2017 Marc Alban <malban@swri.org> - 0.0.13-1
- Autogenerated by Bloom

* Sun Oct 23 2016 Marc Alban <malban@swri.org> - 0.0.13-0
- Autogenerated by Bloom

* Sun Aug 14 2016 Marc Alban <malban@swri.org> - 0.0.12-0
- Autogenerated by Bloom

* Fri May 13 2016 Marc Alban <malban@swri.org> - 0.0.11-0
- Autogenerated by Bloom

* Thu May 12 2016 Marc Alban <malban@swri.org> - 0.0.10-3
- Autogenerated by Bloom

* Thu May 12 2016 Marc Alban <malban@swri.org> - 0.0.10-2
- Autogenerated by Bloom

* Thu May 12 2016 Marc Alban <malban@swri.org> - 0.0.10-1
- Autogenerated by Bloom

* Thu May 12 2016 Marc Alban <malban@swri.org> - 0.0.10-0
- Autogenerated by Bloom


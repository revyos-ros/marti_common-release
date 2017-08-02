Name:           ros-indigo-swri-image-util
Version:        1.0.0
Release:        0%{?dist}
Summary:        ROS swri_image_util package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/swri-robotics/marti_common
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-indigo-camera-calibration-parsers
Requires:       ros-indigo-cv-bridge
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-image-geometry
Requires:       ros-indigo-image-transport
Requires:       ros-indigo-message-filters
Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-nodelet
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rospy
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-swri-geometry-util
Requires:       ros-indigo-swri-math-util
Requires:       ros-indigo-swri-opencv-util
Requires:       ros-indigo-swri-roscpp
Requires:       ros-indigo-tf
BuildRequires:  eigen3-devel
BuildRequires:  pkgconfig
BuildRequires:  ros-indigo-camera-calibration-parsers
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cv-bridge
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-image-geometry
BuildRequires:  ros-indigo-image-transport
BuildRequires:  ros-indigo-message-filters
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-nodelet
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-rostest
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-swri-geometry-util
BuildRequires:  ros-indigo-swri-math-util
BuildRequires:  ros-indigo-swri-nodelet
BuildRequires:  ros-indigo-swri-opencv-util
BuildRequires:  ros-indigo-swri-roscpp
BuildRequires:  ros-indigo-tf

%description
swri_image_util

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
* Wed Aug 02 2017 Kris Kozak <kkozak@swri.org> - 1.0.0-0
- Autogenerated by Bloom

* Tue Jun 20 2017 Kris Kozak <kkozak@swri.org> - 0.3.0-0
- Autogenerated by Bloom

* Tue Apr 11 2017 Kris Kozak <kkozak@swri.org> - 0.0.14-0
- Autogenerated by Bloom

* Sat Mar 18 2017 Kris Kozak <kkozak@swri.org> - 0.0.13-1
- Autogenerated by Bloom

* Sun Oct 23 2016 Kris Kozak <kkozak@swri.org> - 0.0.13-0
- Autogenerated by Bloom

* Sun Aug 14 2016 Kris Kozak <kkozak@swri.org> - 0.0.12-0
- Autogenerated by Bloom

* Fri May 13 2016 Kris Kozak <kkozak@swri.org> - 0.0.11-0
- Autogenerated by Bloom

* Thu May 12 2016 Kris Kozak <kkozak@swri.org> - 0.0.10-3
- Autogenerated by Bloom

* Thu May 12 2016 Kris Kozak <kkozak@swri.org> - 0.0.10-2
- Autogenerated by Bloom

* Thu May 12 2016 Kris Kozak <kkozak@swri.org> - 0.0.10-1
- Autogenerated by Bloom

* Thu May 12 2016 Kris Kozak <kkozak@swri.org> - 0.0.10-0
- Autogenerated by Bloom


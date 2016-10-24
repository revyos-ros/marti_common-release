Name:           ros-jade-swri-image-util
Version:        0.1.6
Release:        0%{?dist}
Summary:        ROS swri_image_util package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/swri-robotics/marti_common
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       qt-devel
Requires:       ros-jade-camera-calibration-parsers
Requires:       ros-jade-cv-bridge
Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-image-geometry
Requires:       ros-jade-image-transport
Requires:       ros-jade-nav-msgs
Requires:       ros-jade-nodelet
Requires:       ros-jade-roscpp
Requires:       ros-jade-rospy
Requires:       ros-jade-std-msgs
Requires:       ros-jade-swri-math-util
Requires:       ros-jade-swri-opencv-util
Requires:       ros-jade-tf
BuildRequires:  eigen3-devel
BuildRequires:  pkgconfig
BuildRequires:  qt-devel
BuildRequires:  ros-jade-camera-calibration-parsers
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-cv-bridge
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-image-geometry
BuildRequires:  ros-jade-image-transport
BuildRequires:  ros-jade-nav-msgs
BuildRequires:  ros-jade-nodelet
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-rospy
BuildRequires:  ros-jade-rostest
BuildRequires:  ros-jade-std-msgs
BuildRequires:  ros-jade-swri-math-util
BuildRequires:  ros-jade-swri-opencv-util
BuildRequires:  ros-jade-tf

%description
swri_image_util

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Sun Oct 23 2016 Kris Kozak <kkozak@swri.org> - 0.1.6-0
- Autogenerated by Bloom

* Fri May 13 2016 Kris Kozak <kkozak@swri.org> - 0.1.5-0
- Autogenerated by Bloom

* Thu May 12 2016 Kris Kozak <kkozak@swri.org> - 0.1.4-0
- Autogenerated by Bloom


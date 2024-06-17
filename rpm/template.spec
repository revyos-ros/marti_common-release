%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/jazzy/.*$
%global __requires_exclude_from ^/opt/ros/jazzy/.*$

Name:           ros-jazzy-swri-image-util
Version:        3.6.1
Release:        4%{?dist}%{?release_suffix}
Summary:        ROS swri_image_util package

License:        BSD
URL:            https://github.com/swri-robotics/marti_common
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       boost-python%{python3_pkgversion}-devel
Requires:       eigen3-devel
Requires:       ros-jazzy-ament-index-cpp
Requires:       ros-jazzy-camera-calibration-parsers
Requires:       ros-jazzy-cv-bridge
Requires:       ros-jazzy-geometry-msgs
Requires:       ros-jazzy-image-geometry
Requires:       ros-jazzy-image-transport
Requires:       ros-jazzy-message-filters
Requires:       ros-jazzy-nav-msgs
Requires:       ros-jazzy-rclcpp
Requires:       ros-jazzy-rclcpp-components
Requires:       ros-jazzy-rclpy
Requires:       ros-jazzy-std-msgs
Requires:       ros-jazzy-swri-geometry-util
Requires:       ros-jazzy-swri-math-util
Requires:       ros-jazzy-swri-opencv-util
Requires:       ros-jazzy-swri-roscpp
Requires:       ros-jazzy-tf2
Requires:       ros-jazzy-ros-workspace
BuildRequires:  boost-devel
BuildRequires:  boost-python%{python3_pkgversion}-devel
BuildRequires:  eigen3-devel
BuildRequires:  pkgconfig
BuildRequires:  ros-jazzy-ament-cmake
BuildRequires:  ros-jazzy-ament-index-cpp
BuildRequires:  ros-jazzy-camera-calibration-parsers
BuildRequires:  ros-jazzy-cv-bridge
BuildRequires:  ros-jazzy-geometry-msgs
BuildRequires:  ros-jazzy-image-geometry
BuildRequires:  ros-jazzy-image-transport
BuildRequires:  ros-jazzy-message-filters
BuildRequires:  ros-jazzy-nav-msgs
BuildRequires:  ros-jazzy-rclcpp
BuildRequires:  ros-jazzy-rclcpp-components
BuildRequires:  ros-jazzy-rclpy
BuildRequires:  ros-jazzy-std-msgs
BuildRequires:  ros-jazzy-swri-geometry-util
BuildRequires:  ros-jazzy-swri-math-util
BuildRequires:  ros-jazzy-swri-opencv-util
BuildRequires:  ros-jazzy-swri-roscpp
BuildRequires:  ros-jazzy-tf2
BuildRequires:  ros-jazzy-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-jazzy-ament-cmake-gtest
%endif

%description
swri_image_util

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/jazzy" \
    -DAMENT_PREFIX_PATH="/opt/ros/jazzy" \
    -DCMAKE_PREFIX_PATH="/opt/ros/jazzy" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/jazzy

%changelog
* Mon Jun 17 2024 P. J. Reed <preed@swri.org> - 3.6.1-4
- Autogenerated by Bloom

* Thu Apr 18 2024 P. J. Reed <preed@swri.org> - 3.6.1-3
- Autogenerated by Bloom

* Wed Mar 06 2024 P. J. Reed <preed@swri.org> - 3.6.1-2
- Autogenerated by Bloom


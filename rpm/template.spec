Name:           ros-indigo-rtt
Version:        2.8.0
Release:        1%{?dist}
Summary:        ROS rtt package

Group:          Development/Libraries
License:        GPL v2 with linking exception
URL:            http://www.orocos.org/rtt
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       omniORB
Requires:       omniORB-devel
Requires:       omniORB-servers
Requires:       perl-XML-XPath
Requires:       pkgconfig
Requires:       ros-indigo-catkin
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  omniORB
BuildRequires:  omniORB-devel
BuildRequires:  omniORB-servers
BuildRequires:  perl-XML-XPath
BuildRequires:  pkgconfig
BuildRequires:  ros-indigo-catkin

%description
Orocos/RTT component framework

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
* Fri Jan 23 2015 RTT Developers <orocos-dev@lists.mech.kuleuven.be> - 2.8.0-1
- Autogenerated by Bloom

* Fri Jan 23 2015 RTT Developers <orocos-dev@lists.mech.kuleuven.be> - 2.8.0-0
- Autogenerated by Bloom


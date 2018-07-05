Name:           xash3d-sdl
Version:        0.19.2
Release:        0
License:        GPL-3.0-and-HLSDK
Summary:        Xash3D FWGS Engine
Group:          Amusements/Games/Action/Shoot
URL:            https://github.com/FWGS/xash3d
Source:         %{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  SDL2-devel
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
#BuildRequires:  vgui-devel

%description
Xash3D FWGS is a fork of Xash3D Engine with enhanced features: crossplatform, multiplayer and so on.

%prep
%setup -q

%build
cd engine/xash3d/
%cmake \
  -DXASH_SDL=ON -DXASH_VGUI=OFF -DXASH_DLL_LOADER=OFF -DXASH_RELEASE=ON \
  -DXASH_WES=ON \
  -DXASH_WES_SRC=$PWD/../gl-wes-v2 \
  -DXASH_NANOGL_SRC=$PWD/../nanogl \
  -DMAINUI_NAME=menu \
  -DXASH_SAILFISH=ON
make %{?_smp_mflags} V=0
cd ../hlsdk-xash3d/cl_dll
make -f ../../../microndk/Microndk.mk %{?_smp_mflags} clean
make -f ../../../microndk/Microndk.mk %{?_smp_mflags}
cd ../dlls
make -f ../../../microndk/Microndk.mk %{?_smp_mflags} clean
make -f ../../../microndk/Microndk.mk %{?_smp_mflags}

%install
cd engine/xash3d
make install DESTDIR=%{buildroot}
cd ../hlsdk-xash3d/cl_dll
install -m 755 libclient.so %{buildroot}/%{_libdir}/xash3d/libclient.so
cd ../dlls
install -m 755 libserver.so %{buildroot}/%{_libdir}/xash3d/libserver.so

%files
%{_bindir}/xash3d
%{_libdir}/xash3d/

%changelog

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: 3d985eb
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : knights
Version  : 24.02.0
Release  : 22
URL      : https://download.kde.org/stable/release-service/24.02.0/src/knights-24.02.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.02.0/src/knights-24.02.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.02.0/src/knights-24.02.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-3.0
Requires: knights-bin = %{version}-%{release}
Requires: knights-data = %{version}-%{release}
Requires: knights-license = %{version}-%{release}
Requires: knights-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kplotting-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Sound files taken from pychess (http://pychess.org/).
Original files were renamed as follows:

%package bin
Summary: bin components for the knights package.
Group: Binaries
Requires: knights-data = %{version}-%{release}
Requires: knights-license = %{version}-%{release}

%description bin
bin components for the knights package.


%package data
Summary: data components for the knights package.
Group: Data

%description data
data components for the knights package.


%package doc
Summary: doc components for the knights package.
Group: Documentation

%description doc
doc components for the knights package.


%package license
Summary: license components for the knights package.
Group: Default

%description license
license components for the knights package.


%package locales
Summary: locales components for the knights package.
Group: Default

%description locales
locales components for the knights package.


%prep
%setup -q -n knights-24.02.0
cd %{_builddir}/knights-24.02.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1710535357
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1710535357
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/knights
cp %{_builddir}/knights-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/knights/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/knights-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/knights/06877624ea5c77efe3b7e39b0f909eda6e25a4ec || :
cp %{_builddir}/knights-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/knights/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/knights-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/knights/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/knights-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/knights/2123756e0b1fc8243547235a33c0fcabfe3b9a51 || :
cp %{_builddir}/knights-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/knights/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/knights-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/knights/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/knights-%{version}/sounds/LICENSE %{buildroot}/usr/share/package-licenses/knights/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang knights

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/knights

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.knights.desktop
/usr/share/config.kcfg/knights.kcfg
/usr/share/dbus-1/interfaces/org.kde.Knights.xml
/usr/share/icons/hicolor/16x16/apps/knights.png
/usr/share/icons/hicolor/32x32/apps/knights.png
/usr/share/icons/hicolor/48x48/apps/knights.png
/usr/share/icons/hicolor/64x64/apps/knights.png
/usr/share/knights/sounds/capture_black.ogg
/usr/share/knights/sounds/capture_white.ogg
/usr/share/knights/sounds/move_black.ogg
/usr/share/knights/sounds/move_white.ogg
/usr/share/knights/themes/default.desktop
/usr/share/knights/themes/east_west.desktop
/usr/share/knights/themes/east_west.png
/usr/share/knights/themes/east_west.svgz
/usr/share/knights/themes/gray.png
/usr/share/knights/themes/gray.svgz
/usr/share/knights/themes/knights.desktop
/usr/share/knights/themes/knights.png
/usr/share/knights/themes/knights.svgz
/usr/share/knights/themes/plain.desktop
/usr/share/knights/themes/plain.png
/usr/share/knights/themes/plain.svgz
/usr/share/knights/themes/xboard2.desktop
/usr/share/knights/themes/xboard2.png
/usr/share/knights/themes/xboard2.svgz
/usr/share/knsrcfiles/knights.knsrc
/usr/share/metainfo/org.kde.knights.appdata.xml
/usr/share/qlogging-categories6/knights.categories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/knights/Knights-engines.png
/usr/share/doc/HTML/ca/knights/Knights-newgame-dialog.png
/usr/share/doc/HTML/ca/knights/Knights-server-account.png
/usr/share/doc/HTML/ca/knights/Knights-server-challenges.png
/usr/share/doc/HTML/ca/knights/Knights-server-graph.png
/usr/share/doc/HTML/ca/knights/Knights-server-list.png
/usr/share/doc/HTML/ca/knights/index.cache.bz2
/usr/share/doc/HTML/ca/knights/index.docbook
/usr/share/doc/HTML/de/knights/Knights-newgame-dialog.png
/usr/share/doc/HTML/de/knights/Knights-server-account.png
/usr/share/doc/HTML/de/knights/Knights-server-challenges.png
/usr/share/doc/HTML/de/knights/Knights-server-graph.png
/usr/share/doc/HTML/de/knights/Knights-server-list.png
/usr/share/doc/HTML/de/knights/index.cache.bz2
/usr/share/doc/HTML/de/knights/index.docbook
/usr/share/doc/HTML/en/knights/Knights-board-setup.png
/usr/share/doc/HTML/en/knights/Knights-board.png
/usr/share/doc/HTML/en/knights/Knights-castle-kingside.png
/usr/share/doc/HTML/en/knights/Knights-castle-queenside.png
/usr/share/doc/HTML/en/knights/Knights-danger.png
/usr/share/doc/HTML/en/knights/Knights-engines.png
/usr/share/doc/HTML/en/knights/Knights-enpassant.png
/usr/share/doc/HTML/en/knights/Knights-lastmove.png
/usr/share/doc/HTML/en/knights/Knights-move-bishop.png
/usr/share/doc/HTML/en/knights/Knights-move-king.png
/usr/share/doc/HTML/en/knights/Knights-move-knight.png
/usr/share/doc/HTML/en/knights/Knights-move-limits.png
/usr/share/doc/HTML/en/knights/Knights-move-pawn.png
/usr/share/doc/HTML/en/knights/Knights-move-queen.png
/usr/share/doc/HTML/en/knights/Knights-move-rook.png
/usr/share/doc/HTML/en/knights/Knights-moving-queen.png
/usr/share/doc/HTML/en/knights/Knights-newgame-dialog.png
/usr/share/doc/HTML/en/knights/Knights-server-account.png
/usr/share/doc/HTML/en/knights/Knights-server-challenges.png
/usr/share/doc/HTML/en/knights/Knights-server-graph.png
/usr/share/doc/HTML/en/knights/Knights-server-list.png
/usr/share/doc/HTML/en/knights/index.cache.bz2
/usr/share/doc/HTML/en/knights/index.docbook
/usr/share/doc/HTML/es/knights/index.cache.bz2
/usr/share/doc/HTML/es/knights/index.docbook
/usr/share/doc/HTML/et/knights/index.cache.bz2
/usr/share/doc/HTML/et/knights/index.docbook
/usr/share/doc/HTML/fr/knights/index.cache.bz2
/usr/share/doc/HTML/fr/knights/index.docbook
/usr/share/doc/HTML/it/knights/index.cache.bz2
/usr/share/doc/HTML/it/knights/index.docbook
/usr/share/doc/HTML/nl/knights/index.cache.bz2
/usr/share/doc/HTML/nl/knights/index.docbook
/usr/share/doc/HTML/pt/knights/index.cache.bz2
/usr/share/doc/HTML/pt/knights/index.docbook
/usr/share/doc/HTML/pt_BR/knights/index.cache.bz2
/usr/share/doc/HTML/pt_BR/knights/index.docbook
/usr/share/doc/HTML/ru/knights/Knights-newgame-dialog.png
/usr/share/doc/HTML/ru/knights/Knights-server-account.png
/usr/share/doc/HTML/ru/knights/Knights-server-challenges.png
/usr/share/doc/HTML/ru/knights/Knights-server-graph.png
/usr/share/doc/HTML/ru/knights/Knights-server-list.png
/usr/share/doc/HTML/ru/knights/index.cache.bz2
/usr/share/doc/HTML/ru/knights/index.docbook
/usr/share/doc/HTML/sv/knights/index.cache.bz2
/usr/share/doc/HTML/sv/knights/index.docbook
/usr/share/doc/HTML/uk/knights/Knights-engines.png
/usr/share/doc/HTML/uk/knights/Knights-newgame-dialog.png
/usr/share/doc/HTML/uk/knights/Knights-server-account.png
/usr/share/doc/HTML/uk/knights/Knights-server-challenges.png
/usr/share/doc/HTML/uk/knights/Knights-server-graph.png
/usr/share/doc/HTML/uk/knights/Knights-server-list.png
/usr/share/doc/HTML/uk/knights/index.cache.bz2
/usr/share/doc/HTML/uk/knights/index.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/knights/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/knights/2123756e0b1fc8243547235a33c0fcabfe3b9a51
/usr/share/package-licenses/knights/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/knights/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/knights/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/knights/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files locales -f knights.lang
%defattr(-,root,root,-)


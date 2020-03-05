#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : knights
Version  : 19.12.3
Release  : 16
URL      : https://download.kde.org/stable/release-service/19.12.3/src/knights-19.12.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/19.12.3/src/knights-19.12.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/19.12.3/src/knights-19.12.3.tar.xz.sig
Summary  : Chess board by KDE with XBoard protocol support
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: knights-bin = %{version}-%{release}
Requires: knights-data = %{version}-%{release}
Requires: knights-license = %{version}-%{release}
Requires: knights-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kplotting-dev
BuildRequires : libkdegames-dev
BuildRequires : plasma-framework-dev

%description
###############################################################
General information
###############################################################
https://github.com/google/sanitizers/wiki
http://clang.llvm.org/docs/index.html
https://llvm.org/svn/llvm-project/compiler-rt/trunk/lib/asan/scripts/asan_symbolize.py
http://developerblog.redhat.com/2014/10/16/gcc-undefined-behavior-sanitizer-ubsan/

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
%setup -q -n knights-19.12.3
cd %{_builddir}/knights-19.12.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583451944
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1583451944
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/knights
cp %{_builddir}/knights-19.12.3/LICENSE %{buildroot}/usr/share/package-licenses/knights/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
cp %{_builddir}/knights-19.12.3/sounds/LICENSE %{buildroot}/usr/share/package-licenses/knights/8624bcdae55baeef00cd11d5dfcfa60f68710a02
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
/usr/share/kxmlgui5/knights/knightsui.rc
/usr/share/metainfo/org.kde.knights.appdata.xml
/usr/share/qlogging-categories5/knights.categories
/usr/share/xdg/knights.knsrc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/knights/Knights-board-setup.png
/usr/share/doc/HTML/ca/knights/Knights-board.png
/usr/share/doc/HTML/ca/knights/Knights-castle-kingside.png
/usr/share/doc/HTML/ca/knights/Knights-castle-queenside.png
/usr/share/doc/HTML/ca/knights/Knights-danger.png
/usr/share/doc/HTML/ca/knights/Knights-engines.png
/usr/share/doc/HTML/ca/knights/Knights-enpassant.png
/usr/share/doc/HTML/ca/knights/Knights-lastmove.png
/usr/share/doc/HTML/ca/knights/Knights-move-bishop.png
/usr/share/doc/HTML/ca/knights/Knights-move-king.png
/usr/share/doc/HTML/ca/knights/Knights-move-knight.png
/usr/share/doc/HTML/ca/knights/Knights-move-limits.png
/usr/share/doc/HTML/ca/knights/Knights-move-pawn.png
/usr/share/doc/HTML/ca/knights/Knights-move-queen.png
/usr/share/doc/HTML/ca/knights/Knights-move-rook.png
/usr/share/doc/HTML/ca/knights/Knights-moving-queen.png
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
/usr/share/package-licenses/knights/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files locales -f knights.lang
%defattr(-,root,root,-)


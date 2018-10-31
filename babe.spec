Name:		babe
Summary:	Babe Media Player
Version:	1.2.1
Release:	2
Group:		Graphical desktop/KDE
License:	GPLv2
Url:		https://babe.kde.org/
Source0:	http://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)

BuildRequires:  cmake(ECM)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5WebChannel)
BuildRequires:  cmake(Qt5WebEngineCore)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5WebEngineWidgets)
BuildRequires:  cmake(Qt5WebSockets)
BuildRequires:  cmake(Qt5)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(Gettext)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5)
BuildRequires:  cmake(Taglib)
BuildRequires:	pkgconfig(taglib)

%description
Babe will handle your whole music collection
by retreaving semantic information from the web.

Just relax, enjoy and discover your new music 

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files
%doc README.md
%{_bindir}/%{name}
%{_iconsdir}/hicolor/*/apps/*.svg
%{_datadir}/applications/org.kde.babe.desktop
%{_datadir}/metainfo/org.kde.babe.appdata.xml


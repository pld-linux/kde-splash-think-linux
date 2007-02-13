
%define		_splash		think-linux

Summary:	KDE splash screen
Summary(pl.UTF-8):	Ekran startowy KDE
Name:		kde-splash-%{_splash}
Version:	1.0
Release:	2
License:	GPL
Group:		X11/Amusements
#Source0:	http://www.kde-look.org/content/download.php?content=12577&id=1
Source0:	http://www.kde-look.org/content/files/12577-think-linux.tar.bz2
# Source0-md5:	a3ee3b84719b124f90283555bca8f2d2
URL:		http://www.kde-look.org/content/show.php?content=12577
Provides:	kde-splash
Requires:	kdebase-desktop >= 9:3.2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nice splash with Tux planning to do something nasty to MSN butterfly :)

%description -l pl.UTF-8
Ładny motyw z Tuxem planującym zrobić coś okropnego z motylkiem MSN :)

%prep
%setup -q -n %{_splash}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}
install * $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/%{_splash}

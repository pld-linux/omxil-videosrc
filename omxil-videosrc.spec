Summary:	Video Source component for Bellagio OpenMAX IL
Summary(pl.UTF-8):	Komponent źródła obrazu (Video Source) dla implementacji Bellagio OpenMAX IL
Name:		omxil-videosrc
Version:	0.1
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/omxil/libomxvideosrc-%{version}.tar.gz
# Source0-md5:	60ba58340f2e1e2056abc1d54e298cc0
URL:		http://omxil.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libomxil-bellagio-devel >= 0.9
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires:	libomxil-bellagio >= 0.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		/usr/%{_lib}/bellagio

%description
Video Source component is a video source component for Bellagio
OpenMAX IL that uses Video4Linux2 interface.

%description -l pl.UTF-8
Komponent Video Source to komponent źródła obrazu dla implementacji
Bellagio OpenMAX IL, wykorzystujący interfejs Video4Linux2.

%prep
%setup -q -n libomxvideosrc-%{version}

# warning about set but unused variable
sed -i -e 's/ -Werror//' configure.ac

%build
# rebuild for as-needed to work
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/libomxvideosrc.so*

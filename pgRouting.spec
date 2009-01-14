#
# TODO:
#  * %{_datadir}/postlbs will probably be shared between 
#    many elements of the postgres LBS system
#  * polish letters in pl description

%define		_name	pgrouting
Summary:	Routing functionality for postgreSQL GIS system
Summary(pl.UTF-8):      Obsluga ruchu dla systemu GIS postgreSQL
Name:		pgRouting
Version:	1.03
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://files.postlbs.org/pgrouting/source/%{name}-%{version}.tgz
# Source0-md5:	ee700d18a984b8fd78c1a739ca078683
URL:		http://pgrouting.postlbs.org/
BuildRequires:	boost-devel >= 1.33
BuildRequires:	CGAL-devel >= 3.2
BuildRequires:	gaul-devel
Requires:	postgis >= 1.0
Requires:	postgresql >= 8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Routing functionality for postgreSQL GIS system, includes TSP and DD algorithms.

%description -l pl.UTF-8
Obsluga ruchu dla systemu GIS postgreSQL. Wkompilowano algorytmy dla problemow 
komiwojazera i obliczania dlugosci przejazdu drogami (Driving Distance).

%prep

%setup -q -n %{_name}

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DWITH_TSP=ON \
	-DWITH_DD=ON \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig


%files
%defattr(644,root,root,755)
%doc README.routing
%attr(755,root,root) %{_libdir}/postgresql/*.so
%{_datadir}/postlbs

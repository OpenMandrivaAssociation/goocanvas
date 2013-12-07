%define major	3
%define libname %mklibname goocanvas %{major}
%define devname %mklibname -d goocanvas

Name:		goocanvas
Version:	1.0.0
Release:	9
Summary:	New canvas widget for GTK+ that uses the cairo 2D library
Group:		Development/GNOME and GTK+
License:	LGPL+
Url:		http://sourceforge.net/projects/goocanvas
Source0:		http://ftp.gnome.org/pub/GNOME/sources/goocanvas/%{name}-%{version}.tar.bz2

BuildRequires:	intltool
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gtk+-2.0)

%description
GooCanvas is a new canvas widget for GTK+ that uses the cairo 2D library for 
drawing. It has a model/view split, and uses interfaces for canvas items and 
views, so you can easily turn any application object into canvas items.

%package -n %{libname}
Summary:	New canvas widget for GTK+ that uses the cairo 2D library
Group:		System/Libraries
Suggests:	%{name}-i18n >= %{version}
Provides:	lib%{name} = %{version}-%{release}

%description -n %{libname}
This package contains the shared library for goocanvas.

%package i18n
Summary:	New canvas widget for GTK+ that uses the cairo 2D library
Group:		System/Internationalization

%description i18n
This package contains the translations for goocanvas.

%package -n %{devname}
Summary:	New canvas widget for GTK+ that uses the cairo 2D library
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the development libraries, include files 
and documentation.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make LIBS=-lm

%install
%makeinstall_std
%find_lang %{name}

%files -n %{libname}
%doc README COPYING AUTHORS
%{_libdir}/libgoocanvas.so.%{major}*

%files i18n -f %{name}.lang

%files -n %{devname}
%doc %{_datadir}/gtk-doc/html/%{name}
%{_includedir}/%{name}-1.0
%{_libdir}/*.so
%{_libdir}/pkgconfig/*


%define major 3
%define libname %mklibname goocanvas %{major}
%define develname %mklibname -d goocanvas

Name:		goocanvas
Version:	1.0.0
Release:	6
Summary:	New canvas widget for GTK+ that uses the cairo 2D library
Group:		Development/GNOME and GTK+
License:	LGPL+
URL:		http://sourceforge.net/projects/goocanvas
Source:		http://ftp.gnome.org/pub/GNOME/sources/goocanvas/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	gnome-doc-utils
BuildRequires:	intltool

%description
GooCanvas is a new canvas widget for GTK+ that uses the cairo 2D library for 
drawing. It has a model/view split, and uses interfaces for canvas items and 
views, so you can easily turn any application object into canvas items.

%package -n %{libname}
Summary:	New canvas widget for GTK+ that uses the cairo 2D library
Group:		System/Libraries
Requires:	%{name}-i18n >= %{version}
Provides:	lib%{name} = %{version}-%{release}

%description -n %{libname}
This package contains the shared library for goocanvas.

%package i18n
Summary:	New canvas widget for GTK+ that uses the cairo 2D library
Group:		System/Internationalization

%description i18n
This package contains the translations for goocanvas.

%package -n %{develname}
Summary:	New canvas widget for GTK+ that uses the cairo 2D library
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
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

%files -n %{develname}
%doc %{_datadir}/gtk-doc/html/%{name}
%{_includedir}/%{name}-1.0
%{_libdir}/*.so
%{_libdir}/pkgconfig/*


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-3mdv2011.0
+ Revision: 664916
- mass rebuild

  + Götz Waschk <waschk@mandriva.org>
    - rebuild
    - new version

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 0.15-3mdv2011.0
+ Revision: 605492
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.15-2mdv2010.1
+ Revision: 522743
- rebuilt for 2010.1

* Mon Jun 29 2009 Götz Waschk <waschk@mandriva.org> 0.15-1mdv2010.0
+ Revision: 390745
- update to new version 0.15

* Sun Mar 15 2009 Götz Waschk <waschk@mandriva.org> 0.14-1mdv2009.1
+ Revision: 355405
- update to new version 0.14

* Sun Nov 30 2008 Götz Waschk <waschk@mandriva.org> 0.13-1mdv2009.1
+ Revision: 308480
- new version
- update source URL

* Sun Sep 21 2008 Götz Waschk <waschk@mandriva.org> 0.12-1mdv2009.0
+ Revision: 286318
- new version
- fix license

* Tue Sep 09 2008 Götz Waschk <waschk@mandriva.org> 0.11-1mdv2009.0
+ Revision: 283281
- new version
- fix license
- update source URL
- fix build

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri May 02 2008 Funda Wang <fwang@mandriva.org> 0.10-1mdv2009.0
+ Revision: 200167
- New version 0.10

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 0.9-2mdv2008.1
+ Revision: 150228
- rebuild

  + Götz Waschk <waschk@mandriva.org>
    - fix dep on i18n package

* Sun Sep 02 2007 Götz Waschk <waschk@mandriva.org> 0.9-1mdv2008.0
+ Revision: 78327
- new version
- new major

* Wed Jul 25 2007 Funda Wang <fwang@mandriva.org> 0.8-1mdv2008.0
+ Revision: 55180
- fix rpmlint errors
- Fill up the file list
- Import goocanvas
- Created package structure for goocanvas.


%define major 2
%define libname %mklibname goocanvas %major
%define develname %mklibname -d goocanvas

Name: goocanvas
Version: 0.8
Release: %mkrel 1
Summary: New canvas widget for GTK+ that uses the cairo 2D library
Group: Developement/Other
License: GPL
URL: http://sourceforge.net/projects/goocanvas
Source: http://kent.dl.sourceforge.net/sourceforge/goocanvas/%{name}-%{version}.tar.gz
BuildRequires: gtk+2-devel

%description
GooCanvas is a new canvas widget for GTK+ that uses the cairo 2D library for 
drawing. It has a model/view split, and uses interfaces for canvas items and 
views, so you can easily turn any application object into canvas items.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

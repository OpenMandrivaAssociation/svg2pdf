%define git_clone_date 20100407

Name:		svg2pdf
Version:	0
Release:	1.%{git_clone_date}.1
Summary:	Simple SVG to PDF converter
Group:		Development/X11
License:	MIT
Url:		http://cgit.freedesktop.org/~cworth/svg2pdf/
Source0:	svg2pdf.c
Source1:	Makefile

BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(librsvg-2.0)

%description
svg2pdf is a very simple tool to convert SVG files to PDF using cairo.

%prep
%setup -q -c -T
cp %{SOURCE0} .
cp %{SOURCE1} .

%build
%make

%install
mkdir -p %{buildroot}/%{_bindir}
install svg2pdf %{buildroot}/%{_bindir}/svg2pdf

%files
%{_bindir}/svg2pdf


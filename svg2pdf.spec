%define git_clone_date 20100407

Name:		svg2pdf
Version:	0
Release:	%mkrel 1.%{git_clone_date}
Summary:	Simple SVG to PDF converter
Group:		Development/X11
Url:		http://cgit.freedesktop.org/~cworth/svg2pdf/
Source0:	svg2pdf.c
Source1:	Makefile
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires: libcairo-devel
BuildRequires: librsvg-devel

%description
svg2pdf is a very simple tool to convert SVG files to PDF using cairo.

%prep
%setup -q -c -T
cp %{SOURCE0} .
cp %{SOURCE1} .

%build
%make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
install svg2pdf %{buildroot}/%{_bindir}/svg2pdf

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/svg2pdf

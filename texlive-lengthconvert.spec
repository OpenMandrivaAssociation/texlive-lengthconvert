Name:		texlive-lengthconvert
Version:	55064
Release:	2
Summary:	Express lengths in arbitrary units
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lengthconvert
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lengthconvert.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lengthconvert.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lengthconvert.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a command to convert a length to any of a
large selection of units. The package relies on the LaTeX 3
programming environment.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/lengthconvert/lengthconvert.sty
%doc %{_texmfdistdir}/doc/latex/lengthconvert/lengthconvert.pdf
#- source
%doc %{_texmfdistdir}/source/latex/lengthconvert/lengthconvert.dtx
%doc %{_texmfdistdir}/source/latex/lengthconvert/lengthconvert.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

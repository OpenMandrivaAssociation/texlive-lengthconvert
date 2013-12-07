# revision 30867
# category Package
# catalog-ctan /macros/latex/contrib/lengthconvert
# catalog-date 2013-06-22 23:41:37 +0200
# catalog-license lppl1.3
# catalog-version 1.0a
Name:		texlive-lengthconvert
Version:	1.0a
Release:	7
Summary:	Express lengths in arbitrary units
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lengthconvert
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lengthconvert.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lengthconvert.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lengthconvert.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

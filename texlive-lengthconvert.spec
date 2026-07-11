%global tl_name lengthconvert
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0a
Release:	%{tl_revision}.1
Summary:	Express lengths in arbitrary units
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lengthconvert
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lengthconvert.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lengthconvert.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lengthconvert.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a command to convert a length to any of a large
selection of units. The package relies on the LaTeX3 programming
environment.


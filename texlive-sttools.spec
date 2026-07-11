%global tl_name sttools
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.5
Release:	%{tl_revision}.1
Summary:	Various macros
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/sttools
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sttools.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sttools.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sttools.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A collection of tools and macros, providing: miscellaneous float
control, page styles for floats, multipage tabulars, even columns at end
of twocolumn region, switching between one- and two-column anywhere,


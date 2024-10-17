Name:		texlive-sttools
Epoch:		1
Version:	60736
Release:	2
Summary:	Various macros
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/sttools
License:	COLLECTION
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sttools.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sttools.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sttools.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A collection of tools and macros, providing: miscellaneous
float control, page styles for floats, multipage tabulars, even
columns at end of twocolumn region, switching between one- and
two-column anywhere, getting more mileage from \marginpar,
simulating the effect of "midfloats", a package to manipulate
numerical lists and arrays.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sttools
%doc %{_texmfdistdir}/doc/latex/sttools
#- source
%doc %{_texmfdistdir}/source/latex/sttools

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

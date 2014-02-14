# revision 32659
# category Package
# catalog-ctan /macros/latex/contrib/sttools
# catalog-date 2014-01-13 12:46:43 +0100
# catalog-license collection
# catalog-version 1.2
Name:		texlive-sttools
Epoch:		1
Version:	1.2
Release:	1
Summary:	Various macros
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sttools
License:	COLLECTION
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sttools.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sttools.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sttools.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A collection of tools and macros, including: miscellaneous
float control, page styles for floats, multipage tabulars, even
columns at end of twocolumn region, switching between one- and
two-column anywhere, getting more mileage from \marginpar,
simulating the effect of "midfloats", create a bounding box, a
package to manipulate numerical lists and arrays.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sttools/boundbox.sty
%{_texmfdistdir}/tex/latex/sttools/cuted.sty
%{_texmfdistdir}/tex/latex/sttools/floatpag.sty
%{_texmfdistdir}/tex/latex/sttools/flushend.sty
%{_texmfdistdir}/tex/latex/sttools/marginal.sty
%{_texmfdistdir}/tex/latex/sttools/midfloat.sty
%{_texmfdistdir}/tex/latex/sttools/stabular.sty
%{_texmfdistdir}/tex/latex/sttools/stfloats.sty
%{_texmfdistdir}/tex/latex/sttools/texsort.sty
%doc %{_texmfdistdir}/doc/latex/sttools/README
%doc %{_texmfdistdir}/doc/latex/sttools/boundbox.pdf
%doc %{_texmfdistdir}/doc/latex/sttools/cuted.pdf
%doc %{_texmfdistdir}/doc/latex/sttools/floatpag.pdf
%doc %{_texmfdistdir}/doc/latex/sttools/flushend.pdf
%doc %{_texmfdistdir}/doc/latex/sttools/marginal.pdf
%doc %{_texmfdistdir}/doc/latex/sttools/midfloat.pdf
%doc %{_texmfdistdir}/doc/latex/sttools/stabular.pdf
%doc %{_texmfdistdir}/doc/latex/sttools/stfloats.pdf
%doc %{_texmfdistdir}/doc/latex/sttools/sttools.pdf
%doc %{_texmfdistdir}/doc/latex/sttools/texsort.pdf
#- source
%doc %{_texmfdistdir}/source/latex/sttools/boundbox.dtx
%doc %{_texmfdistdir}/source/latex/sttools/cuted.dtx
%doc %{_texmfdistdir}/source/latex/sttools/floatpag.dtx
%doc %{_texmfdistdir}/source/latex/sttools/flushend.dtx
%doc %{_texmfdistdir}/source/latex/sttools/marginal.dtx
%doc %{_texmfdistdir}/source/latex/sttools/midfloat.dtx
%doc %{_texmfdistdir}/source/latex/sttools/stabular.dtx
%doc %{_texmfdistdir}/source/latex/sttools/stfloats.dtx
%doc %{_texmfdistdir}/source/latex/sttools/sttools.dtx
%doc %{_texmfdistdir}/source/latex/sttools/sttools.ins
%doc %{_texmfdistdir}/source/latex/sttools/texsort.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

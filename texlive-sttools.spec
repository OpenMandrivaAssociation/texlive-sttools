# revision 26674
# category Package
# catalog-ctan /macros/latex/contrib/sttools
# catalog-date 2012-05-27 12:29:18 +0200
# catalog-license collection
# catalog-version undef
Name:		texlive-sttools
Version:	20120527
Release:	1
Summary:	Various macros
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sttools
License:	COLLECTION
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sttools.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sttools.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A collection of tools and macros, including: - a document
"Inside LaTeX2e kernel" (which discusses some of the functions
of the packages), - miscellaneous float control, - page styles
for floats, - multipage tabulars, - even columns at end of
twocolumn region, - switching between one- and two-column
anywhere, - getting more mileage from \marginpar, - simulating
the effect of "midfloats", - create a bounding box, - a package
to manipulate numerical lists and arrays.

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
%doc %{_texmfdistdir}/doc/latex/sttools/README.TEXLIVE
%doc %{_texmfdistdir}/doc/latex/sttools/doc/cuted.pdf
%doc %{_texmfdistdir}/doc/latex/sttools/doc/cuted.tex
%doc %{_texmfdistdir}/doc/latex/sttools/doc/floatpag.pdf
%doc %{_texmfdistdir}/doc/latex/sttools/doc/floatpag.tex
%doc %{_texmfdistdir}/doc/latex/sttools/doc/flushend.pdf
%doc %{_texmfdistdir}/doc/latex/sttools/doc/flushend.tex
%doc %{_texmfdistdir}/doc/latex/sttools/index.html

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}

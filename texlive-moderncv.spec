# revision 19688
# category Package
# catalog-ctan /macros/latex/contrib/moderncv
# catalog-date 2010-08-05 15:15:10 +0200
# catalog-license lppl1.3
# catalog-version 0.12
Name:		texlive-moderncv
Version:	0.12
Release:	1
Summary:	A modern curriculum vitae class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/moderncv
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/moderncv.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/moderncv.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Moderncv provides a documentclass for typesetting modern
curriculums vitae, both in a classic and in a casual style. It
is fairly customizable, allowing you to define your own style
by changing the colours, the fonts, etc.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/moderncv/moderncv.cls
%{_texmfdistdir}/tex/latex/moderncv/moderncvcompatibility.sty
%{_texmfdistdir}/tex/latex/moderncv/moderncvthemecasual.sty
%{_texmfdistdir}/tex/latex/moderncv/moderncvthemeclassic.sty
%{_texmfdistdir}/tex/latex/moderncv/moderncvthemeempty.sty
%{_texmfdistdir}/tex/latex/moderncv/tweaklist.sty
%doc %{_texmfdistdir}/doc/latex/moderncv/CHANGELOG
%doc %{_texmfdistdir}/doc/latex/moderncv/KNOWN_BUGS
%doc %{_texmfdistdir}/doc/latex/moderncv/README
%doc %{_texmfdistdir}/doc/latex/moderncv/examples/letter.pdf
%doc %{_texmfdistdir}/doc/latex/moderncv/examples/letter.tex
%doc %{_texmfdistdir}/doc/latex/moderncv/examples/picture.eps
%doc %{_texmfdistdir}/doc/latex/moderncv/examples/picture.jpg
%doc %{_texmfdistdir}/doc/latex/moderncv/examples/publications.bib
%doc %{_texmfdistdir}/doc/latex/moderncv/examples/template.pdf
%doc %{_texmfdistdir}/doc/latex/moderncv/examples/template.tex
%doc %{_texmfdistdir}/doc/latex/moderncv/examples/template_casual_orange.pdf
%doc %{_texmfdistdir}/doc/latex/moderncv/examples/template_classic_green.pdf
%doc %{_texmfdistdir}/doc/latex/moderncv/examples/template_multibib.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}

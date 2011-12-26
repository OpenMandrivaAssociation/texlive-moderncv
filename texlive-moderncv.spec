# revision 24929
# category Package
# catalog-ctan /macros/latex/contrib/moderncv
# catalog-date 2011-12-23 14:02:37 +0100
# catalog-license lppl1.3
# catalog-version 0.15.1
Name:		texlive-moderncv
Version:	0.15.1
Release:	1
Summary:	A modern curriculum vitae class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/moderncv
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/moderncv.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/moderncv.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Moderncv provides a documentclass for typesetting modern
curriculums vitae, both in a classic and in a casual style. It
is fairly customizable, allowing you to define your own style
by changing the colours, the fonts, etc.

%pre
    %{_sbindir}/texlive.post

%post
    %{_sbindir}/texlive.post

%preun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/moderncv/moderncv.cls
%{_texmfdistdir}/tex/latex/moderncv/moderncvcolorblack.sty
%{_texmfdistdir}/tex/latex/moderncv/moderncvcolorblue.sty
%{_texmfdistdir}/tex/latex/moderncv/moderncvcolorgreen.sty
%{_texmfdistdir}/tex/latex/moderncv/moderncvcolorgrey.sty
%{_texmfdistdir}/tex/latex/moderncv/moderncvcolororange.sty
%{_texmfdistdir}/tex/latex/moderncv/moderncvcolorpurple.sty
%{_texmfdistdir}/tex/latex/moderncv/moderncvcolorred.sty
%{_texmfdistdir}/tex/latex/moderncv/moderncvcompatibility.sty
%{_texmfdistdir}/tex/latex/moderncv/moderncvstylecasual.sty
%{_texmfdistdir}/tex/latex/moderncv/moderncvstyleclassic.sty
%{_texmfdistdir}/tex/latex/moderncv/moderncvstyleempty.sty
%{_texmfdistdir}/tex/latex/moderncv/moderncvstyleoldstyle.sty
%{_texmfdistdir}/tex/latex/moderncv/tweaklist.sty
%doc %{_texmfdistdir}/doc/latex/moderncv/CHANGELOG
%doc %{_texmfdistdir}/doc/latex/moderncv/KNOWN_BUGS
%doc %{_texmfdistdir}/doc/latex/moderncv/README
%doc %{_texmfdistdir}/doc/latex/moderncv/examples/letter.pdf
%doc %{_texmfdistdir}/doc/latex/moderncv/examples/letter.tex
%doc %{_texmfdistdir}/doc/latex/moderncv/examples/picture.eps
%doc %{_texmfdistdir}/doc/latex/moderncv/examples/picture.jpg
%doc %{_texmfdistdir}/doc/latex/moderncv/examples/publications.bib
%doc %{_texmfdistdir}/doc/latex/moderncv/examples/template-zh.pdf
%doc %{_texmfdistdir}/doc/latex/moderncv/examples/template-zh.tex
%doc %{_texmfdistdir}/doc/latex/moderncv/examples/template.pdf
%doc %{_texmfdistdir}/doc/latex/moderncv/examples/template.tex
%doc %{_texmfdistdir}/doc/latex/moderncv/examples/template_casual_orange.pdf
%doc %{_texmfdistdir}/doc/latex/moderncv/examples/template_classic_green.pdf
%doc %{_texmfdistdir}/doc/latex/moderncv/examples/template_multibib.pdf
%doc %{_texmfdistdir}/doc/latex/moderncv/examples/template_oldstyle_grey.pdf
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

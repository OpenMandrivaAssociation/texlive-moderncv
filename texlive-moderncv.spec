# revision 27250
# category Package
# catalog-ctan /macros/latex/contrib/moderncv
# catalog-date 2012-07-30 13:39:53 +0200
# catalog-license lppl1.3
# catalog-version 1.1.1
Name:		texlive-moderncv
Version:	1.1.1
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

%post
    %{_sbindir}/texlive.post

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
%{_texmfdistdir}/tex/latex/moderncv/moderncvstylebanking.sty
%{_texmfdistdir}/tex/latex/moderncv/moderncvstylecasual.sty
%{_texmfdistdir}/tex/latex/moderncv/moderncvstyleclassic.sty
%{_texmfdistdir}/tex/latex/moderncv/moderncvstyleempty.sty
%{_texmfdistdir}/tex/latex/moderncv/moderncvstyleoldstyle.sty
%{_texmfdistdir}/tex/latex/moderncv/tweaklist.sty
%doc %{_texmfdistdir}/doc/latex/moderncv/CHANGELOG
%doc %{_texmfdistdir}/doc/latex/moderncv/KNOWN_BUGS
%doc %{_texmfdistdir}/doc/latex/moderncv/README
%doc %{_texmfdistdir}/doc/latex/moderncv/examples/picture.eps
%doc %{_texmfdistdir}/doc/latex/moderncv/examples/picture.jpg
%doc %{_texmfdistdir}/doc/latex/moderncv/examples/publications.bib
%doc %{_texmfdistdir}/doc/latex/moderncv/examples/template-es.pdf
%doc %{_texmfdistdir}/doc/latex/moderncv/examples/template-es.tex
%doc %{_texmfdistdir}/doc/latex/moderncv/examples/template-zh.pdf
%doc %{_texmfdistdir}/doc/latex/moderncv/examples/template-zh.tex
%doc %{_texmfdistdir}/doc/latex/moderncv/examples/template.pdf
%doc %{_texmfdistdir}/doc/latex/moderncv/examples/template.tex
%doc %{_texmfdistdir}/doc/latex/moderncv/examples/template_banking_black.pdf
%doc %{_texmfdistdir}/doc/latex/moderncv/examples/template_banking_red.pdf
%doc %{_texmfdistdir}/doc/latex/moderncv/examples/template_casual_orange.pdf
%doc %{_texmfdistdir}/doc/latex/moderncv/examples/template_classic_green.pdf
%doc %{_texmfdistdir}/doc/latex/moderncv/examples/template_multibib.pdf
%doc %{_texmfdistdir}/doc/latex/moderncv/examples/template_oldstyle_grey.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Aug 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1.1-1
+ Revision: 812607
- Update to latest release.

* Tue Mar 27 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 787687
- Update to latest release.

* Wed Feb 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.19-1
+ Revision: 772124
- Update to latest release.

* Tue Jan 31 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.17-1
+ Revision: 770225
- Update to latest upstream package

* Thu Jan 19 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.16-1
+ Revision: 762669
- Update to latest upstream package

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.15.1-2
+ Revision: 754091
- Rebuild to reduce used resources

* Mon Dec 26 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.15.1-1
+ Revision: 745301
- texlive-moderncv

* Fri Dec 09 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.14-1
+ Revision: 739827
- texlive-moderncv

* Tue Nov 22 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.13.1-1
+ Revision: 732600
- texlive-moderncv

* Thu Nov 10 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.13-1
+ Revision: 729683
- texlive-moderncv

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.12-1
+ Revision: 719052
- texlive-moderncv
- texlive-moderncv
- texlive-moderncv
- texlive-moderncv


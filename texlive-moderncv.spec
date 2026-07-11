%global tl_name moderncv
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.6.1
Release:	%{tl_revision}.1
Summary:	A modern curriculum vitae class
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/moderncv
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/moderncv.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/moderncv.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(academicons)
Requires:	texlive(arydshln)
Requires:	texlive(colortbl)
Requires:	texlive(etoolbox)
Requires:	texlive(fancyhdr)
Requires:	texlive(fontawesome5)
Requires:	texlive(graphics)
Requires:	texlive(hyperref)
Requires:	texlive(iftex)
Requires:	texlive(l3packages)
Requires:	texlive(microtype)
Requires:	texlive(multirow)
Requires:	texlive(tools)
Requires:	texlive(url)
Requires:	texlive(xcolor)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class provides facilities for typesetting modern curriculums vitae,
both in a classic and in a casual style. It is fairly customizable,
allowing you to define your own style by changing the colours, the
fonts, etc. The template.tex file can be used as an example.


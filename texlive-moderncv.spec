Name:		texlive-moderncv
Version:	2.0.0
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
The class provides facilities for typesetting modern
curriculums vitae, both in a classic and in a casual style. It
is fairly customizable, allowing you to define your own style
by changing the colours, the fonts, etc. A number of templates
are provided in the distribution examples subdirectory.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/moderncv
%doc %{_texmfdistdir}/doc/latex/moderncv

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}

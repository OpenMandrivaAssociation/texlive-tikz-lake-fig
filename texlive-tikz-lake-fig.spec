Name:		texlive-tikz-lake-fig
Version:	55288
Release:	2
Summary:	Schematic diagrams of lakes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tikz-lake-fig
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-lake-fig.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-lake-fig.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package contains a collection of schematic diagrams of
lakes for use in LaTeX documents. Diagrams include
representations of material budgets, fluxes, and connectivity
arrangements.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/tikz-lake-fig
%doc %{_texmfdistdir}/doc/latex/tikz-lake-fig

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

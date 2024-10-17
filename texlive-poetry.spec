Name:		texlive-poetry
Version:	53129
Release:	2
Summary:	Facilities for typesetting poetry and poetical structure
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/poetry
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/poetry.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/poetry.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/poetry.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides some macros and general doodads for
typesetting poetry. There is, of course, already the excellent
verse package, and the poetrytex package provides some extra
functionality on top of it. But poetry provides much of the
same functionality in a bit of a different way, and with a few
additional abilities, such as facilities for a list of poems,
an index of first lines, and some structural commands.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/poetry
%{_texmfdistdir}/tex/latex/poetry
%doc %{_texmfdistdir}/doc/latex/poetry

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

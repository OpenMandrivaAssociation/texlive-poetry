%global tl_name poetry
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.2
Release:	%{tl_revision}.1
Summary:	Facilities for typesetting poetry and poetical structure
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/poetry
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/poetry.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/poetry.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/poetry.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides some macros and general doodads for typesetting
poetry. There is, of course, already the excellent verse package, and
the poetrytex package provides some extra functionality on top of it.
But poetry provides much of the same functionality in a bit of a
different way, and with a few additional abilities, such as facilities
for a list of poems, an index of first lines, and some structural
commands.


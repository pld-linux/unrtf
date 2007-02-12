Summary:	UnRTF - converter from RTF to other formats
Summary(pl.UTF-8):	UnRTF - konwerter z RTF do innych formatów
Name:		unrtf
Version:	0.19.7
Release:	1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/unrtf/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	1cddb206f3ff5451c8d7699acba26a77
URL:		http://www.gnu.org/software/unrtf/unrtf.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The program unrtf is a converter from Rich Text Format (RTF) to a
growing number of document formats. At present it supports HyperText
Markup Language (HTML), plain text, text with VT100 codes, and LaTeX.
All output formats except HTML are "alpha" i.e. limited and
development has just begun. However with HTML, the program supports
tables, fonts, hyperlinks, and paragraph alignment. Font support
includes face and size changes, as well as typical attributes such as
italic, bold, underlining, strikethrough, smallcaps, allcaps, expand,
compress and both foreground and background colors. Images are always
stored to separate files in the current directory, or they can be
ignored.

%description -l pl.UTF-8
Program unrtf to konwerter z formatu RTF (Rich Text Format) do coraz
większej liczby formatów dokumentów. Aktualnie obsługiwane są
HyperText Markup Language (HTML), czysty tekst, tekst z kodami VT100
oraz LaTeX. Wszystkie formaty wyjściowe z wyjątkiem HTML-a są w stanie
"alpha", czyli ograniczone i ich obsługa dopiero zaczęła być tworzona.
Jednak przy użyciu HTML-a program obsługuje tabele, fonty, odnośniki i
wyrównania paragrafów. Obsługa fontów obejmuje zmiany kroju i
rozmiaru, a także typowe atrybuty, takie jak kursywa, pogrubienie,
podkreślenie, przekreślenie i kolor tła. Obrazki są zapisywane w
oddzielnych plikach w bieżącym katalogu, albo mogą być ignorowane.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT

install -D unrtf $RPM_BUILD_ROOT%{_bindir}/unrtf
install -D unrtf.1 $RPM_BUILD_ROOT%{_mandir}/man1/unrtf.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/unrtf
%{_mandir}/man1/unrtf.1*

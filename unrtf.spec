Summary:	UnRTF - converter from RTF to other formats
Summary(pl):	UnRTF - konwerter z RTF do innych formatów
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

%description -l pl
Program unrtf to konwerter z formatu RTF (Rich Text Format) do coraz
wiêkszej liczby formatów dokumentów. Aktualnie obs³ugiwane s±
HyperText Markup Language (HTML), czysty tekst, tekst z kodami VT100
oraz LaTeX. Wszystkie formaty wyj¶ciowe z wyj±tkiem HTML-a s± w stanie
"alpha", czyli ograniczone i ich obs³uga dopiero zaczê³a byæ tworzona.
Jednak przy u¿yciu HTML-a program obs³uguje tabele, fonty, odno¶niki i
wyrównania paragrafów. Obs³uga fontów obejmuje zmiany kroju i
rozmiaru, a tak¿e typowe atrybuty, takie jak kursywa, pogrubienie,
podkre¶lenie, przekre¶lenie i kolor t³a. Obrazki s± zapisywane w
oddzielnych plikach w bie¿±cym katalogu, albo mog± byæ ignorowane.

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

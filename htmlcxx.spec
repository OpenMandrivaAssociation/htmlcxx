%define		css_major 0
%define		css_minor 0
%define		major 3
%define		minor 1

%define		libname %mklibname %{name} %{major}
%define		devel %mklibname -d %{name}
%define		cssdev %mklibname cssparser %{css_major}
%define		csslib %mklibname -d cssparser

Name:		htmlcxx
Version:	0.87
Release:	1
Summary:	htmlcxx is a simple non-validating css1 and html parser for C++
Group:		Development/Other 
License:	LGPLv2
URL:		http://htmlcxx.sourceforge.net/
Source0:	https://sourceforge.net/projects/htmlcxx/files/v%{version}/%{name}-%{version}.tar.gz
Patch0:		htmlcxx-0.86-linking.patch

%description
htmlcxx is a simple non-validating css1 and html parser for C++.
Although there are several other html parsers available, htmlcxx has some
characteristics that make it unique: - STL like navigation of DOM tree,
using excelent's tree.hh library from Kasper Peeters.

- It is possible to reproduce exactly, character by character, the original
  document from the parse tree
- Bundled css parser
- Optional parsing of attributes
- C++ code that looks like C++ (not so true anymore)
- Offsets of tags/elements in the original document are stored in the nodes
  of the DOM tree

%package -n	%{devel}
Summary:	Development files
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}
Conflicts:	%{libname} < 0.8.6-4

%description -n	%{devel}
Development files

%package -n	%{libname}
Summary:	These are the main libraries
Group:		Development/Other 
Conflicts:	%{devel} < 0.8.6-4

%description -n	%{libname}
The main libraries

%package -n	%{cssdev}
Summary:	These are the css_parser development files
Group:		Development/Other 
Conflicts:	%{devel} < 0.8.6-4

%description -n	%{cssdev}
Development files for libcss_*

%package -n	%{csslib}
Summary:	These are the css_parser libraries
Group:		System/Libraries

%description -n	%{csslib}
Libraries containing the libcss_* files

%prep
%autosetup -p1

%build
autoreconf -vfi
%configure
%make_build

%install
%make_install

# Delete static libraries
find %{buildroot} -name *.*a -delete

%files
%{_bindir}/%{name}

%files -n	%{libname}
%{_libdir}/libhtmlcxx.so.%{major}{,.*}

%files -n	%{devel}
%{_includedir}/%{name}/html/
%{_libdir}/libhtmlcxx.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n	%{cssdev}
%{_includedir}/%{name}/css/
%{_datadir}/%{name}/
%{_libdir}/libcss_parser.so
%{_libdir}/libcss_parser_pp.so

%files -n	%{csslib}
%{_libdir}/libcss_parser.so.%{css_major}{,.*}
%{_libdir}/libcss_parser_pp.so.%{css_major}{,.*}

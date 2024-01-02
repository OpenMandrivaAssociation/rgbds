Name:		rgbds
Version:	0.7.0
Release:	1
Summary:	A development package for the Game Boy, including an assembler

# See LICENSE for details
License:	DWPL and ISC and MIT and BSD
URL:		https://github.com/gbdev/%{name}
Source0:	https://github.com/gbdev/rgbds/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	byacc
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	pkgconfig(libpng)

%description
RGBDS (Rednex Game Boy Development System) is a free assembler/linker package
for the Game Boy and Game Boy Color.

It consists of:

* rgbasm (assembler)
* rgblink (linker)
* rgbfix (checksum/header fixer)
* rgbgfx (PNG‐to‐2bpp graphics converter)

%prep
%autosetup -p1

%build
%cmake
%make_build

%install
%make_install -C build

rm -f %{buildroot}/build/BUILD/rgbds-%{version}/test/gfx/randtilegen
rm -f %{buildroot}/build/BUILD/rgbds-%{version}/test/gfx/rgbgfx_test

%files
%{_bindir}/rgbasm
%{_bindir}/rgblink
%{_bindir}/rgbfix
%{_bindir}/rgbgfx
%{_mandir}/man1/rgbasm.1.*
%{_mandir}/man1/rgblink.1.*
%{_mandir}/man1/rgbfix.1.*
%{_mandir}/man1/rgbgfx.1.*
%{_mandir}/man5/rgbds.5.*
%{_mandir}/man5/rgbasm.5.*
%{_mandir}/man5/rgblink.5.*
%{_mandir}/man7/rgbds.7.*
%{_mandir}/man7/gbz80.7.*
%license LICENSE
%doc README.rst

%exclude /builddir/build/BUILD/rgbds-0.6.1/test/gfx/randtilegen
%exclude /builddir/build/BUILD/rgbds-0.6.1/test/gfx/rgbgfx_test

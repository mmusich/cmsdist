### RPM external libbsd 0.11.5
Source: https://libbsd.freedesktop.org/releases/%{n}-%{realversion}.tar.xz

Requires: libmd

%define drop_files %{i}/share %{i}/lib/pkgconfig

%prep
%setup -n %{n}-%{realversion}

%build
# Update to detect aarch64 and ppc64le
rm -f ./conftools/config.{sub,guess}
%get_config_sub ./conftools/config.sub
%get_config_guess ./conftools/config.guess
chmod +x ./conftools/config.{sub,guess}

./configure --prefix=%{i}
make %{makeprocesses}

%install
make install
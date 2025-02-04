|Dependency|Before|After|Explicit|Environments|
|-|-|-|-|-|
|pip|23.3.2|24.0|true|*all envs* on {linux-64, osx-64, win-64}<br/>{lint, pl014, pl015, pl016, pl017, pl018, pl019, pl020, py310, py311, py312, py39} on osx-arm64|
|pip|23.3.1|24.0|true|default on osx-arm64|
|pytest-cov|4.1.0|5.0.0|true|{default, pl014, pl015, pl016, pl017, pl018, pl019, pl020, py310, py311, py312, py39} on *all platforms*|
|hatchling|1.21.1|1.24.2|true|*all*|
|hypothesis|6.97.4|6.103.2|true|{pl014, pl015, pl016, pl017, pl018, pl019, pl020, py310, py311, py312, py39} on {linux-64, osx-64, win-64}<br/>default on *all platforms*|
|hypothesis|6.97.1|6.103.2|true|{pl017, pl018, pl019, pl020, py310, py311, py312, py39} on osx-arm64|
|hypothesis|6.97.2|6.103.2|true|{pl014, pl015, pl016} on osx-arm64|
|pre-commit|3.6.0|3.7.1|true|lint on *all platforms*|
|pytest|8.0.0|8.2.2|true|{default, pl014, pl015, pl016, pl017, pl018, pl019, pl020, py310, py311, py312, py39} on *all platforms*|
|polars|0.20.6|0.20.31|true|{lint, py310, py311, py312, py39} on *all platforms*<br/>default on {linux-64, osx-64, win-64}<br/>pl020 on win-64|
|polars|0.20.16|0.20.31|true|pl020 on {linux-64, osx-64, osx-arm64}|
|polars|0.20.3|0.20.31|true|default on osx-arm64|
|python|3.9.18|3.9.19|true|py39 on *all platforms*|
|python|3.12.1|3.12.3|true|{lint, py312} on *all platforms*<br/>default on {linux-64, osx-64, win-64}|
|python|3.12.0|3.12.3|true|default on osx-arm64|
|python|3.11.7|3.11.9|true|py311 on *all platforms*|
|python|3.10.13|3.10.14|true|py310 on *all platforms*|
|typing_extensions|4.9.0||false|{default, lint, py311, py312} on win-64|
|ca-certificates|2023.11.17|2024.6.2|false|*all*|
|libcxx|16.0.6|17.0.6|false|*all envs* on {osx-64, osx-arm64}|
|llvm-openmp|17.0.6|18.1.7|false|*all envs* on osx-64<br/>{lint, pl014, pl015, pl016, pl017, pl018, pl019, pl020, py310, py311, py312, py39} on osx-arm64|
|llvm-openmp|17.0.5|18.1.7|false|default on osx-arm64|
|packaging|23.2|24.1|false|*all*|
|setuptools|69.0.3|70.0.0|false|*all envs* on {linux-64, osx-64, win-64}<br/>{lint, pl014, pl015, pl016, pl017, pl018, pl019, pl020, py310, py311, py312, py39} on osx-arm64|
|setuptools|68.2.2|70.0.0|false|default on osx-arm64|
|tzdata|2023d|2024a|false|*all envs* on {linux-64, osx-64, win-64}<br/>{lint, pl014, pl015, pl016, pl017, pl018, pl019, pl020, py310, py311, py312, py39} on osx-arm64|
|tzdata|2023c|2024a|false|default on osx-arm64|
|coverage|7.4.4|7.5.3|false|{default, pl014, pl015, pl016, pl017, pl018, pl019, pl020, py310, py311, py312, py39} on *all platforms*|
|filelock|3.13.1|3.15.1|false|lint on *all platforms*|
|importlib-metadata|7.0.1|7.1.0|false|*all*|
|intel-openmp|2024.0.0|2024.1.0|false|*all envs* on win-64|
|libexpat|2.5.0|2.6.2|false|{default, lint, py311, py312} on *all platforms*|
|libhwloc|2.9.3|2.10.0|false|*all envs* on win-64|
|libsqlite|3.45.2|3.46.0|false|{pl014, pl015, pl016, pl017, pl018, pl019, pl020} on *all platforms*|
|libsqlite|3.44.2|3.46.0|false|{default, lint, py310, py311, py312, py39} on *all platforms*|
|libzlib|1.2.13|1.3.1|false|*all*|
|mkl|2024.0.0|2024.1.0|false|*all envs* on win-64|
|ncurses|6.4.20240210|6.5|false|{pl014, pl015, pl016, pl017, pl018, pl019, pl020} on {linux-64, osx-64, osx-arm64}|
|ncurses|6.4|6.5|false|{default, lint, py310, py311, py312, py39} on {linux-64, osx-64, osx-arm64}|
|nodeenv|1.8.0|1.9.1|false|lint on *all platforms*|
|openssl|3.2.1|3.3.1|false|*all envs* on {linux-64, osx-64, win-64}<br/>{lint, pl014, pl015, pl016, pl017, pl018, pl019, pl020} on osx-arm64|
|openssl|3.2.0|3.3.1|false|{default, py310, py311, py312, py39} on osx-arm64|
|pluggy|1.4.0|1.5.0|false|*all*|
|pycparser|2.21|2.22|false|lint on *all platforms*|
|tbb|2021.11.0|2021.12.0|false|*all envs* on win-64|
|trove-classifiers|2024.1.8|2024.5.22|false|*all*|
|typing_extensions|4.9.0|4.12.2|false|{pl016, pl017, pl018, pl020, py310, py39} on *all platforms*<br/>pl019 on {linux-64, osx-64, osx-arm64}|
|vc14_runtime|14.38.33130|14.40.33810|false|*all envs* on win-64|
|virtualenv|20.25.0|20.26.2|false|lint on *all platforms*|
|vs2015_runtime|14.38.33130|14.40.33810|false|*all envs* on win-64|
|wheel|0.42.0|0.43.0|false|*all envs* on {linux-64, osx-64, win-64}<br/>{lint, pl014, pl015, pl016, pl017, pl018, pl019, pl020, py310, py311, py312, py39} on osx-arm64|
|wheel|0.41.3|0.43.0|false|default on osx-arm64|
|zipp|3.17.0|3.19.2|false|*all*|
|identify|2.5.33|2.5.36|false|lint on *all platforms*|
|libopenblas|0.3.26|0.3.27|false|*all envs* on {linux-64, osx-64}<br/>{lint, pl014, pl015, pl016, pl017, pl018, pl019, pl020, py310, py311, py312, py39} on osx-arm64|
|libopenblas|0.3.25|0.3.27|false|default on osx-arm64|
|libxml2|2.12.4|2.12.7|false|*all envs* on win-64|
|numpy|1.26.3|1.26.4|false|{lint, py310, py311, py312, py39} on *all platforms*<br/>default on {linux-64, osx-64, win-64}|
|numpy|1.26.2|1.26.4|false|default on osx-arm64|
|platformdirs|4.2.0|4.2.2|false|lint on *all platforms*|
|ld_impl_linux-64|h41732ed_0|hf3520f5_4|false|*all envs* on linux-64|
|libblas|21_win64_mkl|22_win64_mkl|false|*all envs* on win-64|
|libblas|21_osxarm64_openblas|22_osxarm64_openblas|false|{lint, pl014, pl015, pl016, pl017, pl018, pl019, pl020, py310, py311, py312, py39} on osx-arm64|
|libblas|20_osxarm64_openblas|22_osxarm64_openblas|false|default on osx-arm64|
|libblas|21_osx64_openblas|22_osx64_openblas|false|*all envs* on osx-64|
|libblas|21_linux64_openblas|22_linux64_openblas|false|*all envs* on linux-64|
|libcblas|21_win64_mkl|22_win64_mkl|false|*all envs* on win-64|
|libcblas|21_osxarm64_openblas|22_osxarm64_openblas|false|{lint, pl014, pl015, pl016, pl017, pl018, pl019, pl020, py310, py311, py312, py39} on osx-arm64|
|libcblas|20_osxarm64_openblas|22_osxarm64_openblas|false|default on osx-arm64|
|libcblas|21_osx64_openblas|22_osx64_openblas|false|*all envs* on osx-64|
|libcblas|21_linux64_openblas|22_linux64_openblas|false|*all envs* on linux-64|
|libgcc-ng|h807b86a_4|h77fa898_9|false|*all envs* on linux-64|
|libgfortran|13_2_0_hd922786_2|13_2_0_hd922786_3|false|{lint, pl014, pl015, pl016, pl017, pl018, pl019, pl020, py310, py311, py312, py39} on osx-arm64|
|libgfortran|13_2_0_hd922786_1|13_2_0_hd922786_3|false|default on osx-arm64|
|libgfortran|13_2_0_h97931a8_2|13_2_0_h97931a8_3|false|*all envs* on osx-64|
|libgfortran-ng|h69a702a_4|h69a702a_9|false|*all envs* on linux-64|
|libgfortran5|hf226fd6_2|hf226fd6_3|false|{lint, pl014, pl015, pl016, pl017, pl018, pl019, pl020, py310, py311, py312, py39} on osx-arm64|
|libgfortran5|hf226fd6_1|hf226fd6_3|false|default on osx-arm64|
|libgfortran5|ha4646dd_4|h3d2ce59_9|false|*all envs* on linux-64|
|libgfortran5|h2873a65_2|h2873a65_3|false|*all envs* on osx-64|
|libgomp|h807b86a_4|h77fa898_9|false|*all envs* on linux-64|
|liblapack|21_win64_mkl|22_win64_mkl|false|*all envs* on win-64|
|liblapack|21_osxarm64_openblas|22_osxarm64_openblas|false|{lint, pl014, pl015, pl016, pl017, pl018, pl019, pl020, py310, py311, py312, py39} on osx-arm64|
|liblapack|20_osxarm64_openblas|22_osxarm64_openblas|false|default on osx-arm64|
|liblapack|21_osx64_openblas|22_osx64_openblas|false|*all envs* on osx-64|
|liblapack|21_linux64_openblas|22_linux64_openblas|false|*all envs* on linux-64|
|libstdcxx-ng|h7e041cc_4|hc0a3c3a_9|false|*all envs* on linux-64|
|vc|hcf57466_18|h8a93ad2_20|false|*all envs* on win-64|

[^1]: **Bold** means explicit dependency.
[^2]: Dependency got downgraded.

# Dependencies

<details>
<summary>Explicit dependencies</summary>

|Dependency[^1]|Before|After|Environments|
|-|-|-|-|
|**pip**|23.3.2|24.0|*all envs* on {linux-64, osx-64, win-64}<br/>{lint, pl014, pl015, pl016, pl017, pl018, pl019, pl020, py310, py311, py312, py39} on osx-arm64|
|**pip**|23.3.1|24.0|default on osx-arm64|
|**pytest-cov**|4.1.0|5.0.0|{default, pl014, pl015, pl016, pl017, pl018, pl019, pl020, py310, py311, py312, py39} on *all platforms*|
|**hatchling**|1.21.1|1.24.2|*all*|
|**hypothesis**|6.97.4|6.103.2|{pl014, pl015, pl016, pl017, pl018, pl019, pl020, py310, py311, py312, py39} on {linux-64, osx-64, win-64}<br/>default on *all platforms*|
|**hypothesis**|6.97.1|6.103.2|{pl017, pl018, pl019, pl020, py310, py311, py312, py39} on osx-arm64|
|**hypothesis**|6.97.2|6.103.2|{pl014, pl015, pl016} on osx-arm64|
|**pre-commit**|3.6.0|3.7.1|lint on *all platforms*|
|**pytest**|8.0.0|8.2.2|{default, pl014, pl015, pl016, pl017, pl018, pl019, pl020, py310, py311, py312, py39} on *all platforms*|
|**polars**|0.20.6|0.20.31|{lint, py310, py311, py312, py39} on *all platforms*<br/>default on {linux-64, osx-64, win-64}<br/>pl020 on win-64|
|**polars**|0.20.16|0.20.31|pl020 on {linux-64, osx-64, osx-arm64}|
|**polars**|0.20.3|0.20.31|default on osx-arm64|
|**python**|3.9.18|3.9.19|py39 on *all platforms*|
|**python**|3.12.1|3.12.3|{lint, py312} on *all platforms*<br/>default on {linux-64, osx-64, win-64}|
|**python**|3.12.0|3.12.3|default on osx-arm64|
|**python**|3.11.7|3.11.9|py311 on *all platforms*|
|**python**|3.10.13|3.10.14|py310 on *all platforms*|

</details>

<details>
<summary>Implicit dependencies</summary>

|Dependency[^1]|Before|After|Environments|
|-|-|-|-|
|typing_extensions|4.9.0||{default, lint, py311, py312} on win-64|
|ca-certificates|2023.11.17|2024.6.2|*all*|
|libcxx|16.0.6|17.0.6|*all envs* on {osx-64, osx-arm64}|
|llvm-openmp|17.0.6|18.1.7|*all envs* on osx-64<br/>{lint, pl014, pl015, pl016, pl017, pl018, pl019, pl020, py310, py311, py312, py39} on osx-arm64|
|llvm-openmp|17.0.5|18.1.7|default on osx-arm64|
|packaging|23.2|24.1|*all*|
|setuptools|69.0.3|70.0.0|*all envs* on {linux-64, osx-64, win-64}<br/>{lint, pl014, pl015, pl016, pl017, pl018, pl019, pl020, py310, py311, py312, py39} on osx-arm64|
|setuptools|68.2.2|70.0.0|default on osx-arm64|
|tzdata|2023d|2024a|*all envs* on {linux-64, osx-64, win-64}<br/>{lint, pl014, pl015, pl016, pl017, pl018, pl019, pl020, py310, py311, py312, py39} on osx-arm64|
|tzdata|2023c|2024a|default on osx-arm64|
|coverage|7.4.4|7.5.3|{default, pl014, pl015, pl016, pl017, pl018, pl019, pl020, py310, py311, py312, py39} on *all platforms*|
|filelock|3.13.1|3.15.1|lint on *all platforms*|
|importlib-metadata|7.0.1|7.1.0|*all*|
|intel-openmp|2024.0.0|2024.1.0|*all envs* on win-64|
|libexpat|2.5.0|2.6.2|{default, lint, py311, py312} on *all platforms*|
|libhwloc|2.9.3|2.10.0|*all envs* on win-64|
|libsqlite|3.45.2|3.46.0|{pl014, pl015, pl016, pl017, pl018, pl019, pl020} on *all platforms*|
|libsqlite|3.44.2|3.46.0|{default, lint, py310, py311, py312, py39} on *all platforms*|
|libzlib|1.2.13|1.3.1|*all*|
|mkl|2024.0.0|2024.1.0|*all envs* on win-64|
|ncurses|6.4.20240210|6.5|{pl014, pl015, pl016, pl017, pl018, pl019, pl020} on {linux-64, osx-64, osx-arm64}|
|ncurses|6.4|6.5|{default, lint, py310, py311, py312, py39} on {linux-64, osx-64, osx-arm64}|
|nodeenv|1.8.0|1.9.1|lint on *all platforms*|
|openssl|3.2.1|3.3.1|*all envs* on {linux-64, osx-64, win-64}<br/>{lint, pl014, pl015, pl016, pl017, pl018, pl019, pl020} on osx-arm64|
|openssl|3.2.0|3.3.1|{default, py310, py311, py312, py39} on osx-arm64|
|pluggy|1.4.0|1.5.0|*all*|
|pycparser|2.21|2.22|lint on *all platforms*|
|tbb|2021.11.0|2021.12.0|*all envs* on win-64|
|trove-classifiers|2024.1.8|2024.5.22|*all*|
|typing_extensions|4.9.0|4.12.2|{pl016, pl017, pl018, pl020, py310, py39} on *all platforms*<br/>pl019 on {linux-64, osx-64, osx-arm64}|
|vc14_runtime|14.38.33130|14.40.33810|*all envs* on win-64|
|virtualenv|20.25.0|20.26.2|lint on *all platforms*|
|vs2015_runtime|14.38.33130|14.40.33810|*all envs* on win-64|
|wheel|0.42.0|0.43.0|*all envs* on {linux-64, osx-64, win-64}<br/>{lint, pl014, pl015, pl016, pl017, pl018, pl019, pl020, py310, py311, py312, py39} on osx-arm64|
|wheel|0.41.3|0.43.0|default on osx-arm64|
|zipp|3.17.0|3.19.2|*all*|
|identify|2.5.33|2.5.36|lint on *all platforms*|
|libopenblas|0.3.26|0.3.27|*all envs* on {linux-64, osx-64}<br/>{lint, pl014, pl015, pl016, pl017, pl018, pl019, pl020, py310, py311, py312, py39} on osx-arm64|
|libopenblas|0.3.25|0.3.27|default on osx-arm64|
|libxml2|2.12.4|2.12.7|*all envs* on win-64|
|numpy|1.26.3|1.26.4|{lint, py310, py311, py312, py39} on *all platforms*<br/>default on {linux-64, osx-64, win-64}|
|numpy|1.26.2|1.26.4|default on osx-arm64|
|platformdirs|4.2.0|4.2.2|lint on *all platforms*|
|ld_impl_linux-64|h41732ed_0|hf3520f5_4|*all envs* on linux-64|
|libblas|21_win64_mkl|22_win64_mkl|*all envs* on win-64|
|libblas|21_osxarm64_openblas|22_osxarm64_openblas|{lint, pl014, pl015, pl016, pl017, pl018, pl019, pl020, py310, py311, py312, py39} on osx-arm64|
|libblas|20_osxarm64_openblas|22_osxarm64_openblas|default on osx-arm64|
|libblas|21_osx64_openblas|22_osx64_openblas|*all envs* on osx-64|
|libblas|21_linux64_openblas|22_linux64_openblas|*all envs* on linux-64|
|libcblas|21_win64_mkl|22_win64_mkl|*all envs* on win-64|
|libcblas|21_osxarm64_openblas|22_osxarm64_openblas|{lint, pl014, pl015, pl016, pl017, pl018, pl019, pl020, py310, py311, py312, py39} on osx-arm64|
|libcblas|20_osxarm64_openblas|22_osxarm64_openblas|default on osx-arm64|
|libcblas|21_osx64_openblas|22_osx64_openblas|*all envs* on osx-64|
|libcblas|21_linux64_openblas|22_linux64_openblas|*all envs* on linux-64|
|libgcc-ng|h807b86a_4|h77fa898_9|*all envs* on linux-64|
|libgfortran|13_2_0_hd922786_2|13_2_0_hd922786_3|{lint, pl014, pl015, pl016, pl017, pl018, pl019, pl020, py310, py311, py312, py39} on osx-arm64|
|libgfortran|13_2_0_hd922786_1|13_2_0_hd922786_3|default on osx-arm64|
|libgfortran|13_2_0_h97931a8_2|13_2_0_h97931a8_3|*all envs* on osx-64|
|libgfortran-ng|h69a702a_4|h69a702a_9|*all envs* on linux-64|
|libgfortran5|hf226fd6_2|hf226fd6_3|{lint, pl014, pl015, pl016, pl017, pl018, pl019, pl020, py310, py311, py312, py39} on osx-arm64|
|libgfortran5|hf226fd6_1|hf226fd6_3|default on osx-arm64|
|libgfortran5|ha4646dd_4|h3d2ce59_9|*all envs* on linux-64|
|libgfortran5|h2873a65_2|h2873a65_3|*all envs* on osx-64|
|libgomp|h807b86a_4|h77fa898_9|*all envs* on linux-64|
|liblapack|21_win64_mkl|22_win64_mkl|*all envs* on win-64|
|liblapack|21_osxarm64_openblas|22_osxarm64_openblas|{lint, pl014, pl015, pl016, pl017, pl018, pl019, pl020, py310, py311, py312, py39} on osx-arm64|
|liblapack|20_osxarm64_openblas|22_osxarm64_openblas|default on osx-arm64|
|liblapack|21_osx64_openblas|22_osx64_openblas|*all envs* on osx-64|
|liblapack|21_linux64_openblas|22_linux64_openblas|*all envs* on linux-64|
|libstdcxx-ng|h7e041cc_4|hc0a3c3a_9|*all envs* on linux-64|
|vc|hcf57466_18|h8a93ad2_20|*all envs* on win-64|

</details>

[^1]: **Bold** means explicit dependency.
[^2]: Dependency got downgraded.

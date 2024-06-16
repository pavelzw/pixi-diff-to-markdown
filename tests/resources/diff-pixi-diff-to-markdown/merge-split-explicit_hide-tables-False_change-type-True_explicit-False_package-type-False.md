# Explicit dependencies

|Dependency[^1]|Before|After|Change|Environments|
|-|-|-|-|-|
|**typos**|1.21.0|1.22.7|Minor Upgrade|lint on *all platforms*|
|**ordered_enum**|0.0.8|0.0.9|Patch Upgrade|{build, default, py312} on *all platforms*|
|**pydantic**|2.7.1|2.7.4|Patch Upgrade|{build, default, py312} on *all platforms*|
|**pytest**|8.2.1|8.2.2|Patch Upgrade|{default, py312} on *all platforms*|
|**ruff**|0.4.4|0.4.9|Patch Upgrade|lint on *all platforms*|
|**py-rattler**|py312h1a1520d_0|py312had01cb0_0|Only build string|{default, py312} on osx-arm64|

# Implicit dependencies

|Dependency[^1]|Before|After|Change|Environments|
|-|-|-|-|-|
|ca-certificates|2024.2.2|2024.6.2|Minor Upgrade|*all*|
|certifi|2024.2.2|2024.6.2|Minor Upgrade|build on *all platforms*|
|filelock|3.14.0|3.15.1|Minor Upgrade|lint on *all platforms*|
|libsqlite|3.45.3|3.46.0|Minor Upgrade|*all*|
|libzlib|1.2.13|1.3.1|Minor Upgrade|*all*|
|more-itertools|10.2.0|10.3.0|Minor Upgrade|build on *all platforms*|
|nodeenv|1.8.0|1.9.1|Minor Upgrade|lint on *all platforms*|
|packaging|24.0|24.1|Minor Upgrade|{build, default, py312} on *all platforms*|
|pkginfo|1.10.0|1.11.1|Minor Upgrade|build on *all platforms*|
|typing-extensions|4.11.0|4.12.2|Minor Upgrade|{build, default, py312} on *all platforms*|
|typing_extensions|4.11.0|4.12.2|Minor Upgrade|{build, default, py312} on *all platforms*|
|vc14_runtime|14.38.33135|14.40.33810|Minor Upgrade|*all envs* on win-64|
|vs2015_runtime|14.38.33135|14.40.33810|Minor Upgrade|*all envs* on win-64|
|zipp|3.17.0|3.19.2|Minor Upgrade|{build, default, py312} on *all platforms*|
|cryptography|42.0.7|42.0.8|Patch Upgrade|build on linux-64|
|openssl|3.3.0|3.3.1|Patch Upgrade|*all*|
|pydantic-core|2.18.2|2.18.4|Patch Upgrade|{build, default, py312} on *all platforms*|
|requests|2.32.2|2.32.3|Patch Upgrade|build on *all platforms*|
|ld_impl_linux-64|hf3520f5_1|hf3520f5_4|Only build string|*all envs* on linux-64|
|libgcc-ng|h77fa898_7|h77fa898_9|Only build string|*all envs* on linux-64|
|libgomp|h77fa898_7|h77fa898_9|Only build string|*all envs* on linux-64|
|libstdcxx-ng|hc0a3c3a_7|hc0a3c3a_9|Only build string|{build, lint} on linux-64|
|vc|ha32ba9b_20|h8a93ad2_20|Only build string|*all envs* on win-64|

[^1]: **Bold** means explicit dependency.
[^2]: Dependency got downgraded.

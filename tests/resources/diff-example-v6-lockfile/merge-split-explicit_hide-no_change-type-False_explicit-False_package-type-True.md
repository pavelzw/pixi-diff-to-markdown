# Explicit dependencies

|Dependency[^1]|Before|After|Package|Environments|
|-|-|-|-|-|
|[**setuptools**](https://pypi.org/project/setuptools)|74.1.3|75.6.0|pypi|*all envs* on osx-arm64|
|[**polars**](https://prefix.dev/channels/conda-forge/packages/polars)|1.15.0|1.16.0|conda|*all envs* on osx-arm64|
|**pkg**|0.23.0|0.23.0|conda|*all envs* on linux-64|
|[**private-package**](https://prefix.dev/channels/setup-pixi-test/packages/private-package)|0.0.1|0.0.1|conda|*all envs* on osx-arm64|
|**my-package**|py313hc743ca1_0|py313hc743ca1_1|conda|*all envs* on osx-arm64|

# Implicit dependencies

|Dependency[^1]|Before|After|Package|Environments|
|-|-|-|-|-|
|microsoft_python_type_stubs|none|none|pypi|*all envs* on linux-64|

[^1]: **Bold** means explicit dependency.
[^2]: Dependency got downgraded.

# Explicit dependencies

|Dependency[^1]|Before|After|Environments|
|-|-|-|-|
|[**setuptools**](https://pypi.org/project/setuptools)|74.1.3|75.6.0|*all envs* on osx-arm64|
|[**polars**](https://prefix.dev/channels/conda-forge/packages/polars)|1.15.0|1.16.0|*all envs* on osx-arm64|
|**pkg**|0.23.0|0.23.0|*all envs* on linux-64|
|[**private-package**](https://prefix.dev/channels/setup-pixi-test/packages/private-package)|0.0.1|0.0.1|*all envs* on osx-arm64|
|**my-package**|py313hc743ca1_0|py313hc743ca1_1|*all envs* on osx-arm64|

# Implicit dependencies

|Dependency[^1]|Before|After|Environments|
|-|-|-|-|
|microsoft_python_type_stubs|none|none|*all envs* on linux-64|

[^1]: **Bold** means explicit dependency.
[^2]: Dependency got downgraded.

# default

## osx-arm64

|Dependency|Before|After|Change|Explicit|Package|
|-|-|-|-|-|-|
|[setuptools](https://pypi.org/project/setuptools)|74.1.3|75.6.0|Major Upgrade|true|pypi|
|[polars](https://prefix.dev/channels/conda-forge/packages/polars)|1.15.0|1.16.0|Minor Upgrade|true|conda|
|[private-package](https://prefix.dev/channels/setup-pixi-test/packages/private-package)|0.0.1|0.0.1|Other|true|conda|
|my-package|py313hc743ca1_0|py313hc743ca1_1|Only build string|true|conda|

## linux-64

|Dependency|Before|After|Change|Explicit|Package|
|-|-|-|-|-|-|
|pkg|0.23.0|0.23.0|Other|true|conda|
|microsoft_python_type_stubs|none|none|Other|false|pypi|

[^1]: **Bold** means explicit dependency.
[^2]: Dependency got downgraded.

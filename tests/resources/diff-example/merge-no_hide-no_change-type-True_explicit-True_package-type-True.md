# default

## linux-64

|Dependency|Before|After|Change|Explicit|Package|
|-|-|-|-|-|-|
|new-package||0.10.1|Added|true|conda|
|removed-package|0.10.1||Removed|true|pypi|
|bpy|0.10.1|2.10.1|Major Upgrade|true|pypi|
|polars|herads_0|herads_1|Only build string|true|conda|
|python|0.10.0|0.10.1|Patch Upgrade|false|conda|

## osx-arm64

|Dependency|Before|After|Change|Explicit|Package|
|-|-|-|-|-|-|
|polars[^2]|0.10.0|0.9.1|Minor Downgrade|true|conda|
|python|0.10.0|0.10.1|Patch Upgrade|true|conda|

# lint

## linux-64

|Dependency|Before|After|Change|Explicit|Package|
|-|-|-|-|-|-|
|polars|0.10.0|0.10.1|Patch Upgrade|true|conda|
|python|0.10.0|0.10.1|Patch Upgrade|false|conda|

[^1]: **Bold** means explicit dependency.
[^2]: Dependency got downgraded.

# default

## linux-64

|Dependency|Before|After|Change|Explicit|
|-|-|-|-|-|
|new-package||0.10.1|Added|true|
|removed-package|0.10.1||Removed|true|
|bpy|0.10.1|2.10.1|Major Upgrade|true|
|polars|herads_0|herads_1|Only build string|true|
|python|0.10.0|0.10.1|Patch Upgrade|false|

## osx-arm64

|Dependency|Before|After|Change|Explicit|
|-|-|-|-|-|
|polars[^2]|0.10.0|0.9.1|Minor Downgrade|true|
|python|0.10.0|0.10.1|Patch Upgrade|true|

# lint

## linux-64

|Dependency|Before|After|Change|Explicit|
|-|-|-|-|-|
|polars|0.10.0|0.10.1|Patch Upgrade|true|
|python|0.10.0|0.10.1|Patch Upgrade|false|

[^1]: **Bold** means explicit dependency.
[^2]: Dependency got downgraded.

# default

## linux-64

|Dependency[^1]|Before|After|Package|
|-|-|-|-|
|**new-package**||0.10.1|conda|
|**removed-package**|0.10.1||pypi|
|**bpy**|0.10.1|2.10.1|pypi|
|**polars**|herads_0|herads_1|conda|
|python|0.10.0|0.10.1|conda|

## osx-arm64

|Dependency[^1]|Before|After|Package|
|-|-|-|-|
|**polars**[^2]|0.10.0|0.9.1|conda|
|**python**|0.10.0|0.10.1|conda|

# lint

## linux-64

|Dependency[^1]|Before|After|Package|
|-|-|-|-|
|**polars**|0.10.0|0.10.1|conda|
|python|0.10.0|0.10.1|conda|

[^1]: **Bold** means explicit dependency.
[^2]: Dependency got downgraded.

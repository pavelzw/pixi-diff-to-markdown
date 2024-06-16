# Explicit dependencies

|Dependency[^1]|Before|After|Environments|
|-|-|-|-|
|**new-package**||0.10.1|default on linux-64|
|**removed-package**|0.10.1||default on linux-64|
|**bpy**|0.10.1|2.10.1|default on linux-64|
|**polars**[^2]|0.10.0|0.9.1|default on osx-arm64|
|**polars**|0.10.0|0.10.1|lint on linux-64|
|**python**|0.10.0|0.10.1|default on osx-arm64|
|**polars**|herads_0|herads_1|default on linux-64|

# Implicit dependencies

|Dependency[^1]|Before|After|Environments|
|-|-|-|-|
|python|0.10.0|0.10.1|*all envs* on linux-64|

[^1]: **Bold** means explicit dependency.
[^2]: Dependency got downgraded.

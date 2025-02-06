# Explicit dependencies

|Dependency[^1]|Before|After|Change|Environments|
|-|-|-|-|-|
|**new-package**||0.10.1|Added|default on linux-64|
|**removed-package**|0.10.1||Removed|default on linux-64|
|**bpy**|0.10.1|2.10.1|Major Upgrade|default on linux-64|
|**polars**[^2]|0.10.0|0.9.1|Minor Downgrade|default on osx-arm64|
|**polars**|0.10.0|0.10.1|Patch Upgrade|lint on linux-64|
|**python**|0.10.0|0.10.1|Patch Upgrade|default on osx-arm64|
|**polars**|herads_0|herads_1|Only build string|default on linux-64|

# Implicit dependencies

|Dependency[^1]|Before|After|Change|Environments|
|-|-|-|-|-|
|python|0.10.0|0.10.1|Patch Upgrade|*all envs* on linux-64|

[^1]: **Bold** means explicit dependency.
[^2]: Dependency got downgraded.

|Dependency|Before|After|Change|Explicit|Environments|
|-|-|-|-|-|-|
|new-package||0.10.1|Added|true|default on linux-64|
|removed-package|0.10.1||Removed|true|default on linux-64|
|bpy|0.10.1|2.10.1|Major Upgrade|true|default on linux-64|
|polars[^2]|0.10.0|0.9.1|Minor Downgrade|true|default on osx-arm64|
|polars|0.10.0|0.10.1|Patch Upgrade|true|lint on linux-64|
|python|0.10.0|0.10.1|Patch Upgrade|true|default on osx-arm64|
|polars|herads_0|herads_1|Only build string|true|default on linux-64|
|python|0.10.0|0.10.1|Patch Upgrade|false|*all envs* on linux-64|

[^1]: **Bold** means explicit dependency.
[^2]: Dependency got downgraded.

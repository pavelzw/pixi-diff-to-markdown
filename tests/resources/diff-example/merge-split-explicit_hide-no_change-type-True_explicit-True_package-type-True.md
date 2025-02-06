# Explicit dependencies

|Dependency|Before|After|Change|Explicit|Package|Environments|
|-|-|-|-|-|-|-|
|new-package||0.10.1|Added|true|conda|default on linux-64|
|removed-package|0.10.1||Removed|true|pypi|default on linux-64|
|bpy|0.10.1|2.10.1|Major Upgrade|true|pypi|default on linux-64|
|polars[^2]|0.10.0|0.9.1|Minor Downgrade|true|conda|default on osx-arm64|
|polars|0.10.0|0.10.1|Patch Upgrade|true|conda|lint on linux-64|
|python|0.10.0|0.10.1|Patch Upgrade|true|conda|default on osx-arm64|
|polars|herads_0|herads_1|Only build string|true|conda|default on linux-64|

# Implicit dependencies

|Dependency|Before|After|Change|Explicit|Package|Environments|
|-|-|-|-|-|-|-|
|python|0.10.0|0.10.1|Patch Upgrade|false|conda|*all envs* on linux-64|

[^1]: **Bold** means explicit dependency.
[^2]: Dependency got downgraded.

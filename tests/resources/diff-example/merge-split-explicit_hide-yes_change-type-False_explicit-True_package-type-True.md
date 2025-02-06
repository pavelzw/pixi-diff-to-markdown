# Dependencies

<details open>
<summary>Explicit dependencies</summary>

|Dependency|Before|After|Explicit|Package|Environments|
|-|-|-|-|-|-|
|new-package||0.10.1|true|conda|default on linux-64|
|removed-package|0.10.1||true|pypi|default on linux-64|
|bpy|0.10.1|2.10.1|true|pypi|default on linux-64|
|polars[^2]|0.10.0|0.9.1|true|conda|default on osx-arm64|
|polars|0.10.0|0.10.1|true|conda|lint on linux-64|
|python|0.10.0|0.10.1|true|conda|default on osx-arm64|
|polars|herads_0|herads_1|true|conda|default on linux-64|

</details>

<details open>
<summary>Implicit dependencies</summary>

|Dependency|Before|After|Explicit|Package|Environments|
|-|-|-|-|-|-|
|python|0.10.0|0.10.1|false|conda|*all envs* on linux-64|

</details>

[^1]: **Bold** means explicit dependency.
[^2]: Dependency got downgraded.

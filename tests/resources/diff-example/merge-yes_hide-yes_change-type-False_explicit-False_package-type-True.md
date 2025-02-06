<details open>
<summary>Dependencies</summary>

|Dependency[^1]|Before|After|Package|Environments|
|-|-|-|-|-|
|**new-package**||0.10.1|conda|default on linux-64|
|**removed-package**|0.10.1||pypi|default on linux-64|
|**bpy**|0.10.1|2.10.1|pypi|default on linux-64|
|**polars**[^2]|0.10.0|0.9.1|conda|default on osx-arm64|
|**polars**|0.10.0|0.10.1|conda|lint on linux-64|
|**python**|0.10.0|0.10.1|conda|default on osx-arm64|
|**polars**|herads_0|herads_1|conda|default on linux-64|
|python|0.10.0|0.10.1|conda|*all envs* on linux-64|

</details>

[^1]: **Bold** means explicit dependency.
[^2]: Dependency got downgraded.

# default

<details open>
<summary>linux-64</summary>

|Dependency[^1]|Before|After|Change|
|-|-|-|-|
|**new-package**||0.10.1|Added|
|**removed-package**|0.10.1||Removed|
|**bpy**|0.10.1|2.10.1|Major Upgrade|
|**polars**|herads_0|herads_1|Only build string|
|python|0.10.0|0.10.1|Patch Upgrade|

</details>

<details open>
<summary>osx-arm64</summary>

|Dependency[^1]|Before|After|Change|
|-|-|-|-|
|**polars**[^2]|0.10.0|0.9.1|Minor Downgrade|
|**python**|0.10.0|0.10.1|Patch Upgrade|

</details>

# lint

<details open>
<summary>linux-64</summary>

|Dependency[^1]|Before|After|Change|
|-|-|-|-|
|**polars**|0.10.0|0.10.1|Patch Upgrade|
|python|0.10.0|0.10.1|Patch Upgrade|

</details>

[^1]: **Bold** means explicit dependency.
[^2]: Dependency got downgraded.

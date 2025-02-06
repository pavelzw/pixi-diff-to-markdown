# default

<details open>
<summary>linux-64</summary>

|Dependency|Before|After|Change|Explicit|
|-|-|-|-|-|
|new-package||0.10.1|Added|true|
|removed-package|0.10.1||Removed|true|
|bpy|0.10.1|2.10.1|Major Upgrade|true|
|polars|herads_0|herads_1|Only build string|true|
|python|0.10.0|0.10.1|Patch Upgrade|false|

</details>

<details open>
<summary>osx-arm64</summary>

|Dependency|Before|After|Change|Explicit|
|-|-|-|-|-|
|polars[^2]|0.10.0|0.9.1|Minor Downgrade|true|
|python|0.10.0|0.10.1|Patch Upgrade|true|

</details>

# lint

<details open>
<summary>linux-64</summary>

|Dependency|Before|After|Change|Explicit|
|-|-|-|-|-|
|polars|0.10.0|0.10.1|Patch Upgrade|true|
|python|0.10.0|0.10.1|Patch Upgrade|false|

</details>

[^1]: **Bold** means explicit dependency.
[^2]: Dependency got downgraded.

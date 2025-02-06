# default

<details open>
<summary>linux-64</summary>

|Dependency|Before|After|Explicit|
|-|-|-|-|
|new-package||0.10.1|true|
|removed-package|0.10.1||true|
|bpy|0.10.1|2.10.1|true|
|polars|herads_0|herads_1|true|
|python|0.10.0|0.10.1|false|

</details>

<details open>
<summary>osx-arm64</summary>

|Dependency|Before|After|Explicit|
|-|-|-|-|
|polars[^2]|0.10.0|0.9.1|true|
|python|0.10.0|0.10.1|true|

</details>

# lint

<details open>
<summary>linux-64</summary>

|Dependency|Before|After|Explicit|
|-|-|-|-|
|polars|0.10.0|0.10.1|true|
|python|0.10.0|0.10.1|false|

</details>

[^1]: **Bold** means explicit dependency.
[^2]: Dependency got downgraded.

# default

<details open>
<summary>linux-64</summary>

|Dependency|Before|After|Explicit|Package|
|-|-|-|-|-|
|new-package||0.10.1|true|conda|
|removed-package|0.10.1||true|pypi|
|bpy|0.10.1|2.10.1|true|pypi|
|polars|herads_0|herads_1|true|conda|
|python|0.10.0|0.10.1|false|conda|

</details>

<details open>
<summary>osx-arm64</summary>

|Dependency|Before|After|Explicit|Package|
|-|-|-|-|-|
|polars[^2]|0.10.0|0.9.1|true|conda|
|python|0.10.0|0.10.1|true|conda|

</details>

# lint

<details open>
<summary>linux-64</summary>

|Dependency|Before|After|Explicit|Package|
|-|-|-|-|-|
|polars|0.10.0|0.10.1|true|conda|
|python|0.10.0|0.10.1|false|conda|

</details>

[^1]: **Bold** means explicit dependency.
[^2]: Dependency got downgraded.

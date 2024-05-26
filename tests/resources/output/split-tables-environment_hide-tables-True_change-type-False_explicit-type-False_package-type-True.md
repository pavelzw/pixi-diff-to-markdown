<details>
<summary>default</summary>

| Platform | Dependency[^1] | Before | After | Package |
| -: | - | - | - | - |
| linux-64 | *new-package* |  | 0.10.1 | conda |
|| *removed-package* | 0.10.1 |  | pypi |
|| *bpy* | 0.10.1 | 2.10.1 | pypi |
|| python | 0.10.0 | 0.10.1 | conda |
|| *polars* | herads_0 | herads_1 | conda |
| osx-arm64 | *polars*[^2] | 0.10.0 | 0.9.1 | conda |
|| *python* | 0.10.0 | 0.10.1 | conda |

</details>

<details>
<summary>lint</summary>

| Platform | Dependency[^1] | Before | After | Package |
| -: | - | - | - | - |
| linux-64 | *polars* | 0.10.0 | 0.10.1 | conda |
|| python | 0.10.0 | 0.10.1 | conda |

</details>

[^1]: *Cursive* means explicit dependency.
[^2]: Dependency got downgraded.

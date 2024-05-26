<details>
<summary>default</summary>

| Platform | Dependency | Before | After | Explicit |
| -: | - | - | - | - |
| linux-64 | new-package |  | 0.10.1 | true |
|| removed-package | 0.10.1 |  | true |
|| bpy | 0.10.1 | 2.10.1 | true |
|| python | 0.10.0 | 0.10.1 | false |
|| polars | herads_0 | herads_1 | true |
| osx-arm64 | polars[^2] | 0.10.0 | 0.9.1 | true |
|| python | 0.10.0 | 0.10.1 | true |

</details>

<details>
<summary>lint</summary>

| Platform | Dependency | Before | After | Explicit |
| -: | - | - | - | - |
| linux-64 | polars | 0.10.0 | 0.10.1 | true |
|| python | 0.10.0 | 0.10.1 | false |

</details>

[^1]: *Cursive* means explicit dependency.
[^2]: Dependency got downgraded.

<details>
<summary>default</summary>

| Platform | Dependency | Before | After | Explicit | Package |
| -: | - | - | - | - | - |
| linux-64 | new-package |  | 0.10.1 | true | conda |
|| removed-package | 0.10.1 |  | true | conda |
|| python | 0.10.0 | 0.10.0 | false | conda |
|| polars | herads_0 | herads_0 | true | conda |
| osx-arm64 | polars[^2] | 0.10.0 | 0.10.0 | true | conda |
|| python | 0.10.0 | 0.10.0 | true | conda |

</details>

<details>
<summary>lint</summary>

| Platform | Dependency | Before | After | Explicit | Package |
| -: | - | - | - | - | - |
| linux-64 | polars | 0.10.0 | 0.10.0 | true | conda |
|| python | 0.10.0 | 0.10.0 | false | conda |

</details>

[^1]: *Cursive* means explicit dependency.
[^2]: Dependency got downgraded.

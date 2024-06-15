<details>
<summary>default</summary>

| Platform | Dependency | Before | After | Change | Explicit | Package |
| -: | - | - | - | - | - | - |
| linux-64 | new-package |  | 0.10.1 | Added | true | conda |
|| removed-package | 0.10.1 |  | Removed | true | pypi |
|| bpy | 0.10.1 | 2.10.1 | Major Upgrade | true | pypi |
|| python | 0.10.0 | 0.10.1 | Patch Upgrade | false | conda |
|| polars | herads_0 | herads_1 | Only build string | true | conda |
| osx-arm64 | polars[^2] | 0.10.0 | 0.9.1 | Minor Downgrade | true | conda |
|| python | 0.10.0 | 0.10.1 | Patch Upgrade | true | conda |

</details>

<details>
<summary>lint</summary>

| Platform | Dependency | Before | After | Change | Explicit | Package |
| -: | - | - | - | - | - | - |
| linux-64 | polars | 0.10.0 | 0.10.1 | Patch Upgrade | true | conda |
|| python | 0.10.0 | 0.10.1 | Patch Upgrade | false | conda |

</details>

[^1]: *Cursive* means explicit dependency.
[^2]: Dependency got downgraded.
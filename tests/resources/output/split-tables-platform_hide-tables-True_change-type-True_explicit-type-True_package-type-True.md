# default

<details>
<summary>linux-64</summary>

| Dependency | Before | After | Change | Explicit | Package |
| - | - | - | - | - | - |
| new-package |  | 0.10.1 | Added | true | conda |
| removed-package | 0.10.1 |  | Removed | true | conda |
| python | 0.10.0 | 0.10.0 | Patch Upgrade | false | conda |
| polars | herads_0 | herads_0 | Only build string | true | conda |

</details>

<details>
<summary>osx-arm64</summary>

| Dependency | Before | After | Change | Explicit | Package |
| - | - | - | - | - | - |
| polars[^2] | 0.10.0 | 0.10.0 | Minor Downgrade | true | conda |
| python | 0.10.0 | 0.10.0 | Patch Upgrade | true | conda |

</details>

# lint

<details>
<summary>linux-64</summary>

| Dependency | Before | After | Change | Explicit | Package |
| - | - | - | - | - | - |
| polars | 0.10.0 | 0.10.0 | Patch Upgrade | true | conda |
| python | 0.10.0 | 0.10.0 | Patch Upgrade | false | conda |

</details>

[^1]: *Cursive* means explicit dependency.
[^2]: Dependency got downgraded.

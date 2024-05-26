# default

<details>
<summary>linux-64</summary>

| Dependency | Before | After | Change | Explicit | Package |
| - | - | - | - | - | - |
| python | 0.10.0 | 0.10.1 | Patch Upgrade | false | conda |
| polars | herads_0 | herads_1 | Only build string | true | conda |

</details>

<details>
<summary>osx-arm64</summary>

| Dependency | Before | After | Change | Explicit | Package |
| - | - | - | - | - | - |
| polars[^2] | 0.10.0 | 0.9.1 | Minor Downgrade | true | conda |
| python | 0.10.0 | 0.10.1 | Patch Upgrade | true | conda |

</details>

# lint

<details>
<summary>linux-64</summary>

| Dependency | Before | After | Change | Explicit | Package |
| - | - | - | - | - | - |
| polars | 0.10.0 | 0.10.1 | Patch Upgrade | true | conda |
| python | 0.10.0 | 0.10.1 | Patch Upgrade | false | conda |

</details>

[^1]: *Cursive* means explicit dependency.
[^2]: Dependency got downgraded.

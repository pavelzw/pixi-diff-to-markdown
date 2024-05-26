# default

<details>
<summary>linux-64</summary>

| Dependency | Before | After | Change | Explicit |
| - | - | - | - | - |
| new-package |  | 0.10.1 | Added | true |
| removed-package | 0.10.1 |  | Removed | true |
| python | 0.10.0 | 0.10.0 | Patch Upgrade | false |
| polars | herads_0 | herads_0 | Only build string | true |

</details>

<details>
<summary>osx-arm64</summary>

| Dependency | Before | After | Change | Explicit |
| - | - | - | - | - |
| polars[^2] | 0.10.0 | 0.10.0 | Minor Downgrade | true |
| python | 0.10.0 | 0.10.0 | Patch Upgrade | true |

</details>

# lint

<details>
<summary>linux-64</summary>

| Dependency | Before | After | Change | Explicit |
| - | - | - | - | - |
| polars | 0.10.0 | 0.10.0 | Patch Upgrade | true |
| python | 0.10.0 | 0.10.0 | Patch Upgrade | false |

</details>

[^1]: *Cursive* means explicit dependency.
[^2]: Dependency got downgraded.

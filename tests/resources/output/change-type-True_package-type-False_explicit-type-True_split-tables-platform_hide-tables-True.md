# default

<details>
<summary>linux-64</summary>

| Dependency | Before | After | Change | Explicit |
| - | - | - | - | - |
| python | 0.10.0 | 0.10.1 | Patch Upgrade | false |
| polars | herads_0 | herads_1 | Only build string | true |

</details>

<details>
<summary>osx-arm64</summary>

| Dependency | Before | After | Change | Explicit |
| - | - | - | - | - |
| polars[^2] | 0.10.0 | 0.9.1 | Minor Downgrade | true |
| python | 0.10.0 | 0.10.1 | Patch Upgrade | true |

</details>

# lint

<details>
<summary>linux-64</summary>

| Dependency | Before | After | Change | Explicit |
| - | - | - | - | - |
| polars | 0.10.0 | 0.10.1 | Patch Upgrade | true |
| python | 0.10.0 | 0.10.1 | Patch Upgrade | false |

</details>

[^1]: *Cursive* means explicit dependency.
[^2]: Dependency got downgraded.

# default

<details>
<summary>linux-64</summary>

| Dependency | Before | After | Explicit |
| - | - | - | - |
| new-package |  | 0.10.1 | true |
| removed-package | 0.10.1 |  | true |
| python | 0.10.0 | 0.10.0 | false |
| polars | herads_0 | herads_0 | true |

</details>

<details>
<summary>osx-arm64</summary>

| Dependency | Before | After | Explicit |
| - | - | - | - |
| polars[^2] | 0.10.0 | 0.10.0 | true |
| python | 0.10.0 | 0.10.0 | true |

</details>

# lint

<details>
<summary>linux-64</summary>

| Dependency | Before | After | Explicit |
| - | - | - | - |
| polars | 0.10.0 | 0.10.0 | true |
| python | 0.10.0 | 0.10.0 | false |

</details>

[^1]: *Cursive* means explicit dependency.
[^2]: Dependency got downgraded.

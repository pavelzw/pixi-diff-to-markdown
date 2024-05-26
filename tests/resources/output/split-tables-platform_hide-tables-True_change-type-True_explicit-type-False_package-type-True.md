# default

<details>
<summary>linux-64</summary>

| Dependency[^1] | Before | After | Change | Package |
| - | - | - | - | - |
| *new-package* |  | 0.10.1 | Added | conda |
| *removed-package* | 0.10.1 |  | Removed | conda |
| python | 0.10.0 | 0.10.0 | Patch Upgrade | conda |
| *polars* | herads_0 | herads_0 | Only build string | conda |

</details>

<details>
<summary>osx-arm64</summary>

| Dependency[^1] | Before | After | Change | Package |
| - | - | - | - | - |
| *polars*[^2] | 0.10.0 | 0.10.0 | Minor Downgrade | conda |
| *python* | 0.10.0 | 0.10.0 | Patch Upgrade | conda |

</details>

# lint

<details>
<summary>linux-64</summary>

| Dependency[^1] | Before | After | Change | Package |
| - | - | - | - | - |
| *polars* | 0.10.0 | 0.10.0 | Patch Upgrade | conda |
| python | 0.10.0 | 0.10.0 | Patch Upgrade | conda |

</details>

[^1]: *Cursive* means explicit dependency.
[^2]: Dependency got downgraded.

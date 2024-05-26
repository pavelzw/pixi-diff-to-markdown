# default

<details>
<summary>linux-64</summary>

| Dependency[^1] | Before | After | Change |
| - | - | - | - |
| *new-package* |  | 0.10.1 | Added |
| *removed-package* | 0.10.1 |  | Removed |
| python | 0.10.0 | 0.10.0 | Patch Upgrade |
| *polars* | herads_0 | herads_0 | Only build string |

</details>

<details>
<summary>osx-arm64</summary>

| Dependency[^1] | Before | After | Change |
| - | - | - | - |
| *polars*[^2] | 0.10.0 | 0.10.0 | Minor Downgrade |
| *python* | 0.10.0 | 0.10.0 | Patch Upgrade |

</details>

# lint

<details>
<summary>linux-64</summary>

| Dependency[^1] | Before | After | Change |
| - | - | - | - |
| *polars* | 0.10.0 | 0.10.0 | Patch Upgrade |
| python | 0.10.0 | 0.10.0 | Patch Upgrade |

</details>

[^1]: *Cursive* means explicit dependency.
[^2]: Dependency got downgraded.

# default

<details>
<summary>linux-64</summary>

| Dependency[^1] | Before | After | Change | Package |
| - | - | - | - | - |
| *new-package* |  | 0.10.1 | Added | conda |
| *removed-package* | 0.10.1 |  | Removed | pypi |
| *bpy* | 0.10.1 | 2.10.1 | Major Upgrade | pypi |
| python | 0.10.0 | 0.10.1 | Patch Upgrade | conda |
| *polars* | herads_0 | herads_1 | Only build string | conda |

</details>

<details>
<summary>osx-arm64</summary>

| Dependency[^1] | Before | After | Change | Package |
| - | - | - | - | - |
| *polars*[^2] | 0.10.0 | 0.9.1 | Minor Downgrade | conda |
| *python* | 0.10.0 | 0.10.1 | Patch Upgrade | conda |

</details>

# lint

<details>
<summary>linux-64</summary>

| Dependency[^1] | Before | After | Change | Package |
| - | - | - | - | - |
| *polars* | 0.10.0 | 0.10.1 | Patch Upgrade | conda |
| python | 0.10.0 | 0.10.1 | Patch Upgrade | conda |

</details>

[^1]: *Cursive* means explicit dependency.
[^2]: Dependency got downgraded.

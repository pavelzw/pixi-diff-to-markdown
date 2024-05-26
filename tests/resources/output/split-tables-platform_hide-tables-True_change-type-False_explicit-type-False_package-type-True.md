# default

<details>
<summary>linux-64</summary>

| Dependency[^1] | Before | After | Package |
| - | - | - | - |
| *new-package* |  | 0.10.1 | conda |
| *removed-package* | 0.10.1 |  | pypi |
| *bpy* | 0.10.1 | 2.10.1 | pypi |
| python | 0.10.0 | 0.10.1 | conda |
| *polars* | herads_0 | herads_1 | conda |

</details>

<details>
<summary>osx-arm64</summary>

| Dependency[^1] | Before | After | Package |
| - | - | - | - |
| *polars*[^2] | 0.10.0 | 0.9.1 | conda |
| *python* | 0.10.0 | 0.10.1 | conda |

</details>

# lint

<details>
<summary>linux-64</summary>

| Dependency[^1] | Before | After | Package |
| - | - | - | - |
| *polars* | 0.10.0 | 0.10.1 | conda |
| python | 0.10.0 | 0.10.1 | conda |

</details>

[^1]: *Cursive* means explicit dependency.
[^2]: Dependency got downgraded.

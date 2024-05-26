<details>
<summary>default</summary>

| Platform | Dependency[^1] | Before | After |
| -: | - | - | - |
| linux-64 | *new-package* |  | 0.10.1 |
|| *removed-package* | 0.10.1 |  |
|| python | 0.10.0 | 0.10.0 |
|| *polars* | herads_0 | herads_0 |
| osx-arm64 | *polars*[^2] | 0.10.0 | 0.10.0 |
|| *python* | 0.10.0 | 0.10.0 |

</details>

<details>
<summary>lint</summary>

| Platform | Dependency[^1] | Before | After |
| -: | - | - | - |
| linux-64 | *polars* | 0.10.0 | 0.10.0 |
|| python | 0.10.0 | 0.10.0 |

</details>

[^1]: *Cursive* means explicit dependency.
[^2]: Dependency got downgraded.

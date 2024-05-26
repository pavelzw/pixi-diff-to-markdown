## default

| Platform | Dependency[^1] | Before | After |
| -: | - | - | - |
| linux-64 | *new-package* |  | 0.10.1 |
|| *removed-package* | 0.10.1 |  |
|| *bpy* | 0.10.1 | 2.10.1 |
|| python | 0.10.0 | 0.10.1 |
|| *polars* | herads_0 | herads_1 |
| osx-arm64 | *polars*[^2] | 0.10.0 | 0.9.1 |
|| *python* | 0.10.0 | 0.10.1 |

## lint

| Platform | Dependency[^1] | Before | After |
| -: | - | - | - |
| linux-64 | *polars* | 0.10.0 | 0.10.1 |
|| python | 0.10.0 | 0.10.1 |

[^1]: *Cursive* means explicit dependency.
[^2]: Dependency got downgraded.

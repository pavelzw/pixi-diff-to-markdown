# default

## linux-64

| Dependency[^1] | Before | After | Change |
| - | - | - | - |
| *new-package* |  | 0.10.1 | Added |
| *removed-package* | 0.10.1 |  | Removed |
| *bpy* | 0.10.1 | 2.10.1 | Major Upgrade |
| python | 0.10.0 | 0.10.1 | Patch Upgrade |
| *polars* | herads_0 | herads_1 | Only build string |

## osx-arm64

| Dependency[^1] | Before | After | Change |
| - | - | - | - |
| *polars*[^2] | 0.10.0 | 0.9.1 | Minor Downgrade |
| *python* | 0.10.0 | 0.10.1 | Patch Upgrade |

# lint

## linux-64

| Dependency[^1] | Before | After | Change |
| - | - | - | - |
| *polars* | 0.10.0 | 0.10.1 | Patch Upgrade |
| python | 0.10.0 | 0.10.1 | Patch Upgrade |

[^1]: *Cursive* means explicit dependency.
[^2]: Dependency got downgraded.

# default

## linux-64

| Dependency[^1] | Before | After | Change | Package |
| - | - | - | - | - |
| *new-package* |  | 0.10.1 | Added | conda |
| *removed-package* | 0.10.1 |  | Removed | conda |
| python | 0.10.0 | 0.10.0 | Patch Upgrade | conda |
| *polars* | herads_0 | herads_0 | Only build string | conda |

## osx-arm64

| Dependency[^1] | Before | After | Change | Package |
| - | - | - | - | - |
| *polars*[^2] | 0.10.0 | 0.10.0 | Minor Downgrade | conda |
| *python* | 0.10.0 | 0.10.0 | Patch Upgrade | conda |

# lint

## linux-64

| Dependency[^1] | Before | After | Change | Package |
| - | - | - | - | - |
| *polars* | 0.10.0 | 0.10.0 | Patch Upgrade | conda |
| python | 0.10.0 | 0.10.0 | Patch Upgrade | conda |

[^1]: *Cursive* means explicit dependency.
[^2]: Dependency got downgraded.

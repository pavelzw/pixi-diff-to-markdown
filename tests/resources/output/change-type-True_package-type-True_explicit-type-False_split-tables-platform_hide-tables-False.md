# default

## linux-64

| Dependency[^1] | Before | After | Change | Package |
| - | - | - | - | - |
| python | 0.10.0 | 0.10.1 | Patch Upgrade | conda |
| *polars* | herads_0 | herads_1 | Only build string | conda |

## osx-arm64

| Dependency[^1] | Before | After | Change | Package |
| - | - | - | - | - |
| *polars*[^2] | 0.10.0 | 0.9.1 | Minor Downgrade | conda |
| *python* | 0.10.0 | 0.10.1 | Patch Upgrade | conda |

# lint

## linux-64

| Dependency[^1] | Before | After | Change | Package |
| - | - | - | - | - |
| *polars* | 0.10.0 | 0.10.1 | Patch Upgrade | conda |
| python | 0.10.0 | 0.10.1 | Patch Upgrade | conda |

[^1]: *Cursive* means explicit dependency.
[^2]: Dependency got downgraded.

# default

## linux-64

| Dependency | Before | After | Change | Explicit |
| - | - | - | - | - |
| python | 0.10.0 | 0.10.1 | Patch Upgrade | false |
| polars | herads_0 | herads_1 | Only build string | true |

## osx-arm64

| Dependency | Before | After | Change | Explicit |
| - | - | - | - | - |
| polars[^2] | 0.10.0 | 0.9.1 | Minor Downgrade | true |
| python | 0.10.0 | 0.10.1 | Patch Upgrade | true |

# lint

## linux-64

| Dependency | Before | After | Change | Explicit |
| - | - | - | - | - |
| polars | 0.10.0 | 0.10.1 | Patch Upgrade | true |
| python | 0.10.0 | 0.10.1 | Patch Upgrade | false |

[^1]: *Cursive* means explicit dependency.
[^2]: Dependency got downgraded.

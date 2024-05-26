## default

| Platform | Dependency | Before | After | Change | Explicit |
| -: | - | - | - | - | - |
| linux-64 | new-package |  | 0.10.1 | Added | true |
|| removed-package | 0.10.1 |  | Removed | true |
|| python | 0.10.0 | 0.10.0 | Patch Upgrade | false |
|| polars | herads_0 | herads_0 | Only build string | true |
| osx-arm64 | polars[^2] | 0.10.0 | 0.10.0 | Minor Downgrade | true |
|| python | 0.10.0 | 0.10.0 | Patch Upgrade | true |

## lint

| Platform | Dependency | Before | After | Change | Explicit |
| -: | - | - | - | - | - |
| linux-64 | polars | 0.10.0 | 0.10.0 | Patch Upgrade | true |
|| python | 0.10.0 | 0.10.0 | Patch Upgrade | false |

[^1]: *Cursive* means explicit dependency.
[^2]: Dependency got downgraded.

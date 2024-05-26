## default

| Platform | Dependency | Before | After | Change | Explicit | Package |
| -: | - | - | - | - | - | - |
| linux-64 | new-package |  | 0.10.1 | Added | true | conda |
|| removed-package | 0.10.1 |  | Removed | true | conda |
|| python | 0.10.0 | 0.10.0 | Patch Upgrade | false | conda |
|| polars | herads_0 | herads_0 | Only build string | true | conda |
| osx-arm64 | polars[^2] | 0.10.0 | 0.10.0 | Minor Downgrade | true | conda |
|| python | 0.10.0 | 0.10.0 | Patch Upgrade | true | conda |

## lint

| Platform | Dependency | Before | After | Change | Explicit | Package |
| -: | - | - | - | - | - | - |
| linux-64 | polars | 0.10.0 | 0.10.0 | Patch Upgrade | true | conda |
|| python | 0.10.0 | 0.10.0 | Patch Upgrade | false | conda |

[^1]: *Cursive* means explicit dependency.
[^2]: Dependency got downgraded.

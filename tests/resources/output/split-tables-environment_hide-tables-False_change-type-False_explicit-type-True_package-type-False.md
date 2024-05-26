## default

| Platform | Dependency | Before | After | Explicit |
| -: | - | - | - | - |
| linux-64 | python | 0.10.0 | 0.10.1 | false |
|| polars | herads_0 | herads_1 | true |
| osx-arm64 | polars[^2] | 0.10.0 | 0.9.1 | true |
|| python | 0.10.0 | 0.10.1 | true |

## lint

| Platform | Dependency | Before | After | Explicit |
| -: | - | - | - | - |
| linux-64 | polars | 0.10.0 | 0.10.1 | true |
|| python | 0.10.0 | 0.10.1 | false |

[^1]: *Cursive* means explicit dependency.
[^2]: Dependency got downgraded.

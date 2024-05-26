| Environment | Dependency | Before | After | Explicit |
| -: | - | - | - | - |
| default / linux-64 | new-package |  | 0.10.1 | true |
|| removed-package | 0.10.1 |  | true |
|| bpy | 0.10.1 | 2.10.1 | true |
|| python | 0.10.0 | 0.10.1 | false |
|| polars | herads_0 | herads_1 | true |
| default / osx-arm64 | polars[^2] | 0.10.0 | 0.9.1 | true |
|| python | 0.10.0 | 0.10.1 | true |
| lint / linux-64 | polars | 0.10.0 | 0.10.1 | true |
|| python | 0.10.0 | 0.10.1 | false |

[^1]: *Cursive* means explicit dependency.
[^2]: Dependency got downgraded.

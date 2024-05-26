| Environment | Dependency | Before | After | Explicit | Package |
| -: | - | - | - | - | - |
| default / linux-64 | python | 0.10.0 | 0.10.1 | false | conda |
|| polars | herads_0 | herads_1 | true | conda |
| default / osx-arm64 | polars[^2] | 0.10.0 | 0.9.1 | true | conda |
|| python | 0.10.0 | 0.10.1 | true | conda |
| lint / linux-64 | polars | 0.10.0 | 0.10.1 | true | conda |
|| python | 0.10.0 | 0.10.1 | false | conda |

[^1]: *Cursive* means explicit dependency.
[^2]: Dependency got downgraded.

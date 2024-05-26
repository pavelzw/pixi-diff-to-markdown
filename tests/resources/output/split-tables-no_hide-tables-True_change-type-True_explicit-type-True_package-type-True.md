| Environment | Dependency | Before | After | Change | Explicit | Package |
| -: | - | - | - | - | - | - |
| default / linux-64 | python | 0.10.0 | 0.10.1 | Patch Upgrade | false | conda |
|| polars | herads_0 | herads_1 | Only build string | true | conda |
| default / osx-arm64 | polars[^2] | 0.10.0 | 0.9.1 | Minor Downgrade | true | conda |
|| python | 0.10.0 | 0.10.1 | Patch Upgrade | true | conda |
| lint / linux-64 | polars | 0.10.0 | 0.10.1 | Patch Upgrade | true | conda |
|| python | 0.10.0 | 0.10.1 | Patch Upgrade | false | conda |

[^1]: *Cursive* means explicit dependency.
[^2]: Dependency got downgraded.

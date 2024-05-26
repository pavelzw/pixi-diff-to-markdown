| Environment | Dependency[^1] | Before | After | Package |
| -: | - | - | - | - |
| default / linux-64 | *new-package* |  | 0.10.1 | conda |
|| *removed-package* | 0.10.1 |  | conda |
|| python | 0.10.0 | 0.10.0 | conda |
|| *polars* | herads_0 | herads_0 | conda |
| default / osx-arm64 | *polars*[^2] | 0.10.0 | 0.10.0 | conda |
|| *python* | 0.10.0 | 0.10.0 | conda |
| lint / linux-64 | *polars* | 0.10.0 | 0.10.0 | conda |
|| python | 0.10.0 | 0.10.0 | conda |

[^1]: *Cursive* means explicit dependency.
[^2]: Dependency got downgraded.

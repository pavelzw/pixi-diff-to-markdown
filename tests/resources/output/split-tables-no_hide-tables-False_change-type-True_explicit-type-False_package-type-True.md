| Environment | Dependency[^1] | Before | After | Change | Package |
| -: | - | - | - | - | - |
| default / linux-64 | *new-package* |  | 0.10.1 | Added | conda |
|| *removed-package* | 0.10.1 |  | Removed | pypi |
|| *bpy* | 0.10.1 | 2.10.1 | Major Upgrade | pypi |
|| python | 0.10.0 | 0.10.1 | Patch Upgrade | conda |
|| *polars* | herads_0 | herads_1 | Only build string | conda |
| default / osx-arm64 | *polars*[^2] | 0.10.0 | 0.9.1 | Minor Downgrade | conda |
|| *python* | 0.10.0 | 0.10.1 | Patch Upgrade | conda |
| lint / linux-64 | *polars* | 0.10.0 | 0.10.1 | Patch Upgrade | conda |
|| python | 0.10.0 | 0.10.1 | Patch Upgrade | conda |

[^1]: *Cursive* means explicit dependency.
[^2]: Dependency got downgraded.

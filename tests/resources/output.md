| Environment | Dependency[^1] | Before | After | Change |
| -: | - | - | - | - |
| default / linux-64 | python | 0.10.0 | 0.10.1 | Patch Upgrade |
|| *polars* | herads_0 | herads_1 | Only build string |
| default / osx-arm64 | *polars*[^2] | 0.10.0 | 0.9.1 | Minor Downgrade |
|| *python* | 0.10.0 | 0.10.1 | Patch Upgrade |
| lint / linux-64 | *polars* | 0.10.0 | 0.10.1 | Patch Upgrade |
|| python | 0.10.0 | 0.10.1 | Patch Upgrade |

[^1]: *Cursive* means explicit dependency.
[^2]: Dependency got downgraded.
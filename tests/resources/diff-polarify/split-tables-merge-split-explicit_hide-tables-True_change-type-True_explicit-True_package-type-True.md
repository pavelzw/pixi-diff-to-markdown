## Explicit dependencies

|Dependency|Before|After|Change|Explicit|Package|Environments|
|-|-|-|-|-|-|-|
|pip|23.3.1|24.0|Major Upgrade|true|conda|default on osx-arm64|
|pip|23.3.2|24.0|Major Upgrade|true|conda|{lint, pl014, pl015, pl016, pl017, pl018, pl019, pl020, py310, py311, py312, py39} on osx-arm64<br/>*all envs* on {linux-64, osx-64, win-64}|
|pytest-cov|4.1.0|5.0.0|Major Upgrade|true|conda|{default, pl014, pl015, pl016, pl017, pl018, pl019, pl020, py310, py311, py312, py39} on *all platforms*|
|hatchling|1.21.1|1.24.2|Minor Upgrade|true|conda|*all*|
|hypothesis|6.97.4|6.103.2|Minor Upgrade|true|conda|default on *all platforms*<br/>{pl014, pl015, pl016, pl017, pl018, pl019, pl020, py310, py311, py312, py39} on {linux-64, osx-64, win-64}|
|hypothesis|6.97.1|6.103.2|Minor Upgrade|true|conda|{pl017, pl018, pl019, pl020, py310, py311, py312, py39} on osx-arm64|
|hypothesis|6.97.2|6.103.2|Minor Upgrade|true|conda|{pl014, pl015, pl016} on osx-arm64|
|pre-commit|3.6.0|3.7.1|Minor Upgrade|true|conda|lint on *all platforms*|
|pytest|8.0.0|8.2.2|Minor Upgrade|true|conda|{default, pl014, pl015, pl016, pl017, pl018, pl019, pl020, py310, py311, py312, py39} on *all platforms*|
|polars|0.20.3|0.20.31|Patch Upgrade|true|conda|default on osx-arm64|
|polars|0.20.6|0.20.31|Patch Upgrade|true|conda|pl020 on win-64<br/>default on {linux-64, osx-64, win-64}<br/>{lint, py310, py311, py312, py39} on *all platforms*|
|polars|0.20.16|0.20.31|Patch Upgrade|true|conda|pl020 on {linux-64, osx-64, osx-arm64}|
|python|3.12.0|3.12.3|Patch Upgrade|true|conda|default on osx-arm64|
|python|3.12.1|3.12.3|Patch Upgrade|true|conda|default on {linux-64, osx-64, win-64}<br/>{lint, py312} on *all platforms*|
|python|3.9.18|3.9.19|Patch Upgrade|true|conda|py39 on *all platforms*|
|python|3.10.13|3.10.14|Patch Upgrade|true|conda|py310 on *all platforms*|
|python|3.11.7|3.11.9|Patch Upgrade|true|conda|py311 on *all platforms*|

## Implicit dependencies

|Dependency|Before|After|Change|Explicit|Package|Environments|
|-|-|-|-|-|-|-|
|pip|23.3.1|24.0|Major Upgrade|true|conda|default on osx-arm64|
|pip|23.3.2|24.0|Major Upgrade|true|conda|{lint, pl014, pl015, pl016, pl017, pl018, pl019, pl020, py310, py311, py312, py39} on osx-arm64<br/>*all envs* on {linux-64, osx-64, win-64}|
|pytest-cov|4.1.0|5.0.0|Major Upgrade|true|conda|{default, pl014, pl015, pl016, pl017, pl018, pl019, pl020, py310, py311, py312, py39} on *all platforms*|
|hatchling|1.21.1|1.24.2|Minor Upgrade|true|conda|*all*|
|hypothesis|6.97.4|6.103.2|Minor Upgrade|true|conda|default on *all platforms*<br/>{pl014, pl015, pl016, pl017, pl018, pl019, pl020, py310, py311, py312, py39} on {linux-64, osx-64, win-64}|
|hypothesis|6.97.1|6.103.2|Minor Upgrade|true|conda|{pl017, pl018, pl019, pl020, py310, py311, py312, py39} on osx-arm64|
|hypothesis|6.97.2|6.103.2|Minor Upgrade|true|conda|{pl014, pl015, pl016} on osx-arm64|
|pre-commit|3.6.0|3.7.1|Minor Upgrade|true|conda|lint on *all platforms*|
|pytest|8.0.0|8.2.2|Minor Upgrade|true|conda|{default, pl014, pl015, pl016, pl017, pl018, pl019, pl020, py310, py311, py312, py39} on *all platforms*|
|polars|0.20.3|0.20.31|Patch Upgrade|true|conda|default on osx-arm64|
|polars|0.20.6|0.20.31|Patch Upgrade|true|conda|pl020 on win-64<br/>default on {linux-64, osx-64, win-64}<br/>{lint, py310, py311, py312, py39} on *all platforms*|
|polars|0.20.16|0.20.31|Patch Upgrade|true|conda|pl020 on {linux-64, osx-64, osx-arm64}|
|python|3.12.0|3.12.3|Patch Upgrade|true|conda|default on osx-arm64|
|python|3.12.1|3.12.3|Patch Upgrade|true|conda|default on {linux-64, osx-64, win-64}<br/>{lint, py312} on *all platforms*|
|python|3.9.18|3.9.19|Patch Upgrade|true|conda|py39 on *all platforms*|
|python|3.10.13|3.10.14|Patch Upgrade|true|conda|py310 on *all platforms*|
|python|3.11.7|3.11.9|Patch Upgrade|true|conda|py311 on *all platforms*|

[^1]: *Cursive* means explicit dependency.
[^2]: Dependency got downgraded.

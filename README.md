# pixi-diff-to-markdown

[![License][license-badge]](LICENSE)
[![Build Status][build-badge]][build]
[![Conda Platform][conda-badge]][conda-url]
[![Conda Downloads][conda-downloads-badge]][conda-url]
[![pypi-version][pypi-badge]][pypi]
[![python-version][python-version-badge]][pypi]
[![codecov][codecov-badge]][codecov]

[license-badge]: https://img.shields.io/github/license/pavelzw/pixi-diff-to-markdown?style=flat-square
[build-badge]: https://img.shields.io/github/actions/workflow/status/pavelzw/pixi-diff-to-markdown/ci.yml?style=flat-square&branch=main
[build]: https://github.com/pavelzw/pixi-diff-to-markdown/actions/
[conda-url]: https://prefix.dev/channels/conda-forge/packages/pixi-diff-to-markdown
[conda-badge]: https://img.shields.io/conda/pn/conda-forge/pixi-diff-to-markdown?style=flat-square&logoColor=white&logo=conda-forge
[conda-downloads-badge]: https://img.shields.io/conda/dn/conda-forge/pixi-diff-to-markdown?style=flat-square
[pypi]: https://pypi.org/project/pixi-diff-to-markdown
[pypi-badge]: https://img.shields.io/pypi/v/pixi-diff-to-markdown.svg?style=flat-square&logo=pypi&logoColor=white
[python-version-badge]: https://img.shields.io/pypi/pyversions/pixi-diff-to-markdown?style=flat-square&logoColor=white&logo=python
[codecov-badge]: https://img.shields.io/codecov/c/github/pavelzw/pixi-diff-to-markdown?style=flat-square&logo=codecov
[codecov]: https://codecov.io/gh/pavelzw/pixi-diff-to-markdown

`pixi-diff-to-markdown` is a tool that generates markdown from a JSON diff that's generated by `pixi update --json`.
It reads from the standard input and writes to the standard output.

```bash
pixi update --no-install --json | pixi exec pixi-diff-to-markdown > diff.md
```

> [!TIP]
> If you don't care about the environment being installed and only want to update the lockfile (for example in a CI pipeline), you can use `pixi update --json --no-install` to generate the diff.

Example output:

| Dependency                                                            | Before   | After    | Change            |
| --------------------------------------------------------------------- | -------- | -------- | ----------------- |
| **new-package**                                                       |          | 0.10.1   | Added             |
| **removed-package**                                                   | 0.10.1   |          | Removed           |
| **bpy**                                                               | 0.10.1   | 2.10.1   | Major Upgrade     |
| [**polars**](https://prefix.dev/channels/conda-forge/packages/polars) | herads_0 | herads_1 | Only build string |
| python                                                                | 0.10.0   | 0.10.1   | Patch Upgrade     |

> [!TIP]
> The sorting of the tables is done by explicit/implicit, change type and alphabetically.

## Installation

You can install `pixi-diff-to-markdown` using `pip` or `pixi`.

```bash
# via pixi
pixi global install pixi-diff-to-markdown
# via pip
pip install pixi-diff-to-markdown
```

## Configuration

Depending on your use case, you may want to configure the output of `pixi-diff-to-markdown`.
You can do this by creating a configuration section in `pixi.toml` or `pyproject.toml`.

```toml
# defaults
[tool.pixi-diff-to-markdown]
merge-dependencies = "no" # or "split-explicit" when there are three or more environments / platforms
hide = "auto"
max-expanded-rows = 10
change-type-column = true
explicit-column = false
package-type-column = false
create-links-for-packages = true
```

You can also override the configuration options by passing them as arguments to `pixi-diff-to-markdown`.

```bash
pixi update --json | pixi-diff-to-markdown --merge-dependencies=yes --explicit-column
```

### `merge-dependencies`

Depending on the amount of `environments` and `platforms` you have in your `pixi.toml`, it might make sense to either merge all dependencies into one table, split them by `explicit` and `implicit` dependencies or split them by `environment` and `platform`.
For a large amount of `environments` and `platforms`, it is recommended to merge the dependencies into one table for deduplication.
`merge-dependencies` can be set to one of the following values:

- `no`: Don't merge the dependencies, each environment will be displayed in their own table. Only recommended for a small amount of environments / platforms ([example](./tests/resources/diff-example/merge-no_hide-False_change-type-True_explicit-False_package-type-False.md)).
- `yes`: Merge all dependencies into one table and deduplicate them ([example](./tests/resources/diff-polarify/merge-yes_hide-False_change-type-True_explicit-False_package-type-False.md)).
- `split-explicit`: Merge all dependencies into one table and deduplicate them but split the table into one `explicit` and one `implicit` table ([example](./tests/resources/diff-polarify/merge-split-explicit_hide-False_change-type-True_explicit-False_package-type-False.md)).

The default is `no` when there are less than three environments / platforms and `split-explicit` when there are three or more environments / platforms.

### `hide`

Whether to hide the tables in a collapsible object.
`hide` can be set to one of the following values (defaults to `auto`):

- `no`: Don't hide the tables ([example](./tests/resources/diff-example/merge-no_hide-False_change-type-True_explicit-False_package-type-False.md)).
- `yes`: Put the tables in collapsible objects ([example](./tests/resources/diff-example/merge-no_hide-True_change-type-True_explicit-False_package-type-False.md)).
- `auto`: Put the tables in collapsible objects if there are at most `max-expanded-rows` rows in each table.

### `max-expanded-rows`

The maximum amount of rows in a table before it is hidden.
Defaults to `10`.

### `change-type-column`

Whether to enable the `Change` column in the output ([example true](./tests/resources/diff-example/merge-yes_hide-False_change-type-True_explicit-False_package-type-False.md), [example false](./tests/resources/diff-example/merge-yes_hide-False_change-type-False_explicit-False_package-type-False.md)).

### `explicit-column`

Whether to enable the `Explicit` column in the output ([example true](./tests/resources/diff-example/merge-yes_hide-False_change-type-True_explicit-True_package-type-False.md), [example false](./tests/resources/diff-example/merge-yes_hide-False_change-type-True_explicit-False_package-type-False.md)).
If a dependency is explicitly defined in `pixi.toml`, it will be marked as `Explicit`. Otherwise, it will be marked as `Implicit`.

If this is set to `false`, the `Explicit` column will be omitted and the explicitly defined dependencies will be marked as _cursive_.

### `package-type-column`

Whether to enable the `Package Type` column in the output ([example true](./tests/resources/diff-example/merge-yes_hide-False_change-type-True_explicit-False_package-type-True.md), [example false](./tests/resources/diff-example/merge-yes_hide-False_change-type-True_explicit-False_package-type-False.md)).
This column will show whether the dependency is a `conda` or `pypi` package.

### `create-links-for-packages`

Whether to create links for packages from public channels (i.e., `conda-forge` or `bioconda`, etc.) or channels on [prefix.dev](https://prefix.dev) ([example](./tests/resources/diff-example-v6-lockfile/merge-yes_hide-False_change-type-True_explicit-False_package-type-False.md)).
Defaults to `true`.

# aws-service-availability

<div align="center">

[![Build status](https://github.com/jensroland/aws-service-availability/workflows/build/badge.svg?branch=master&event=push)](https://github.com/jensroland/aws-service-availability/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/aws-service-availability.svg)](https://pypi.org/project/aws-service-availability/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/jensroland/aws-service-availability/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/jensroland/aws-service-availability/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/jensroland/aws-service-availability/releases)
[![License](https://img.shields.io/github/license/jensroland/aws-service-availability)](https://github.com/jensroland/aws-service-availability/blob/master/LICENSE)
![Coverage Report](assets/images/coverage.svg)

CLI tool for listing (un)available AWS services by region

</div>

## Very first steps

### Initialize your code

1. Initialize `git` inside your repo:

    ```bash
    cd aws-service-availability && git init
    ```

2. If you don't have `Poetry` installed run:

    ```bash
    make poetry-download
    ```

3. Initialize poetry and install `pre-commit` hooks:

    ```bash
    make install
    make pre-commit-install
    ```

4. Run the codestyle:

    ```bash
    make codestyle
    ```

5. Upload initial code to GitHub:

```bash
git add .
git commit -m ":tada: Initial commit"
git branch -M main
git remote add origin https://github.com/jensroland/aws-service-availability.git
git push -u origin main
```

### Set up bots

- Set up [Dependabot](https://docs.github.com/en/github/administering-a-repository/enabling-and-disabling-version-updates#enabling-github-dependabot-version-updates) to ensure you have the latest dependencies.
- Set up [Stale bot](https://github.com/apps/stale) for automatic issue closing.

### Poetry

Want to know more about Poetry? Check [its documentation](https://python-poetry.org/docs/).

<details>
<summary>Details about Poetry</summary>
<p>

Poetry's [commands](https://python-poetry.org/docs/cli/#commands) are very intuitive and easy to learn, like:

- `poetry add numpy@latest`
- `poetry run pytest`
- `poetry publish --build`

etc
</p>
</details>

### Building and releasing your package

Building a new version of the application contains steps:

- Bump the version of your package `poetry version <version>`. You can pass the new version explicitly, or a rule such as `major`, `minor`, or `patch`. For more details, refer to the [Semantic Versions](https://semver.org/) standard.
- Make a commit to `GitHub`.
- Create a `GitHub release`.
- And... publish 🙂 `poetry publish --build`

## 🚀 Features

- TODO

## Installation

```bash
pip install -U aws-service-availability
```

or install with `Poetry`

```bash
poetry add aws-service-availability
```

Then you can run

```bash
aws-service-availability --help
```

or with `Poetry`:

```bash
poetry run aws-service-availability --help
```

### Makefile usage

[`Makefile`](https://github.com/jensroland/aws-service-availability/blob/master/Makefile) contains a lot of functions for faster development.

<details>
<summary>1. Download and remove Poetry</summary>
<p>

To download and install Poetry run:

```bash
make poetry-download
```

To uninstall

```bash
make poetry-remove
```

</p>
</details>

<details>
<summary>2. Install all dependencies and pre-commit hooks</summary>
<p>

Install requirements:

```bash
make install
```

Pre-commit hooks coulb be installed after `git init` via

```bash
make pre-commit-install
```

</p>
</details>

<details>
<summary>3. Codestyle</summary>
<p>

Automatic formatting uses `pyupgrade`, `isort`, and `black`.

```bash
make codestyle

# or use synonym
make formatting
```

Codestyle checks only, without rewriting files:

```bash
make check-codestyle
```

> Note: `check-codestyle` uses `isort`, `black`, `darglint`, and `pylint`.

Update all dev libraries to the latest version using one comand

```bash
make update-dev-deps
```

</p>
</details>

<details>
<summary>4. Code security</summary>
<p>

```bash
make check-safety
```

This command launches `Poetry` integrity checks as well as identifies security issues with `Safety` and `Bandit`.

```bash
make check-safety
```

</p>
</details>

<details>
<summary>5. Type checks</summary>
<p>

Run `mypy` static type checker

```bash
make mypy
```

</p>
</details>

<details>
<summary>6. Tests with coverage badges</summary>
<p>

Run `pytest`

```bash
make test
```

</p>
</details>

<details>
<summary>7. All linters</summary>
<p>

Of course there is a command to ~~rule~~ run all linters in one:

```bash
make lint
```

the same as:

```bash
make test && make check-codestyle && make mypy && make check-safety
```

</p>
</details>

<details>
<summary>8. Docker</summary>
<p>

```bash
make docker-build
```

which is equivalent to:

```bash
make docker-build VERSION=latest
```

Remove docker image with

```bash
make docker-remove
```

More information [about docker](https://github.com/jensroland/aws-service-availability/tree/master/docker).

</p>
</details>

<details>
<summary>9. Cleanup</summary>
<p>
Delete pycache files

```bash
make pycache-remove
```

Remove package build

```bash
make build-remove
```

Delete .DS_STORE files

```bash
make dsstore-remove
```

Remove .mypycache

```bash
make mypycache-remove
```

Or to remove all above run:

```bash
make cleanup
```

</p>
</details>

## 📈 Releases

You can see the list of available releases on the [GitHub Releases](https://github.com/jensroland/aws-service-availability/releases) page.

We follow the [Semantic Versioning](https://semver.org/) specification.

We use [`Release Drafter`](https://github.com/marketplace/actions/release-drafter). As pull requests are merged, a draft release is kept up-to-date listing the changes, ready to publish when you’re ready. With the categories option, you can categorize pull requests in release notes using labels.

### List of labels and corresponding titles

|               **Label**               |  **Title in Releases**  |
| :-----------------------------------: | :---------------------: |
|       `enhancement`, `feature`        |       🚀 Features       |
| `bug`, `refactoring`, `bugfix`, `fix` | 🔧 Fixes & Refactoring  |
|       `build`, `ci`, `testing`        | 📦 Build System & CI/CD |
|              `breaking`               |   💥 Breaking Changes   |
|            `documentation`            |    📝 Documentation     |
|            `dependencies`             | ⬆️ Dependencies updates |

## 🛡 License

[![License](https://img.shields.io/github/license/jensroland/aws-service-availability)](https://github.com/jensroland/aws-service-availability/blob/master/LICENSE)

This project is licensed under the terms of the `GNU GPL v3.0` license. See [LICENSE](https://github.com/jensroland/aws-service-availability/blob/master/LICENSE) for more details.

## Credits

This project was generated with [`python-package-template`](https://github.com/JensRoland/python-package-template), based on [`python-package-template`](https://github.com/TezRomacH/python-package-template/) by Roman Tezikov

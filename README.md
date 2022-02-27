# aws-service-availability

<div align="center">

[![Build status](https://github.com/jensroland/aws-service-availability/workflows/build/badge.svg?branch=main&event=push)](https://github.com/jensroland/aws-service-availability/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/aws-service-availability.svg)](https://pypi.org/project/aws-service-availability/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/jensroland/aws-service-availability/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![License](https://img.shields.io/github/license/jensroland/aws-service-availability)](https://github.com/jensroland/aws-service-availability/blob/main/LICENSE)
![Coverage Report](assets/images/coverage.svg)

CLI tool for listing (un)available AWS services by region, because the [AWS regional services page](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/) no longer contains the useful table of supported services.

</div>

## 🚀 Features

- List all the supported services for a given AWS region
- List all the unsupported services for a given AWS region

## Installation

```bash
pip install -U aws-service-availability
```

or install with `Poetry`:

```bash
poetry add aws-service-availability
```

Then you can run the tool:

```bash
aws-service-availability list-supported-services eu-north-1
aws-service-availability list-unsupported-services eu-north-1
```

or with `Poetry`:

```bash
poetry run aws-service-availability list-supported-services eu-north-1
poetry run aws-service-availability list-unsupported-services eu-north-1
```

## 📈 Releases

You can see the list of available releases on the [GitHub Releases](https://github.com/jensroland/aws-service-availability/releases) page. We follow the [Semantic Versioning](https://semver.org/) specification.

## 🛡 License

[![License](https://img.shields.io/github/license/jensroland/aws-service-availability)](https://github.com/jensroland/aws-service-availability/blob/main/LICENSE)

This project is licensed under the terms of the `GNU GPL v3.0` license. See [LICENSE](https://github.com/jensroland/aws-service-availability/blob/main/LICENSE) for more details.

## Credits

This project was generated with [`python-package-template`](https://github.com/JensRoland/python-package-template), based on [`python-package-template`](https://github.com/TezRomacH/python-package-template/) by Roman Tezikov.

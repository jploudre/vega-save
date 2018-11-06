# vega-save
Save vega and vega-lite images in python purely offline.

[![Build Status](https://travis-ci.org/SyntaxRules/vega-save.svg?branch=master)](https://travis-ci.org/SyntaxRules/vega-save)[![codecov](https://codecov.io/gh/SyntaxRules/vega-save/branch/master/graph/badge.svg)](https://codecov.io/gh/SyntaxRules/vega-save)[![Dependabot Status](https://api.dependabot.com/badges/status?host=github&repo=SyntaxRules/vega-save)](https://dependabot.com)[![Documentation Status](https://readthedocs.org/projects/vega-save/badge/?version=latest)](https://vega-save.readthedocs.io/en/latest/?badge=latest)



Documentation: http://vega-save.readthedocs.io/en/latest/

## Versioning

This project uses [Semver](http://semver.org/) as its versioning scheme.

## Tests

Basic acceptance tests are in the tests folder. You can run these tests by running `python setup.py test`. The unit tests are in line with the code. You can run all the tests with `python -m pytest .`.

The tests are ran automatically when they are submitted to github via [travici.org](https://travis-ci.org/SyntaxRules/python-starter). Your tests must work here to be considered passing, it doesn't matter if they run on your local machine, if they fail on TravisCI, then they will not be accepted into matser.

Coverage is also determined by TravisCI and reported to [CodeCov](https://codecov.io/gh/SyntaxRules/python-starter).

## Documentation

Documentation is inline (like unit tests) and deployed with [Read the Docs](http://vega-save.readthedocs.io/en/latest/). When editing code, please include documentation for your changes. Add any new files to the `mkdocs.yml` file. The documentation is automatically built and installed.

The documentation is found here: http://vega-save.readthedocs.io/en/latest/

You can test the docs locally by installing [mkdocs](http://www.mkdocs.org/) and running `mkdocs serve` in the root directory of the project source. This will launch a server locally that you can use to view what the docs will look like when deployed. The pages update automatically when changes are made.

You can add a page to the documentation by editing the *mkdocs.yml* file in the source repo. See [Adding Pages](http://www.mkdocs.org/#adding-pages).
Great Magna Code - Tests
----------------------

[![circle-ci-image]][circle-ci]
[![snyk-image]][snyk]

Tests for [https://great-magna.staging.uktrade.digital](https://great-magna.staging.uktrade.digital).


## Contents

This repository contains:

* Tests suites:
    * [Functional (Browser) tests](tests/browser/README.md)
    * [Load tests](tests/load/README.md)
* [great_magna_tests_shared](great_magna_tests_shared/README.md) - a sub-project with shared test code

## Development

### General requirements

You'll need:

* Python 3.8+
* [pip](https://pypi.org/project/pip/) to install required dependencies
* [virtualenvwrapper](https://pypi.org/project/virtualenvwrapper/) to create a virtual python environment

### Installing

Following instructions apply to all test suites and tasks included in this repository.

```bash
git clone https://github.com/uktrade/great_magna_tests_shared
cd great_magna-tests
mkvirtualenv -p python3.8 {browser|load|tests_shared}
make requirements_{browser|load|tests_shared}
```

For all additional configuration instructions please check dedicated [README](#Contents).


### Requirements

There are separate sets of `requirement` files for every test suite and also for `great_magna_tests_shared`.

We use `pip-compile` (part of [pip-tools](https://pypi.org/project/pip-tools/) package) to compile pinned `requirements_*.txt` files from unpinned `requirement_*.in` files.

List of unpinned requirements files for all tests suites, tasks and sub-projects:

* [great_magna_tests_shared/requirements.in](great_magna_tests_shared/requirements.in)
* [requirements_browser.in](requirements_browser.in)
* [requirements_load.in](requirements_load.in)


#### Compiling requirements_*.txt files

To add, remove or change any dependency:
* first edit appropriate `requirements_*.in` file
* do not used pinned version of any dependency (unless the latest version of specific dependency introduced a braking change)
* recompile requirements file
    ```bash
    make compile_requirements_{browser|load|test_tools|tests_shared}
    ```

To recompile all requirement files at once use:
```bash
make compile_all_requirements
```

## Convenience shell scripts

To easily switch between env var configurations for different test environments (DEV, Staging, Beta),
please use dedicated convenience shell scripts. You can find those scripts in Rattic (look for `DIT test env vars`).  

Once you get hold of them you'll be able to locally run any test suite or task against specific test environment.

To make switching between configurations easier and faster, you can create handy shell aliases, like:

```bash
alias dev='source ~/dir-dev.sh';
alias stage='source ~/dir-stage.sh';
alias uat='source ~/dir-uat.sh';
```


### Env Vars

All required and optional Service URLs and Secrets such as API keys are specified in [env.json](env_vars/env.json).  
In order to run any test suite or task from this repository, locally or remotely, you'll have to have all of those env vars exported to shell.  

The reason why env vars are specified in aforementioned `env.json` file is because initially the tests we executed locally in docker containers and later on also in CircleCI.  
Setting env vars for a docker container via [env_file](https://docs.docker.com/compose/env-file/) requires a simple `key:val` file.
Whereas CircleCI allows you to either use a shell script that uses `export` command to set env vars or define env vars in project settings.
The latter solution is preferred but it's not ideal because there's no easy way to have a single project in CircleCI with different sets of secrets for different test environments.  
Moreover exporting env vars locally also requires a shell script that use `export` command to do the same.  

In order to address all of those requirements and have only one place where we specify all mandatory (and optional) env vars (for all test environments)
we've decided to use env vars prefixed with the name of test environment e.g. `DEV_`, `STAGE_`, `UAT_`, & `PROD_`.  
We've also wrote a convenience script [env_vars/env_writer.py](env_vars/env_writer.py) which:  

* checks if required env vars are set
* saves env vars without name prefix in files that can be used by locally, in a docker container or on a CI to export env vars.

#### env_writer.py

This scripts takes two arguments:
* `--env` - look for environment variables prefixed with "`ENV_`", where `ENV` can be e.g.: `DEV`, `STAGE`, `UAT` or `PROD`
* `--config` - specify input config file [defaults to: ./env_vars/env.json] with a list of required and optional env vars and output `file_path`.

Lets explain how this script works in a quasi-BDD scenario:

**Given** all required env vars are specified in `env.json` file e.g.: "`CMS_API_KEY`" & "`CMS_API_URL`"  
**When** `env_writer.py` is executed with `--env=DEV` and `--config=env.json`  
**Then** it will check if both "`DEV_CMS_API_KEY`" & "`DEV_CMS_API_URL`" env vars are set  
**And**  it will generate two env files (only if both env vars are set):  
    1) `.env_with_export` - a shell script which sets env vars with `export` command. (can be used with `source` or `.` shell commands)  
    2) `.env_without_export` - a simple `key:val` file. (can be used by `docker` or `docker-compose`)  
**Or** it will raise an exception if any required env var is missing

Using env vars with test environment prefixes allowed us to keep multiple sets of secrets in one CircleCI project.  


## Code style

All code in this repository is formatted with [black](https://pypi.org/project/black/) & [isort](https://pypi.org/project/isort/).  
It is highly advisable to use these tools to maintain a consistent code style across all test suites.  
To automate the process of code formatting with all aforementioned code formatters, code checkers
(like [flake8](https://pypi.org/project/flake8/)) and other linters you can use use [pre-commit](https://pre-commit.com/) tool.  

A ready to use `pre-commit` configuration is in [.pre-commit-config.yaml](.pre-commit-config.yaml).


## CircleCI

All test suites, periodic tasks & tests are executed every day (Mon through Fri) in CircleCI against `Dev`, `Staging` & `UAT` environments.

Test workflows are defined in [.circleci/config.yml](.circleci/config.yml#L1259).

Workflows were designed with DRY rule in mind. Code duplication is kept to necessary minimum.

Every workflow consists of one or more jobs. A job is built with multi-step blocks.
Every step should have "Single Responsibility" like installing requirements or running tests.
Thanks to this approach we've reduced code duplication and increased readability.  
More on that topic in CircleCI [Reusable Config Reference Guide](https://circleci.com/docs/2.0/reusing-config/)


[circle-ci-image]: https://circleci.com/gh/uktrade/great-magna-tests/tree/master.svg?style=svg
[circle-ci]: https://circleci.com/gh/uktrade/great-magna-tests/tree/master

[codecov-image]: https://codecov.io/gh/uktrade/great-magna-tests/branch/master/graph/badge.svg
[codecov]: https://codecov.io/gh/uktrade/great-magna-tests

[snyk-image]: https://snyk.io/test/github/uktrade/great-magna-tests/badge.svg
[snyk]: https://snyk.io/test/github/uktrade/great-magna-tests

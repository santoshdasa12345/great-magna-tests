# <span style="color:orange">Great Magna Code - Tests</span>

[![circle-ci-image]][circle-ci]
[![snyk-image]][snyk]

## <span style="color:orange">Background</span>
This repo is a dockerised test suite for [Great](https://great.gov.uk/).
## <span style="color:orange">Available tests</span>

Test types:
* Load
* Functional
* Browser
* Smoke

Environments:
* [Dev](https://great.dev.uktrade.digital/)
* [Stage](https://great.stage.uktrade.digital/)
* [UAT](https://great.uat.uktrade.digital/)
* [Prod](https://great.gov.uk/)

## <span style="color:orange">Prerequisites</span>
To follow along with this tutorial you will need to ensure you have the following installed on your machine.

* [Docker Desktop](https://docs.docker.com/desktop/install/mac-install/)
* [Cloud Foundry CLI](https://admin.london.cloud.service.gov.uk/organisations)
* SSH access to [uktrade](https://github.com/uktrade/) on Github
* VPN access

## <span style="color:orange">Resources<span>
This repo have confluence instructions. Please refer to these pages on your specific requirements.

Test type | Confluence page 
--- | --- 
Load  | [https://uktrade.atlassian.net/wiki/spaces/ED/pages/3560243231/Running+Load+Tests+Locally](https://uktrade.atlassian.net/wiki/spaces/ED/pages/3560243231/Running+Load+Tests+Locally)

## <span style="color:orange">Repository<span>
1. Navigate to your development directory and open a terminal.
2. Clone the development repository:
    ```
    git clone https://github.com/uktrade/great-magna-tests.git
    cd great_magna-tests
    ```

## <span style="color:orange">Start Docker Container<span>

Use the following command to run tests:
> Make sure Docker is running on your machine!

1. Open a terminal on your machine.

2. Optional step! Prune docker.
    You may want to prune un-used Docker images and containers.
    ```
    docker system prune
    ```

3. Fire up a dev Docker container and run tests.
    > Note: you may want to prune un used Docker images and containers

    Test type  | Command
    --- | ---
    Load | ```make build compose/docker-compose-load.yml```
    Browser | ```make build compose/docker-compose-browser.yml```
    Functional | ```make build compose/docker-compose-functional.yml```
    Smoke | ```make build compose/docker-compose-smoke.yml```


## <span style="color:orange">Run Tests<span>

Use the following command to run tests:
> Make sure Docker is running on your machine!

1. Open a terminal on your machine.

2. Optional step! Prune docker.
    You may want to prune un-used Docker images and containers.
    ```
    docker system prune
    ```

3. Fire up a dev Docker container and run tests.
    > Note: you may want to prune un used Docker images and containers

    Test type | Environment  | Command
    --- | ---  | ---
    Load  | Dev  | ```./start-docker.sh -e dev -t load```
    Load  | Stage  | ```./start-docker.sh -e stage -t load```
    Load  | UAT  | ```./start-docker.sh -e uat -t load```
    Load  | Prod  | ```./start-docker.sh -e prod -t load```


>Note: The following instructions assume that docker is running with no errors
## <span style="color:orange">Running commands<span>
All repository commands work within the docker container.
You can user docker desktops built-in terminal to run python commands. You can also use your IDE/Text editor of choice with the following commands.


Test type  | Command
--- | ---
Load | ```make enter-container load-tests```
Browser | ```make enter-container browser-tests```
Functional | ```make enter-container functional-tests```
Smoke | ```make enter-container smoke-tests```

## <span style="color:orange">Example commands<span>
Here are a few common commands for reference

Objective | Command
--- | ---
Compile requirements  | ```make requirements```
Install requirements  | ```make install-requirements```
Open Python interpreter  | ```python```
Auto format  | ```make format```

***
***
ARGUMENTS=$(filter-out $@,$(MAKECMDGOALS)) $(filter-out --,$(MAKEFLAGS))
include *.mk

clean:
	-find . -type f -name "*.pyc" -delete
	-find . -type d -name "__pycache__" -delete
	-find . -type f -name "behave.log" -delete
	-find ./results/ -type f -not -name '.gitignore' -delete
	-find ./reports/ -type f -not -name '.gitignore' -delete
	-find ./tests/browser/results/ -type f -not -name '.gitignore' -delete
	-find ./tests/browser/reports/ -type f -not -name '.gitignore' -delete
	-rm -fr ./allure_report/
	-rm -fr ./tests/browser/reports/*.xml

pep8:
	flake8 .

format:
	@isort --recursive .
	@black .

# compare contents of Staging & Dev environments by default
SERVICE ?= invest
ENVS_TO_COMPARE ?= stage_dev
TEST_ENV ?= DEV


geckoboard_updater:
	PYTHONPATH=. python3 ./tests/periodic_tasks/geckoboard_updater/geckoboard_updater.py


# Locust
LOCUST := \
	locust \
		--locustfile $$LOCUST_FILE \
		--users=$$NUM_USERS \
		--hatch-rate=$$HATCH_RATE \
		--run-time=$$RUN_TIME \
		--csv=./reports/results \
		--headless || true

BROWSER ?= chrome
BROWSER_ENVIRONMENT ?= local
HEADLESS ?= false
AUTO_RETRY ?= false
BROWSER_TYPE ?= desktop
VERSION ?= ""

load_test_sign_in:
	export LOCUST_FILE=./locustfile_sign_in.py; \
	$(LOCUST)

load_test_cms:
	export LOCUST_FILE=./locustfile_cms.py; \
	$(LOCUST)

load_test_domestic:
	export LOCUST_FILE=./locustfile_domestic.py; \
	$(LOCUST)
TEST_ENV ?= DEV

smoke_tests:
	#pytest --capture=no --verbose --alluredir=results/ --allure-link-pattern=issue:$(BUG_TRACKER_URL_PATTERN) --junitxml=reports/smoke.xml tests/smoke $(PYTEST_ARGS) || true
	cd tests/smoke && \
	BROWSER_ENVIRONMENT=$(BROWSER_ENVIRONMENT) BROWSER_TYPE=$(BROWSER_TYPE) BROWSER=$(BROWSER) VERSION=$(VERSION) HEADLESS=$(HEADLESS) AUTO_RETRY=$(AUTO_RETRY) behave --format=allure_behave.formatter:AllureFormatter --define AllureFormatter.issue_pattern=$(BUG_TRACKER_URL_PATTERN) --define AllureFormatter.link_pattern=$(BUG_TRACKER_URL_PATTERN) --outfile=smoke_results/ -f pretty --no-skipped --tags=~@wip --tags=~@fixme --tags=~@skip ${TAGS}


functional_tests:
	behave --no-skipped --format progress3 --logging-filter=-root --stop --tags=~@wip --tags=~@skip --tags=~@fixme tests/functional/features ${TAGS}

functional_tests_feature_dir:
	behave --format=allure_behave.formatter:AllureFormatter --define AllureFormatter.issue_pattern=$(BUG_TRACKER_URL_PATTERN) --define AllureFormatter.link_pattern=$(BUG_TRACKER_URL_PATTERN) --outfile=results_${FEATURE_DIR}/ --no-skipped --format progress3 --logging-filter=-root --tags=~@wip --tags=~@skip --tags=~@fixme tests/functional/features/${FEATURE_DIR} ${TAGS} || true

BROWSER ?= firefox
HEADLESS ?= false
AUTO_RETRY ?= true
BROWSER_TYPE ?= desktop
VERSION ?= ""


browser_tests_locally:
	cd tests/browser && \
	BROWSER_ENVIRONMENT=$(BROWSER_ENVIRONMENT) BROWSER_TYPE=$(BROWSER_TYPE) BROWSER=$(BROWSER) VERSION=$(VERSION) HEADLESS=$(HEADLESS) AUTO_RETRY=$(AUTO_RETRY) behave --format=allure_behave.formatter:AllureFormatter --define AllureFormatter.issue_pattern=$(BUG_TRACKER_URL_PATTERN) --define AllureFormatter.link_pattern=$(BUG_TRACKER_URL_PATTERN) --outfile=results/ -f pretty --no-skipped --tags=~@wip --tags=~@fixme --tags=~@skip ${TAGS}

requirements:
	pip-compile requirements.in

install_requirements:
	pip install -r requirements.txt

find_duplicated_scenario_names: SHELL:=/usr/bin/env bash  # set shell for this target to bash
find_duplicated_scenario_names:
	@diff -u <(behave $(ARGUMENTS) --dry --no-source --no-summary --no-snippets | grep 'Scenario' | sort) \
		<(behave $(ARGUMENTS) --dry --no-source --no-summary --no-snippets | grep 'Scenario' | sort -u)

results_browser:
	@for directory in $(shell find ./ -maxdepth 1 -iname "results_chrome_*" -type d -printf '%P\n') ; do echo "Processing results from $${directory}"; ./update_results.py "$${directory}" Chrome; mv ./$${directory}/* results/ | true; done
	@for directory in $(shell find ./ -maxdepth 1 -iname "results_firefox_*" -type d -printf '%P\n') ; do echo "Processing results from $${directory}"; ./update_results.py "$${directory}" Firefox; mv ./$${directory}/* results/ | true; done


results_functional:
	@for suite in fas sso profile international ; \
	do \
		if test -d "./results_$$suite"; \
		then \
			if [ -n "$$(ls -A results_$$suite 2>/dev/null)" ]; \
				then \
					./update_results.py results_$$suite $$suite; \
					mv ./results_$$suite/* results/; \
				else \
					echo "./results_$$suite is empty"; \
				fi \
		else \
			echo ./results_$$suite does not exist; \
		fi \
	done

serve:
	@echo Allure
	@allure --version
	@allure serve tests/browser/results/

serve_smoke:
	@echo Allure
	@allure --version
	@allure serve tests/smoke/smoke_results/

report:
	@echo Allure
	@allure --version
	@allure generate --clean --output ./allure_report tests/browser/results/

report_smoke:
	@echo Allure
	@allure --version
	@allure generate --clean --output ./allure_report tests/smoke/smoke_results/

.PHONY: build clean results_browser report

cf-signin:
	cf login -a api.london.cloud.service.gov.uk -u $(ARGUMENTS) -o dit-staging -s directory-dev

cf-signin-sso:
	cf login --sso -a api.london.cloud.service.gov.uk -u $(ARGUMENTS) -o dit-staging -s directory-dev


cf-load-dev-signin-sso:
	cf login --sso -a api.london.cloud.service.gov.uk -u $(ARGUMENTS) -o dit-staging -s directory-dev

install-cf-conduit:
	cf install-plugin conduit

build:
	docker-compose -f $(ARGUMENTS) up -d --build

enter-container:
	docker exec -it $(ARGUMENTS) bash

down:
	docker-compose -f $(ARGUMENTS) down

down_v:
	docker-compose -f $(ARGUMENTS) down -v


locust:
	docker exec load-tests \
		locust --headless -f $(LOCUST_FILE) --users=$(NUM_USERS) --spawn-rate=$(SPAWN_RATE) --run-time=$(RUN_TIME) --html=$(HTML_FILE)

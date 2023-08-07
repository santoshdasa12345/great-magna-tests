# -*- coding: utf-8 -*-
from random import choice

from locust import HttpUser, TaskSet, between, task

from directory_tests_shared.directory_tests_shared import URLs, settings
from directory_tests_shared.directory_tests_shared.constants import (
    LOAD_TESTS_USER_AGENT,
)
from directory_tests_shared.directory_tests_shared.utils import basic_auth, rare_word


class DomesticTasks(TaskSet):
    @task
    def advice_and_markets(self):
        self.client.get(
            choice(settings.ADVICE_AND_MARKETS),
            headers=LOAD_TESTS_USER_AGENT,
            name="advice & markets",
            auth=basic_auth(),
        )

    @task
    def misc_pages(self):
        self.client.get(
            choice(settings.MISC_ENDPOINTS),
            headers=LOAD_TESTS_USER_AGENT,
            name="misc pages",
            auth=basic_auth(),
        )

    @task
    def search(self):
        url = URLs.DOMESTIC_SEARCH.relative
        params = {"q": rare_word()}

        self.client.get(
            url,
            params=params,
            headers=LOAD_TESTS_USER_AGENT,
            name="search/?q=[...]",
            auth=basic_auth(),
        )


class Domestic(HttpUser):
    host = settings.DOMESTIC_URL
    tasks = [DomesticTasks]
    wait_time = between(settings.LOCUST_MIN_WAIT, settings.LOCUST_MAX_WAIT)

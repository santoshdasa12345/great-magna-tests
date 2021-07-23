# -*- coding: utf-8 -*-
from random import choice

from locust import HttpUser, TaskSet, between, task

from great_magna_tests_shared import URLs, settings


class signUpTasks(TaskSet):
    @task
    def landing(self):
        self.client.get("/")

    @task
    def signUpPage(self):
        response = self.client.get("/")
        csrftoken = response.cookies['csrftoken']
        csrfmiddlewaretoken = f"csrfmiddlewaretoken={settings.CSRFMIDDLEWARETOKEN}&proddesc=cake"
        self.client.post(url="signup/",
                         data=csrfmiddlewaretoken,
                         headers={'referer': URLs.GREAT_MAGNA_SIGNUP.absolute,
                                  "X-CSRFToken": csrftoken},
                         )


class loginTasks(HttpUser):
    host = settings.GREAT_MAGNA_LOGIN
    tasks = [LoginTasks]
    wait_time = between(settings.LOCUST_MIN_WAIT, settings.LOCUST_MAX_WAIT)

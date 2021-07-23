# -*- coding: utf-8 -*-
"""SSO static assets - Page Object."""
from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service

NAME = "Static assets"
SERVICE = Service.SSO
TYPE = PageType.FORM
URL = URLs.SSO_API_LANDING.absolute
PAGE_TITLE = "Static assets"

SELECTORS = {}

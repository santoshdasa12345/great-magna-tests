# -*- coding: utf-8 -*-
from typing import Tuple

import pytest
from requests import Session
from requests.auth import HTTPBasicAuth
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT

from great_magna_tests_shared import URLs
from great_magna_tests_shared.clients import (  # CMS_API_CLIENT,
    BASIC_AUTHENTICATOR,
    SSO_API_CLIENT,
)
from great_magna_tests_shared.settings import BASICAUTH_PASS, BASICAUTH_USER

#
#
# @pytest.fixture
# def cms_client():
#     return CMS_API_CLIENT


@pytest.fixture
def basic_auth():
    return HTTPBasicAuth(BASICAUTH_USER, BASICAUTH_PASS)


def extract_csrf_middleware_token(content: str) -> str:
    line = [l for l in content.splitlines() if "csrfmiddlewaretoken" in l][0]
    delimiter = '"' if '"' in line else "'"
    fields = line.strip().split(delimiter)
    token_position = 5
    return fields[token_position]


#


@pytest.fixture
def test_sso_user() -> dict:
    """Creates an unverified test SSO user.

    Such user won't have any business profile associated with it.
    It can be treated as a UK Tax payer account.

    :returns a dict with basic user details
    {
        'email': 'test+451359d7e7e644278cc66f4342c78741@ci.uktrade.io',
        'password': 'password',
        'id': 34715,
        'first_name': 'Automated',
        'last_name': 'Test',
        'job_title': 'AUTOMATED TESTS',
        'mobile_phone_number': 1027958256750
    }
    """
    create_user_response = SSO_API_CLIENT.post(
        "/testapi/test-users/", data={}, authenticator=BASIC_AUTHENTICATOR
    )
    assert create_user_response.status_code == HTTP_200_OK
    return create_user_response.json()


@pytest.fixture
def test_sso_user_verified(test_sso_user) -> dict:
    """Creates a verified test SSO user.

    Such user won't have any business profile associated with it.
    It can be treated as a UK Tax payer account.
    """
    verify_response = SSO_API_CLIENT.patch(
        url=f"testapi/user-by-email/{test_sso_user['email']}/",
        data={"is_verified": True},
        authenticator=BASIC_AUTHENTICATOR,
    )
    assert verify_response.status_code == HTTP_204_NO_CONTENT
    return test_sso_user


@pytest.fixture
def session_and_csrf_middleware_token() -> Tuple[Session, str]:
    session = Session()
    login_url = URLs.SSO_LOGIN.absolute
    response = session.get(url=login_url, auth=(BASICAUTH_USER, BASICAUTH_PASS))
    assert (
        response.status_code == 200
    ), f"Expected 200 but got {response.status_code} from {response.url}"
    return session, extract_csrf_middleware_token(response.content.decode("UTF-8"))


#
@pytest.fixture
def logged_in_session_and_user(
    test_sso_user_verified: dict, session_and_csrf_middleware_token: Tuple[Session, str]
) -> Tuple[Session, dict]:
    session, csrfmiddlewaretoken = session_and_csrf_middleware_token
    data = {
        "login": test_sso_user_verified["email"],
        "password": test_sso_user_verified["password"],
        "csrfmiddlewaretoken": csrfmiddlewaretoken,
        "next": URLs.PROFILE_ABOUT.absolute,
    }
    response = session.post(
        url=URLs.SSO_LOGIN.absolute,
        data=data,
        allow_redirects=True,
        auth=(BASICAUTH_USER, BASICAUTH_PASS),
    )
    error = f"Expected 200 but got {response.status_code} from {response.url}"
    assert response.status_code == 200, error
    error = f"Couldn't find 'Sign out' in the response from: {response.url}"
    assert "Sign out" in response.content.decode("UTF-8"), error
    return session, test_sso_user_verified


# @pytest.fixture
# def logged_in_session(logged_in_session_and_user: Tuple[Session, dict]) -> Session:
#     session, _ = logged_in_session_and_user
#     return session

# def generic_set_basic_auth_creds(driver: WebDriver, *, service_name: str = None):
#     base_url = URLs.GREAT_MAGNA_START.absolute
#     parsed = urlparse(base_url)
#     logging.debug(parsed)
#     #with_creds = f"{parsed.scheme}://{BASICAUTH_USER}:{BASICAUTH_PASS}@{parsed.netloc}{parsed.path}"
#     with_creds = f"{parsed.scheme}://{parsed.netloc}/login?enc=gAAAAABgF-Gia1slIhrlp4r6x3BdqsFCnpp1VRANWAhb6fDX_VnPi8iDIaXNYceAq-Z7e234b77gF-_HlPmQue6L47pnvKr46xU6s22ZC-4m8En3V4uISwY="
#     logging.debug(f"Doing basic auth")
#     beta_user_token = "gAAAAABfsppja2o9NnJuOzzlW76Alej9q6u96Pj_S7jfHuyWiR5rD3QRnncKCARpoN0c5A8aNPfBn7bzvNf42xiiyvCDXa5YfgnyNewjqymHFXKR4cqESOY="
#     with wait_for_page_load_after_action(driver):
#         #driver.add_cookie(({'name' : 'beta-user', 'value' : beta_user_token}))
#         driver.get(with_creds)
#     #driver.add_cookie({'name': 'beta-user', 'value': beta_user_token})
#     #driver.add_cookie({'name':'csrftoken', 'value': 'zNbUFyadpZzFKXqUFwTqy537f2ygmVQLnQwsKLGaFC7eEI4TbTB2YKEbUfKcQ2qP'})
#     #logging.debug(driver.get_cookies())
#     assertion_msg = f"Access is still denied after authentication attempt → {base_url}"
#     with selenium_action(driver, assertion_msg):
#         assert "ok" in driver.page_source

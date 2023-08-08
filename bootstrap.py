import os
import sys

import hvac
import requests


class RVault:
    def __init__(self):
        self.ENVIRONMENT = sys.argv[1]
        self.WORKSPACE = os.environ.get("WORKSPACE")
        self.VAULT_API = os.environ.get("VAULT_API")
        self.VAULT_PREFIX = os.environ.get("VAULT_PREFIX")
        self.VAULT_ROLE = os.environ.get("VAULT_ROLE")
        self.VAULT_ROLE_ID = os.environ.get("VAULT_ROLE_ID")
        self.VAULT_TOKEN_ID = os.environ.get("VAULT_TOKEN_ID")
        self.VAULT_SECRET_ID = os.environ.get("VAULT_SECRET_ID")
        self.ENV_FILE = f"#{self.WORKSPACE}/great-magna-tests/env.json"
        self.URL = f"{self.VAULT_API}/{self.VAULT_PREFIX}/directory/great-magna-tests/{self.ENVIRONMENT}_eu-west-2"
        self.AUTH_URL = f"{self.VAULT_API}/auth/approle/login"

    def get_token(self):
        data = {"role_id": self.VAULT_ROLE_ID, "secret_id": self.VAULT_SECRET_ID}

        response = requests.post(
            self.URL,
            data=data,
        )
        print(response.json())
        if response.status_code == 200:
            return response.json()["auth"]["client_token"]
        return None

    def secrets(self):
        token = self.get_token()
        if token:
            response = requests.get(
                self.URL, headers={"X-Vault-Token": self.get_token()}
            )
            print(response.json())
            if response.status_code == 200:
                data = response.json()["data"]["data"]
                with open(self.ENV_FILE, "w") as outfile:
                    outfile.write(data)


class HVault:
    def __init__(self):
        self.ENVIRONMENT = sys.argv[1]
        self.WORKSPACE = os.environ.get("WORKSPACE")
        self.VAULT_API = os.environ.get("VAULT_API").replace("/v1", "")
        self.VAULT_PREFIX = os.environ.get("VAULT_PREFIX")
        self.VAULT_ROLE = os.environ.get("VAULT_ROLE")
        self.VAULT_ROLE_ID = os.environ.get("VAULT_ROLE_ID")
        self.VAULT_TOKEN_ID = os.environ.get("VAULT_TOKEN_ID")
        self.VAULT_SECRET_ID = os.environ.get("VAULT_SECRET_ID")
        self.ENV_FILE = f"#{self.WORKSPACE}/great-magna-tests/env.json"

    def client(self):
        # Create a client instance
        client = hvac.Client(self.VAULT_API)

        # Enable approle auth
        client.sys.enable_auth_method(
            method_type="approle",
        )

        # Authenticate to Vault with role_id and secret
        client.auth.approle.login(
            role_id=self.VAULT_ROLE_ID,
            secret_id=self.VAULT_SECRET_ID,
        )

        print(f"Authentication status: {client.is_authenticated()}")

        return client

    def secrets(self):
        client = self.client()
        # Perform operations with Vault
        secrets = client.secrets.kv.v2.read_secret_version(
            path=f"/{self.VAULT_PREFIX}/directory/great-magna-tests/{self.ENVIRONMENT}_eu-west-2"
        )
        if secrets:
            data = secrets["data"]["data"]
            with open(self.ENV_FILE, "w") as outfile:
                outfile.write(data)
        client.logout()


# HVault().secrets()
RVault().secrets()

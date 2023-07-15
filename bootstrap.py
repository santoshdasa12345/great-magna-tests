import hvac
import os
import sys

class Vault:
    
    def __init__(self):
      self.ENVIRONMENT = sys.argv[1]
      self.WORKSPACE = os.environ.get('WORKSPACE')
      self.VAULT_API = os.environ.get('VAULT_API')
      self.VAULT_PREFIX = os.environ.get('VAULT_PREFIX')
      self.VAULT_ROLE_ID = os.environ.get('VAULT_ROLE_ID')
      self.VAULT_SECRET_ID = os.environ.get('VAULT_SERECT_ID')
      self.ENV_FILE = f"#{self.WORKSPACE}/great-magna-tests/env.json"

    def client(self):

      # Create a client instance
      client = hvac.Client(url=self.VAULT_API)  # Replace with your Vault URL
      
      # Enable approle auth
      client.sys.enable_auth_method(
          method_type='approle',
      )

      # Authenticate to Vault with role_id and secret
      client.auth.approle.login(
          role_id=self.VAULT_ROLE_ID,
          secret_id=self.VAULT_SECRET_ID,
      )

      return client

    def secrets(self):
      
      client = self.client()
      # Perform operations with Vault
      secrets = client.secrets.kv.v2.read_secret_version(
         path=f'/{self.VAULT_PREFIX}dit/directory/great-magna-tests/{self.ENVIRONMENT}_eu-west-2'
         )
      if secrets:
          data = secrets['data']['data']
          with open(self.ENV_FILE, "w") as outfile:
              outfile.write(data)
      client.logout()


Vault().secrets()
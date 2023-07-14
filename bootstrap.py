import hvac
import os

WORKSPACE = os.environ.get('WORKSPACE')
CONFIG_DIR = f"#{WORKSPACE}/great-magna-tests/config"
JSON_SCHEMA = f"#{WORKSPACE}/great-magna-tests/schema.json"
CONSUL = os.environ.get('CONSUL')
VAULT_API = os.environ.get('VAULT_API')
VAULT_PREFIX = os.environ.get('VAULT_PREFIX')
VAULT_ROLE_ID = os.environ.get('VAULT_ROLE_ID')
VAULT_SERECT_ID = os.environ.get('VAULT_SERECT_ID')
OPTION_FILE = f"#{WORKSPACE}/great-magna-tests/.option.json"
ENV_FILE = f"#{WORKSPACE}/great-magna-tests/env.json"
CONF_FILE = f"#{WORKSPACE}/great-magna-tests/config.json"

print(WORKSPACE)
print(VAULT_API)
print(VAULT_PREFIX)
print(VAULT_ROLE_ID)
print(VAULT_SERECT_ID)


# Create a client instance
client = hvac.Client(url='https://vault.ci.uktrade.digital/ui/vault/secrets/dit%2Fdirectory/')  # Replace with your Vault URL

# Authenticate to Vault
client.auth.userpass(username=VAULT_ROLE_ID, password=VAULT_SERECT_ID)  # Replace with your username and password

# Check if authentication was successful
if not client.is_authenticated():
    print("Authentication failed. Please check your credentials.")
    exit()

# Perform operations with Vault
secrets = client.secrets.kv.v2.read_secret_version(path='great-magna-tests/dev_eu-west-2')  # Replace with your secret path
if secrets:
    data = secrets['data']['data']
    with open(ENV_FILE, "w") as outfile:
        outfile.write(data)
else:
    print("Failed to retrieve secrets.")

# Disconnect from Vault
client.logout()

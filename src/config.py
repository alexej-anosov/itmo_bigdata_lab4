import os
from ansible_vault import Vault


vault = Vault(os.getenv('VAULT_PASSWORD'))

secrets = vault.load(open('../secrets.yml').read())

class Config:
    DB_URL = secrets["DB_URL"]

    
config = Config()

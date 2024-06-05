import requests
import os
import base64
from dotenv import load_dotenv

load_dotenv()

BASE = "https://weaviate-n2ppa-u16782.vm.elestio.app/v1"

SCHEMA = BASE + "/schema"
GET_OBJ = BASE + "/objects"


username = "root"
password = "CZLTVzJz-PgmQ-jttFcU9k"

auth_config = "Basic " + base64.b64encode(f"{username}:{password}".encode()).decode()

header = {"Authorization": auth_config, "X-Cohere-Api-Key": os.environ.get('COHERE_API_KEY')}

res = requests.get(GET_OBJ, headers=header)
print(*res.json()['objects'], end="\n")

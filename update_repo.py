import os
from requests import Session
import json
from git import Repo

def update_repo_readme():
    with Repo()
    with open(os.path.join(os.getcwd(), "README.md"), "w") as f:
        with Session() as s:
            s.headers.update({"User-Agent": "Stilt34/Vanilla Sounds", "Authorization": os.environ["MODRINTH_VS_PAT"]})
            
            f.write(json.loads(s.get(os.environ["MODRINTH_VS_API"]).text)["body"])


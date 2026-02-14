import os
from requests import Session
import json

def check_version_uploaded_already(v : str) -> bool:
    with Session() as s:
        s.headers.update({"User-Agent": "Stilt34/Vanilla Sounds", "Authorization": os.environ["MODRINTH_VS_PAT"]})
        l = []
        vers = json.loads(s.get(os.environ["MODRINTH_VS_API"]+"/version").text)

        for i in vers:
            if(i["game_versions"][0]==v):
                print(f"Version {v} of Vanilla Sounds is already uploaded on Modrinth hence skipping its creation.")
                return True
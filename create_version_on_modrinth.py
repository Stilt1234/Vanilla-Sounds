import os
import json
from requests import Session

def create_version(v: str):
    with Session() as session:

        session.headers.update({"User-Agent": "Stilt34/Vanilla Sounds", "Authorization": os.environ["MODRINTH_VS_PAT"]})

        data = {
            "name": f"Vanilla Sounds Minecraft {v}",
            "version_number": "1.0.0",
            "changelog": f"## Vanilla Sounds Resource Pack for Minecraft version {v}.",
            "game_versions": [v],
            "version_type": "release",
            "loaders": ["minecraft"],
            "featured": True,
            "status": "listed",
            "project_id": json.loads(session.get(os.environ["MODRINTH_VS_API"]).text)["id"],
            "file_parts": ["file"],
            "primary_file": "file",
            "dependencies": []
        }

        with open(os.path.join(os.getcwd(), "Vanilla Sounds.zip"), "rb") as zip: 
            files = {
                "data": (None, json.dumps(data), "application/json"),
                "file": ("Vanilla Sounds.zip", zip, "application/zip")
            }

            print(session.post("https://api.modrinth.com/v2/version", files=files).text)

    print(f"Created a new version and uploaded Vanilla Sounds Resource Pack for Minecraft version {v}.")

create_version("1.6.1")
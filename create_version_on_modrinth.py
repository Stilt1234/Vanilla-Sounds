import os
import json
from requests import Session
import make_zip_file

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
        
        try:
            with open(os.path.join(os.getcwd(), "Vanilla Sounds.zip"), "rb") as zip: 
                files = {
                    "data": (None, json.dumps(data), "application/json"),
                    "file": ("Vanilla Sounds.zip", zip, "application/zip")
                }

                response = session.post("https://api.modrinth.com/v2/version", files=files)

                if (response.status_code == 413):
                    make_zip_file.make_zip(True)

                    data_gs = {
                            "name": f"Vanilla Sounds Minecraft {v}",
                            "version_number": "1.0.0",
                            "changelog": f"## Vanilla Sounds Resource Pack for Minecraft version {v}.",
                            "game_versions": [v],
                            "version_type": "release",
                            "loaders": ["minecraft"],
                            "featured": True,
                            "status": "listed",
                            "project_id": json.loads(session.get(os.environ["MODRINTH_VS_API"]).text)["id"],
                            "file_parts": ["game_sounds"],
                            "primary_file": "game_sounds",
                            "dependencies": []
                        }
                    
                    
                    with open(os.path.join(os.getcwd(), "Vanilla Sounds - Game Sounds.zip"), "rb") as gs: 
                        with open(os.path.join(os.getcwd(), "Vanilla Sounds - Music.zip"), "rb") as m: 
                            files = {
                                "data": (None, json.dumps(data_gs), "application/json"),
                                "game_sounds": ("Vanilla Sounds - Game Sounds.zip", gs, "application/zip"),
                            }

                            response = session.post("https://api.modrinth.com/v2/version", files=files)

                            if(response.status_code != 200):
                                print(f"An invalid response with status code {response.status_code} was sent to Modrinth while uploading both Vanilla Sounds - Game Sounds.zip and Vanilla Sounds - Music.zip files : {response.text}")
                                return
                            
                            data_m = {
                                "data" : (None, json.dumps({"file_parts": ["music"]}), "application/json")
                            }

                            files = {
                                **data_m,
                                "music": ("Vanilla Sounds - Music.zip", m, "application/zip")
                            }

                            version_id = response.json()["id"]
                            
                            response = session.post(f"https://api.modrinth.com/v2/version/{version_id}/file", files=files)
                            

                elif(response.status_code != 200):
                    print(f"An invalid response with status code {response.status_code} was sent to Modrinth while uploading Vanilla Sounds.zip file : {response.text}")
                
                print(f"Created a new version and uploaded Vanilla Sounds Resource Pack for Minecraft version {v}.")
        
        except Exception as e:
            if(os.path.exists(os.path.join(os.getcwd(), "Vanilla Sounds"))):
                print(f"An unexpected error occured while trying to create and upload a version of Vanilla Sounds Resource Pack on modrinth for Minecraft version {v} : {e}.")
            return
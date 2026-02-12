import os
from requests import Session
from bs4 import BeautifulSoup
import json
from PIL import Image
from packaging import version

def create_pack_png(v : str):
    if(version.parse(v) >= version.parse("1.6.1")):
        with Session as session:
            session.headers.update({"User-Agent": "Stilt34/Vanilla Sounds", "Authorization": os.environ["MODRINTH_VS_PAT"]})

            j = json.loads(session.get(os.environ["MODRINTH_VS_API"]).text)

            with open(os.path.join(os.getcwd(), "Vanilla Sounds", "pack.webp"), "wb") as f:
                f.write(session.get(j["icon_url"]).content)

            with Image.open(os.path.join(os.getcwd(), "Vanilla Sounds", "pack.webp"), "r") as icon:
                icon.save(os.path.join(os.getcwd(), "Vanilla Sounds", "pack.png"), "PNG")

            os.remove(os.path.join(os.getcwd(), "Vanilla Sounds", "pack.webp"))

            print(f"Created pack.png file for Minecraft version {v}.")
    else:
        print(f"Not creating pack.png file as Minecraft version {v} does not support resource packs.")
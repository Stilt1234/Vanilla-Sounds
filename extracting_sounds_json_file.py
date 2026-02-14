import os
import json
import shutil
import glob
import shutil
from packaging import version

def extract_sounds_json_file(v : str):
    v = version.parse(v)
    if(v >= version.parse("1.7.2")):
        hash = ""

        with open(glob.glob(os.getcwd()+"\\minecraft\\assets\\indexes\\*.json")[0], "r") as f:
            file : dict = json.load(f)
            for key, value in file["objects"].items():
                if(key.__contains__("sounds.json")):
                    hash = value["hash"]

        shutil.copy(os.path.join(os.getcwd(), "minecraft", "assets", "objects", f"{hash[:2]}", f"{hash}"), os.path.join(os.getcwd(), "Vanilla Sounds", "assets", "for_resourcepack_creators_sounds.json"))
        shutil.copy(os.path.join(os.getcwd(), "minecraft", "assets", "objects", f"{hash[:2]}", f"{hash}"), os.path.join(os.getcwd(), "Vanilla Sounds", "assets", "minecraft", "sounds.json"))
    else:
        print("No sounds.json file found as it is a version before 1.7.2 therefore skipping extracting sounds.json file.")
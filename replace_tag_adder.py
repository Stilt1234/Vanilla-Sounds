import os
import json

def add_replace_tag():
    try:
        with open(os.path.join(os.getcwd(), "Vanilla Sounds", "assets", "minecraft", "sounds.json"), "r+") as f:
            print("Loading and editing sounds.json file.")
            
            file : dict = json.load(f)
            for id, value in file.items():
                value["replace"]=True
            
            f.seek(0)
            json.dump(file, f, indent=4)
            f.truncate()

            print("File sounds.json has been successfully edited.")
    except:
        print("No sounds.json file found as it is a version before 1.7.2 therefore skipped adding replace tag.")
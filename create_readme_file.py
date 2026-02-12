import os
from packaging import version

def create_readme(v : str):
    if(not version.parse(v) < version.parse("1.7.2")):
        with open(os.path.join(os.getcwd(), "Vanilla Sounds", "assets", "minecraft", "WARNING-README.txt"), "w") as r:
            r.write("The minecraft/sounds.json file was edited by me (Stilt34).\nThe vanilla/default sounds.json file is located in assets/for_resourcepack_creators_sounds.json.")
    elif(version.parse(v) >= version.parse("1.6.1")):
        with open(os.path.join(os.getcwd(), "Vanilla Sounds", "assets", "minecraft", "README-PLS"), "w") as r:
            r.write(f"Minecraft version {v} does not support sounds.json file hence it is not there.\nBut you can edit or change the sound files just like resource packs.")
    else:
        with open(os.path.join(os.getcwd(), "Vanilla Sounds", "README-PLS.txt"), "w") as r:
            r.write(f"Minecraft version {v} does not support resource packs.\nThis folder's purpose is to provide sound files to old versions of minecraft for anyone who needs it.")
    print("Readme file has been created.")
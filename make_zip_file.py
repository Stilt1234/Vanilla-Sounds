import os
import shutil
import zipfile

def make_zip(split = False):
    if(not split):
        with zipfile.ZipFile(os.path.join(os.getcwd(), "Vanilla Sounds.zip"), 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
                for root, dirs, files in os.walk(os.path.join(os.getcwd(), "Vanilla Sounds")):
                    for file in files:
                        full_path = os.path.join(root, file)
                        rel_path = os.path.relpath(full_path, os.path.join(os.getcwd(), "Vanilla Sounds"))
                        zf.write(full_path, rel_path)
    
        print("Created Vanilla Sounds.zip file.")

    else:
        vs_assets = os.path.join(os.getcwd(), "Vanilla Sounds", "assets")

        shutil.move(os.path.join(vs_assets, "minecraft", "sounds", "music"), os.path.join(os.getcwd(), "Vanilla Sounds - Music", "assets", "minecraft", "sounds", "music"))
        shutil.copy(os.path.join(vs_assets, "minecraft", "sounds.json"), os.path.join(os.getcwd(), "Vanilla Sounds - Music", "assets", "minecraft", "sounds.json"))
        shutil.copy(os.path.join(vs_assets, "minecraft", "WARNING-README.txt"), os.path.join(os.getcwd(), "Vanilla Sounds - Music", "assets", "minecraft", "WARNING-README.txt"))
        shutil.copy(os.path.join(vs_assets, "for_resourcepack_creators_sounds.json"), os.path.join(os.getcwd(), "Vanilla Sounds - Music", "assets", "for_resourcpack_creators_sounds.json"))
        shutil.copy(os.path.join("Vanilla Sounds", "pack.mcmeta"), os.path.join(os.getcwd(), "Vanilla Sounds - Music", "pack.mcmeta"))
        shutil.copy(os.path.join("Vanilla Sounds", "pack.png"), os.path.join(os.getcwd(), "Vanilla Sounds - Music", "pack.png"))

        shutil.move(os.path.join(os.getcwd(), "Vanilla Sounds"), os.path.join(os.getcwd(), "Vanilla Sounds - Game Sounds"))

        with zipfile.ZipFile(os.path.join(os.getcwd(), "Vanilla Sounds - Game Sounds.zip"), 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
                for root, dirs, files in os.walk(os.path.join(os.getcwd(), "Vanilla Sounds - Game Sounds")):
                    for file in files:
                        full_path = os.path.join(root, file)
                        rel_path = os.path.relpath(full_path, os.path.join(os.getcwd(), "Vanilla Sounds - Game Sounds"))
                        zf.write(full_path, rel_path)
        
        with zipfile.ZipFile(os.path.join(os.getcwd(), "Vanilla Sounds - Music.zip"), 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
                for root, dirs, files in os.walk(os.path.join(os.getcwd(), "Vanilla Sounds - Music")):
                    for file in files:
                        full_path = os.path.join(root, file)
                        rel_path = os.path.relpath(full_path, os.path.join(os.getcwd(), "Vanilla Sounds - Music"))
                        zf.write(full_path, rel_path)
        
        print("Created both Vanilla Sounds - Game Sounds.zip and Vanilla Sounds - Music.zip files.")
import json, os, platform, shutil, sys

def extract_sounds():

    # This section should work on any system as well
    print("The OS is " + platform.system())
    MC_ASSETS = os.path.join(os.getcwd(), "minecraft", "assets")

    # Find the latest json index file
    MC_VERSION = os.listdir(MC_ASSETS+"/indexes/")[0]
    print("The latest found index.json file is " + MC_VERSION + "\n")

    OUTPUT_PATH = os.path.normpath(os.path.join(os.getcwd(), "Vanilla Sounds", "assets"))

    # These are unlikely to change
    MC_OBJECT_INDEX = f"{MC_ASSETS}/indexes/{MC_VERSION}"
    MC_OBJECTS_PATH = f"{MC_ASSETS}/objects"
    MC_SOUNDS = "minecraft/sounds/"

    with open(MC_OBJECT_INDEX, "r") as read_file:
        # Parse the JSON file into a dictionary
        data = json.load(read_file)

        # Find each line with MC_SOUNDS prefix
        if(not MC_OBJECT_INDEX.__contains__("legacy.json") and not MC_OBJECT_INDEX.__contains__("pre-1.6.json")):
            files = {k : v["hash"] for (k, v) in data["objects"].items() if k.startswith(MC_SOUNDS)}
        else:
            files = {k : v["hash"] for (k, v) in data["objects"].items() if k.endswith(".ogg")}
            OUTPUT_PATH = os.path.normpath(os.path.join(os.getcwd(), "Vanilla Sounds", "assets", "minecraft", "sounds"))
        # # Uncomment to extract all files.
        # files = {k : v["hash"] for (k, v) in data["objects"].items()}
        
        print("File extraction:")
        
        for fpath, fhash in files.items():
            # Ensure the paths are good to go for Windows with properly escaped backslashes in the string
            src_fpath = os.path.normpath(f"{MC_OBJECTS_PATH}/{fhash[:2]}/{fhash}")
            dest_fpath = os.path.normpath(f"{OUTPUT_PATH}/{fpath}")

            # Print current extracted file
            print(fpath)

            # Make any directories needed to put the output file into as Python expects
            os.makedirs(os.path.dirname(dest_fpath), exist_ok=True)

            # Copy the file
            shutil.copyfile(src_fpath, dest_fpath)
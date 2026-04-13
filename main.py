import minecraft_launcher_lib as mc
import os
import shutil
import create_pack_mcmeta_file
import update_repo
import extracting_mc_sounds as mc_sounds
import extracting_sounds_json_file as mc_sounds_json_file
import replace_tag_adder
import create_readme_file
import create_pack_png_file
import create_version_on_modrinth
import exclude_already_uploaded_versions_on_modrinth
import make_zip_file

print("Vanilla Sounds Resource Pack creation has been initialised.")

update_repo.update_repo_readme()
update_repo.update_repo_desc()

n = int(os.environ["VS_NUM_DOWNLOAD_RETRIES"])

list_to_install = []

for e in mc.utils.get_version_list():
    if(e.get("type") == "release"):
        list_to_install.append(e.get("id"))

print("Vanilla Sounds Resource Pack creation has been launched.")

print(f"No. of minecraft version download retries is {n}.")

for v in reversed(list_to_install):
    print("---------------------------------------------------------------------------------------------")
    if(exclude_already_uploaded_versions_on_modrinth.check_version_uploaded_already(v)):
        print("---------------------------------------------------------------------------------------------\n")
        continue
    print(f"Vanilla Sounds Resource Pack creation for Minecraft version {v} has been initiated.")
    try:
        shutil.rmtree(os.path.join(os.getcwd(), "minecraft"))
        print("Deleted folder - minecraft ...")
    except Exception as e:
        pass
    try:
        shutil.rmtree(os.path.join(os.getcwd(), "Vanilla Sounds"))
        print("Deleted folder - Vanilla Sounds ...")
    except Exception as e:
        pass
    try:
        os.remove(os.path.join(os.getcwd(), "Vanilla Sounds.zip"))
        print("Deleted file - Vanilla Sounds.zip ...")
    except Exception as e:
        pass
    try:
        os.remove("Vanilla Sounds.zip")
    except Exception as e:
        pass

    print(f"Installing minecraft version {v} ...")
    
    for i in range(0, n):
        try:
            mc.install.install_minecraft_version(v, os.path.join(os.getcwd(), "minecraft"))
            break
        except Exception as e:
            print(f"An unexpected error occured while trying to install minecraft version {v} : {e}.")
            print("Retrying download ...")
    
    if(not os.path.exists(os.path.join(os.getcwd(), "minecraft"))):
        print(f"Unable to download minecraft version {v}, hence skipping its resource pack creation.")
        print("---------------------------------------------------------------------------------------------\n")
        continue

    mc_sounds.extract_sounds()
    mc_sounds_json_file.extract_sounds_json_file(v)
    replace_tag_adder.add_replace_tag()
    create_readme_file.create_readme(v)
    create_pack_png_file.create_pack_png(v)
    create_pack_mcmeta_file.create_pack_file(v)

    # shutil.make_archive("Vanilla Sounds", "zip", os.path.join(os.getcwd(), "Vanilla Sounds"), ".")
    make_zip_file.make_zip()

    create_version_on_modrinth.create_version(v)

    print(f"Vanilla Sounds for minecraft version {v} has been done.")
    print("---------------------------------------------------------------------------------------------\n")

print("Vanilla Sounds Resource Pack creation for all the available Minecraft versions has been completed.")
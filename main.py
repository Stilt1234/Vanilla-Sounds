import minecraft_launcher_lib as mc
import os
import shutil
import create_pack_mcmeta_file
from packaging import version
import update_repo
import extracting_mc_sounds as mc_sounds
import extracting_sounds_json_file as mc_sounds_json_file
import replace_tag_adder
import create_readme_file
import create_pack_png_file
import create_version_on_modrinth
import exclude_already_uploaded_versions_on_modrinth

update_repo.update_repo_readme()
update_repo.update_repo_desc()

list_to_install = []

for e in mc.utils.get_version_list():
    #if(e.get("type") == "release" and version.parse(e.get("id")) >= next(iter(create_pack_mcmeta_file.v_pf)) and float(create_pack_mcmeta_file.get_pack_format(e.get("id"))) > 0.0):
    if(e.get("type") == "release"):
        list_to_install.append(e.get("id"))

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
    mc.install.install_minecraft_version(v, os.path.join(os.getcwd(), "minecraft"))

    mc_sounds.extract_sounds()
    mc_sounds_json_file.extract_sounds_json_file()
    replace_tag_adder.add_replace_tag()
    create_readme_file.create_readme(v)
    create_pack_png_file.create_pack_png(v)
    create_pack_mcmeta_file.create_pack_file(v)

    shutil.make_archive("Vanilla Sounds", "zip", os.path.join(os.getcwd(), "Vanilla Sounds"), ".")

    create_version_on_modrinth.create_version(v)

    print(f"Vanilla Sounds for minecraft version {v} has been successfully created.")
    print("---------------------------------------------------------------------------------------------\n")

print("Vanilla Sounds Resource Pack creation for all the available Minecraft versions has been completed.")
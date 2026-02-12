import os
from requests import Session
import json
from git import Repo
import github
from requests import Session

def update_repo_readme():
    with Repo(os.getcwd()) as repo:

        with open(os.path.join(os.getcwd(), "README.md"), "w") as f:
            with Session() as s:
                s.headers.update({"User-Agent": "Stilt34/Vanilla Sounds", "Authorization": os.environ["MODRINTH_VS_PAT"]})
                
                f.write(json.loads(s.get(os.environ["MODRINTH_VS_API"]).text)["body"])

        repo.index.add(os.path.join(os.getcwd(), "README.md"))
        repo.index.commit("Updated README.md file.")

        auth_url = f"https://x-access-token:{os.environ["GITHUB_TOKEN"]}@github.com/Stilt1234/Vanilla-Sounds"

        try:
            remote = repo.create_remote("Vanilla-Sounds", "https://github.com/Stilt1234/Vanilla-Sounds", auth_url)
        except:
            remote = repo.remote("Vanilla-Sounds")
            remote.set_url(auth_url)

        remote.push(refspec=f"{repo.active_branch.name}:{repo.active_branch.name}", set_upstream=True)

        print("Updated README.md file in Github repository.")

def update_repo_desc():
    with Session() as s:
        
        s.headers.update({"User-Agent": "Stilt34/Vanilla Sounds", "Authorization": os.environ["MODRINTH_VS_PAT"]})
        
        with github.Github(auth=github.Auth.Token(os.environ["GITHUB_TOKEN"])) as g:
            
            g.get_repo("Stilt1234/Vanilla-Sounds").edit(description=json.loads(s.get(os.environ["MODRINTH_VS_API"]).text)["description"])
           
            print("Updated description of Github repository.")
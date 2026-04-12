import os
from packaging import version
import json
import minecraft_launcher_lib as mc
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

s = requests.Session()
s.headers.update({"User-Agent": "Stilt34/Vanilla Sounds", "Authorization": os.environ["MODRINTH_VS_PAT"]})
page = s.get("https://minecraft.wiki/w/Pack_format")
soup = BeautifulSoup(page.text, "html.parser")

table = soup.body.find("div", attrs={"id" : "content"}).find("div", attrs={"id" : "bodyContent"}).find("div", attrs={"id" : "mw-content-text"}).find_all("caption")[2].parent

v = table.find_all("th", attrs={"id" : "v"})
pf = table.find_all("th", attrs={"id" : "pack-format"})

v_pf = {}

for e in range(v.__len__()):
    if(v[e].__contains__(" – ")):
        f = v[e].text.split(" – ")

        v_pf.setdefault(version.parse(f[0]), pf[e].text)
        v_pf.setdefault(version.parse(f[1]), pf[e].text)
    else:
        v_pf.setdefault(version.parse(v[e].text), pf[e].text)

pack_format = 0

def get_pack_format(v : str) -> str:
    v = version.parse(v)
    
    try:
        return v_pf[v]
    except:
        for ve, f in v_pf.items():
            if (ve > v and v > next(iter(v_pf)) and v < next(reversed(v_pf))):
                return f
        
        return get_pack_format_third_table(v) if not v < version.parse("1.6.1") else "-1"

def get_pack_format_third_table(v : str) -> str:
    driver = webdriver.Chrome()
    driver.get("https://minecraft.wiki/w/Pack_format")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    button = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//th[contains(., 'Client version')]")))

    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)

    for i in range(3):
        driver.execute_script("arguments[0].click();", button)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    table = soup.select("table.wikitable.sortable.jquery-tablesorter").pop()
    try:
        return table.find("a", string=f"Java Edition {v}").find_parent("tr").find_all("td")[1].text
    except:
        return get_pack_format_website(v)

def get_pack_format_website(v : str):
    s = requests.Session()
    s.headers.update({"User-Agent": "Stilt34/Vanilla Sounds", "Authorization": os.environ["MODRINTH_VS_PAT"]})
    page = s.get(f"https://minecraft.wiki/w/Java_Edition_{v}")
    soup = BeautifulSoup(page.text, "html.parser")
    try:
        return soup.find("a", string="Resource pack format").parent.parent.parent.find("td").text
    except:
        return "0"

def create_pack_file(v : str):
    ext = "mcmeta"
    format = get_pack_format(v)

    if(format == "-1"):
        print(f"Minecraft version {v} does not support Resource Packs hence using -1 as pack format so that it can be uploaded to Modrinth.")
        ext = "txt"

    if(format == "0"):
        print("Pack format not found for the given version.")
        return

    with open(os.path.join(os.getcwd(), "Vanilla Sounds", f"pack.{ext}"), "w") as f:
        desc = json.loads((s.get(os.environ["MODRINTH_VS_API"])).text)["description"]
        
        j = {
            "pack": {
                "description": desc,
                "pack_format": format,
                }
            }

        j_1_21_9 = {
            "pack": {
                "description": desc,
                "min_format" : format,
                "max_format" : format
                }
            }
        
        if(float(format) >= 69.0):
            f.write(json.dumps(j_1_21_9, indent=4))
        else:
            f.write(json.dumps(j, indent=4))
    
    print(f"Created pack.{ext} file for Minecraft version {v}.")
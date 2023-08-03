import wget
import json
from random import randrange

from time import sleep

def getHtml(link_path, html_path):
    with open(link_path, "r", encoding="utf-8") as file: links = json.load(file)

    for i in range(len(links)):
        wget.download(url=links[i]["link"], out=html_path + links[i]["id"] + ".html")
        sleep(0.3 + randrange(2, 8)/10)

if __name__ == "__main__": pass
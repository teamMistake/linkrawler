from selenium import webdriver
from selenium.webdriver.common.by import By

import json
from random import randrange
from datetime import datetime
from time import sleep

from config import category_dict, KEYWORD_XPATH, CATEGORY_XPATH

options = webdriver.ChromeOptions()
options.add_argument('window-size=1920,1080')

def getLinkByKeyword(keyword, pages):
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)

    result = []

    for page in range(pages):
        driver.get(url="https://kin.naver.com/search/list.naver?query=" + keyword + "&page=" + str(page + 1))

        q_list = driver.find_elements(By.XPATH, KEYWORD_XPATH)

        for q in q_list:
            result.append(
                {
                    "id": q.get_attribute("href").split("&docId=")[-1].split("&")[0],
                    "title": q.text,
                    "link": q.get_attribute("href")
                }
            )
        sleep(0.3 + randrange(2, 8)/10)

    link_path = "./link/keyword_link/" + datetime.today().strftime("%y%m%d.%H%M%S.") + keyword + "link.json"

    with open(link_path, 'w', encoding='utf-8') as file:
        json.dump(result, file, ensure_ascii=False, indent=2)

    return link_path, keyword

    driver.close()

def getLinkByCategory(category, pages):
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)

    result = []

    for page in range(pages):
        driver.get(url="https://kin.naver.com/qna/kinupList.naver?dirId=" + str(category_dict[category]) + "&page=" + str(page + 1))

        q_list = driver.find_elements(By.XPATH, CATEGORY_XPATH)

        for q in q_list:
            result.append(
                {
                    "id": q.get_attribute("href").split("&docId=")[-1].split("&")[0],
                    "title": q.text,
                    "link": q.get_attribute("href")
                }
            )
        sleep(0.3 + (randrange(2, 8) / 10))

    link_path = "./link/category_link/" + datetime.today().strftime("%y%m%d.%H%M%S.") + category + ".json"

    with open(link_path, 'w', encoding='utf-8') as file:
        json.dump(result, file, ensure_ascii=False, indent=2)

    return link_path, category

    driver.close()

if __name__ == "__main__":
    getLinkByCategory(1, 5)
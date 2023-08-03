from selenium import webdriver
from selenium.webdriver.common.by import By

import json
from random import randrange
from time import sleep

SEARCH_XPATH = '//*[@id="s_content"]/div[3]/ul/li[*]/dl/dt/a'

options = webdriver.ChromeOptions()
options.add_argument('window-size=1920,1080')

def getLink(keyword, pages):
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)

    result = []

    for page in range(pages):
        driver.get(url="https://kin.naver.com/search/list.naver?query=" + keyword + "&page=" + str(page + 1))

        q_list = driver.find_elements(By.XPATH, SEARCH_XPATH)

        for q in q_list:
            result.append(
                {
                    "id": q.get_attribute("href").split("&docId=")[-1].split("&")[0],
                    "title": q.text,
                    "link": q.get_attribute("href")
                }
            )
        sleep(0.3 + randrange(2, 8)/10)

    with open("./link/link.json", 'w', encoding='utf-8') as file:
        json.dump(result, file, ensure_ascii=False, indent=2)

    driver.close()

if __name__ == "__main__": pass
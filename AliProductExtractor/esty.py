
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from PIL import Image

import re
import time
import os
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from typing import TypedDict

from scrape_ali_express import AliExpress
import requests


def getFileUrl(url, loc):
    URL = url
    picture_req = requests.get(URL)
    if picture_req.status_code == 200:
        with open(loc, 'wb') as f:
            f.write(picture_req.content)
        basewidth = 2024
        img = Image.open(loc)
        os.remove(loc)
        img = img.resize((basewidth, basewidth), Image.ANTIALIAS)
        img.save(loc)
    return loc


class AExpressToEtsy:
    username = ""
    password = ""
    uid = "0"

    def __init__(self, username, password, uid="0") -> None:
        self.username = username
        self.password = password
        self.uid = uid

    def product_uploader(self, data: AliExpress = None, driver: WebDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))):
        driver.get("https://www.etsy.com/")

        WebDriverWait(driver, 300).until(EC.visibility_of_element_located(
            (By.XPATH, "/html/body/div[2]/header/div[3]/nav/ul/li[1]/button")))

        driver.find_element(
            By.XPATH, "/html/body/div[2]/header/div[3]/nav/ul/li[1]/button").click()
        print("click")

        WebDriverWait(driver, 300).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '#join_neu_email_field')))
        driver.find_element(By.CSS_SELECTOR, '#join_neu_password_field').send_keys(
            self.password)

        WebDriverWait(driver, 300).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '#join_neu_password_field')))
        driver.find_element(
            By.CSS_SELECTOR, '#join_neu_email_field').send_keys(self.username)

        print("sign in")
        WebDriverWait(driver, 300).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "button.wt-width-full:nth-child(1)")))
        driver.find_element(
            By.CSS_SELECTOR, 'button.wt-width-full:nth-child(1)').click()
        WebDriverWait(driver, 300).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#gnav-header-inner > div.wt-flex-shrink-xs-0 > nav > ul > li:nth-child(4) > div > button")))
        driver.get(
            "https://www.etsy.com/your/shops/me/onboarding/listings/create")
        # /***ADDing Images**/
        cwd = Path.cwd()

        for img in data.images:
            print("~img")

            location = getFileUrl(img, os.path.abspath(
                f"{self.uid}_file_name.png"))
            WebDriverWait(driver, 300).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#listing-edit-image-upload")))
            print("location ,"+location)
            driver.find_element(
                By.CSS_SELECTOR, '#listing-edit-image-upload').send_keys(location)
            print("img")
            os.remove(location)
            # os.remove(location)


if __name__ == "__main__":
    os.environ['WDM_LOG_LEVEL'] = '0'
    os.environ['WDM_LOCAL'] = '1'
    url = 'https://www.aliexpress.us/item/3256804136971215.html'

    ali = AliExpress()
    ali.images = ["https://ae01.alicdn.com/kf/S2f4257ea5ff745918980d97f5c7bb8c7G/Dec-Super-Sale-Xiaomi-RedmiBook-Pro-15-2022-Laptop-Ryzen-R7-6800H-R5-6600H-AMD.png",
                  "https://ae01.alicdn.com/kf/S2f4257ea5ff745918980d97f5c7bb8c7G/Dec-Super-Sale-Xiaomi-RedmiBook-Pro-15-2022-Laptop-Ryzen-R7-6800H-R5-6600H-AMD.png"]
    data = AExpressToEtsy(username="locivej993@khaxan.com",
                          password="dL6ykWgp83S").product_uploader(ali)
    print(data)

# locivej993@khaxan.com
# dL6ykWgp83S

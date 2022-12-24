
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from PIL import Image
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


import re
import time
import os
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from typing import TypedDict

from scrape_ali_express import AliExpress, aliExtractor
import requests


def getLocalImageUrl(url, loc=''):
    URL = url
    picture_req = requests.get(URL)
    fname = loc
    if "Content-Disposition" in picture_req.headers.keys():
        fname = re.findall(
            "filename=(.+)", picture_req.headers["Content-Disposition"])[0]
    else:
        fname = url.split("/")[-1]

    # print("fname", fname)
    download = os.path.abspath(fname)
    if picture_req.status_code == 200:
        with open(download, 'wb') as f:
            f.write(picture_req.content)
        basewidth = 2024
        img = Image.open(download)
        os.remove(download)
        img = img.resize((basewidth, basewidth), Image.ANTIALIAS)
        img.save(download)
    return download


def getLocalVideoUrl(url, loc=''):
    URL = url
    video_req = requests.get(URL)
    fname = loc
    if "Content-Disposition" in video_req.headers.keys():
        fname = re.findall(
            "filename=(.+)", video_req.headers["Content-Disposition"])[0]
    else:
        fname = url.split("/")[-1]

    # print("fname", fname)
    download = os.path.abspath(fname)
    if video_req.status_code == 200:
        with open(download, 'wb') as f:
            f.write(video_req.content)
        ffmpeg_extract_subclip(download, 0, 12, targetname=f"_{fname}")
        os.remove(download)

    return os.path.abspath(f"_{fname}")


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
            location = getLocalImageUrl(img, os.path.abspath(
                f"{self.uid}_file_name.png"))
            WebDriverWait(driver, 300).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#listing-edit-image-upload")))
            driver.find_element(
                By.CSS_SELECTOR, '#listing-edit-image-upload').send_keys(location)

            os.remove(location)

        WebDriverWait(driver, 300).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#title-input")))
        driver.find_element(
            By.CSS_SELECTOR, '#title-input').send_keys(ali.title)

        WebDriverWait(driver, 300).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#taxonomy-search")))
        driver.find_element(
            By.CSS_SELECTOR, '#taxonomy-search').send_keys(ali.title)

        WebDriverWait(driver, 300).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#taxonomy-search-results-option-0")))
        driver.find_element(
            By.CSS_SELECTOR, '#taxonomy-search-results-option-0').click()

        WebDriverWait(driver, 300).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#who_made-input")))
        driver.find_element(
            By.CSS_SELECTOR, '#who_made-input').click()
        driver.find_element(
            By.CSS_SELECTOR, '#who_made-input > optgroup > option:nth-child(3)').click()
        driver.find_element(
            By.CSS_SELECTOR, '#description-text-area-input').send_keys(ali.description)
        driver.find_element(
            By.CSS_SELECTOR, '#description-text-area-input').send_keys(ali.price)
        driver.find_element(
            By.CSS_SELECTOR, '#variations-component > div > div > div > div > span').click()
        WebDriverWait(driver, 300).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#wt-modal-container > div.wt-overlay.wt-overlay--will-animate.wt-overlay--large > div > div:nth-child(2) > div > div > label > select")))
        driver.find_element(
            By.CSS_SELECTOR, '#wt-modal-container > div.wt-overlay.wt-overlay--will-animate.wt-overlay--large > div > div:nth-child(2) > div > div > label > select').click()
        WebDriverWait(driver, 300).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#wt-modal-container > div.wt-overlay.wt-overlay--will-animate.wt-overlay--large > div > div:nth-child(2) > div > div > label > select > optgroup:nth-child(3)")))
        driver.find_element(
            By.CSS_SELECTOR, '#wt-modal-container > div.wt-overlay.wt-overlay--will-animate.wt-overlay--large > div > div:nth-child(2) > div > div > label > select > optgroup:nth-child(3)').click()
        WebDriverWait(driver, 300).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#undefined-input")))
        driver.find_element(
            By.CSS_SELECTOR, '#undefined-input').send_keys(ali.variant_title)

        driver.find_element(
            By.CSS_SELECTOR, ' #wt-modal-container > div.wt-overlay.wt-overlay--will-animate.wt-overlay--large > div > div:nth-child(2) > div > div > div > div.input-group-btn > button').click()
        for variant in ali.variant:
            WebDriverWait(driver, 300).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#undefined-input")))
            driver.find_element(
                By.CSS_SELECTOR, '#undefined-input').send_keys(variant["name"])
            driver.find_element(
                By.CSS_SELECTOR, '#wt-modal-container > div.wt-overlay.wt-overlay--will-animate.wt-overlay--large > div > div:nth-child(2) > div:nth-child(2) > div.col-sm-6.col-offset-md-1.col-lg-5.col-offset-lg-2.mt-xs-2.mt-sm-0 > div:nth-child(1) > div > div.input-group-btn > button').click()
        driver.find_element(
            By.CSS_SELECTOR, "#wt-modal-container > div.wt-overlay.wt-overlay--will-animate.wt-overlay--large > div > div:nth-child(2) > div:nth-child(2) > div.col-sm-6.col-md-5 > div.mt-xs-4 > div:nth-child(1) > label > input").click()

        driver.find_element(
            By.CSS_SELECTOR, '#save').click()

        if (ali.video):
            locVideo = getLocalVideoUrl(ali.video)
            WebDriverWait(driver, 300).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#listing-video-upload-button")))
            video = driver.find_element(
                By.CSS_SELECTOR, '#listing-video-upload-button')
            print(locVideo)
            video.send_keys(locVideo)
            print("video")
            # os.remove(locVideo)


if __name__ == "__main__":
    os.environ['WDM_LOG_LEVEL'] = '0'
    os.environ['WDM_LOCAL'] = '1'
    # url = 'https://www.aliexpress.us/item/3256804136971215.html'
    url = 'https://www.aliexpress.us/item/3256804136971215.html'

    [ali, driver] = aliExtractor(url)

    # ali = {'images': ["https://ae01.alicdn.com/kf/S2f4257ea5ff745918980d97f5c7bb8c7G/Dec-Super-Sale-Xiaomi-RedmiBook-Pro-15-2022-Laptop-Ryzen-R7-6800H-R5-6600H-AMD.png",
    #                   "https://ae01.alicdn.com/kf/S2f4257ea5ff745918980d97f5c7bb8c7G/Dec-Super-Sale-Xiaomi-RedmiBook-Pro-15-2022-Laptop-Ryzen-R7-6800H-R5-6600H-AMD.png"]}
    ali.images = ["https://ae01.alicdn.com/kf/S2f4257ea5ff745918980d97f5c7bb8c7G/Dec-Super-Sale-Xiaomi-RedmiBook-Pro-15-2022-Laptop-Ryzen-R7-6800H-R5-6600H-AMD.png",
                  "https://ae01.alicdn.com/kf/S2f4257ea5ff745918980d97f5c7bb8c7G/Dec-Super-Sale-Xiaomi-RedmiBook-Pro-15-2022-Laptop-Ryzen-R7-6800H-R5-6600H-AMD.png"]
    ali.video = "https://video.aliexpress-media.com/play/u/ae_sg_item/17381167788/p/1/e/6/t/10301/1100063275440.mp4"
    data = AExpressToEtsy(username="locivej993@khaxan.com",
                          password="dL6ykWgp83S").product_uploader(ali)
    print(data)

    # getFileUrl(ali, '0.png')


# locivej993@khaxan.com
# dL6ykWgp83S

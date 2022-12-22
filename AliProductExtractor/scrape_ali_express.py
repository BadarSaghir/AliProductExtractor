from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import re
import time
import os
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from typing import TypedDict
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")  # linux only
chrome_options.add_argument("--headless")

USA_SEARCH = '?spm=a2g0o.detail.0.0.4e3048beiFDUoE&gps-id=pcDetailBottomMoreThisSeller&scm=1007.13339.291025.0&scm_id=1007.13339.291025.0&scm-url=1007.13339.291025.0&pvid=605d10f0-cf77-4b61-a51c-e4eaff32a7b2&_t=gps-id%3ApcDetailBottomMoreThisSeller%2Cscm-url%3A1007.13339.291025.0%2Cpvid%3A605d10f0-cf77-4b61-a51c-e4eaff32a7b2%2Ctpp_buckets%3A668%232846%238107%231934&pdp_ext_f=%7B"sku_id"%3A"12000025917204937"%2C"sceneId"%3A"3339"%7D&pdp_npi=2%40dis%21PKR%217770.36%215439.25%21%21%21%21%21%402101f6b516712770955781365e5cbb%2112000025917204937%21rec&gatewayAdapt=glo2usa4itemAdapt&_randl_shipto=US'


class TextMatch(object):
    def __init__(self, locator, regexp):
        self.locator = locator
        self.regexp = regexp

    def __call__(self, driver):
        element = EC.presence_of_element_located(self.locator)(driver)
        # print(element.text)
        # print(re.search(self.regexp, element.text))
        return element and re.search(self.regexp, element.text)


class Variant(TypedDict):
    name: str
    price: str


class AliExpress:
    variant: list[Variant] = []
    title: str = ""
    description: str
    video: str
    images: list[str] = []
    specification: list[dict] = []
    shipping = ''

    def __init__(self) -> None:
        self.description = ''

    def __repr__(self) -> str:
        return f'{self.variant}, {self.title}'

    def __str__(self) -> str:
        return f'{"{"}\nvariant:{self.variant}, \ndescriptionL{self.description}, \nvideo:{ self.video }, \nimages:{self.images} , \ntitle:{self.title},\n\n specification:{self.specification} {"}"}'


def aliExtractor(url, browser: WebDriver = webdriver.Chrome(options=chrome_options,
                                                            service=Service(ChromeDriverManager().install())), default_location=True) -> AliExpress:
    # print("started....")
    pattern_price = r"^[^-]*$"
    aliExpressData = AliExpress()
    pattern = r"^https://www?\.?aliexpress\.us/item/\d+\.html\??.*$"

    if re.match(pattern, url):
        pass
    else:
        print("URL does not match the pattern. Please Provide Ali express product url")
        return aliExpressData
    search = USA_SEARCH
    if default_location:
        pass
    else:
        search = ''

    browser.get(
        f'{url+search}')

    WebDriverWait(browser, 300).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".sku-property-item")))
    WebDriverWait(browser, 300).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".product-title-text")))
    els = browser.find_elements(By.CSS_SELECTOR, '.sku-property-item')
    title = browser.find_element(By.CSS_SELECTOR, '.product-title-text').text
    aliExpressData.title = title
    WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.dynamic-shipping-titleLayout span span')))
    shipping = browser.find_element(
        By.CSS_SELECTOR, ".dynamic-shipping-titleLayout span span")
    aliExpressData.shipping = shipping.text
    for e in els:
        e.click()
        # time.sleep(5)
        WebDriverWait(browser, 300).until(TextMatch(
            (By.CSS_SELECTOR, ".product-price-current span"), pattern_price))
        price = browser.find_element(
            By.CSS_SELECTOR, '.product-price-current')
        WebDriverWait(browser, 300).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".sku-title-value")))
        _name = browser.find_element(
            By.CSS_SELECTOR, '.sku-title-value')
        variant: Variant = {
            'price': price.text.split("$")[1],
            'name': _name.text
        }
        aliExpressData.variant.append(variant)
        e.click()

    for i in range(0, 2):
        browser.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.PAGE_DOWN)
    WebDriverWait(browser, 300).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".detailmodule_text")))
    details = browser.find_elements(
        By.CSS_SELECTOR, '.detailmodule_text')
    for detail in details:
        aliExpressData.description = aliExpressData.description+detail.text
    for i in range(0, 2):
        browser.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.PAGE_UP)

    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".video-container video")))
        video = browser.find_element(
            By.CSS_SELECTOR, '.video-container video').get_attribute('src')
        aliExpressData.video = video
        # print(aliExpressData)
        # print('\n'+video)

    except e:
        pass
        # print("no video ", e)

    WebDriverWait(browser, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".images-view-wrap")))
    imagesLi = browser.find_elements(
        By.CSS_SELECTOR, '.images-view-wrap li')
    for li in imagesLi:
        img = li.find_elements(
            By.CSS_SELECTOR, 'div > *')
        length = len(img)
        if length < 2:
            aliExpressData.images.append(
                img[0].get_attribute("src").split("_")[0])

    WebDriverWait(browser, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#product-detail > div.product-detail-tab > div > div.detail-tab-bar > ul > li:nth-child(3)')))
    browser.find_element(
        By.CSS_SELECTOR, '#product-detail > div.product-detail-tab > div > div.detail-tab-bar > ul > li:nth-child(3)').click()
    WebDriverWait(browser, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '.product-prop')))

    specList = browser.find_elements(
        By.CSS_SELECTOR, '.product-prop')

    for spec in specList:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.property-title')))
        title = spec.find_element(By.CSS_SELECTOR, ".property-title")
        WebDriverWait(browser, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.property-desc')))
        value = spec.find_element(
            By.CSS_SELECTOR, ".property-desc")
        aliExpressData.specification.append(
            {title.text.split(':')[0]: value.text})

    # aliExpressData.video = video
    browser.close()
    return aliExpressData


if __name__ == "__main__":
    os.environ['WDM_LOG_LEVEL'] = '0'
    os.environ['WDM_LOCAL'] = '1'
    url = 'https://www.aliexpress.us/item/3256804136971215.html'

    data = aliExtractor(url)

    print(data)

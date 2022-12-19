from AliProductExtractor.scrape_ali_express import aliExtractor
import os

if __name__ == "__main__":
    os.environ['WDM_LOG_LEVEL'] = '0'
    os.environ['WDM_LOCAL'] = '1'
    url = 'https://www.aliexpress.us/item/3256804136971215.html'

    data = aliExtractor(url)

    print(data)

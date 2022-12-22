from distutils.core import setup
# Ali Express Product Extractor

description = """
    
[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)


## Features

- Extract products from Ali Express
- Easy to use



## Tech

Dillinger uses a number of open source projects to work properly:

- [python] - Programing Language!
- [vscode] -  text editor
- [selenium] - Markdown parser done right. Fast and easy to extend.



## Installation


Install the dependencies and devDependencies and start the server.

```sh
pip install AliProductExtractor
```



## Usage example


```python

from AliProductExtractor.scrape_ali_express import aliExtractor
import os

if __name__ == "__main__":
    os.environ['WDM_LOG_LEVEL'] = '0'
    os.environ['WDM_LOCAL'] = '1'
    url = 'https://www.aliexpress.us/item/3256804136971215.html'

    data = aliExtractor(url)

    print(data)

```
    
    """

setup(

    name='AliProductExtractor',
    packages=['AliProductExtractor'],
    version='0.8',
    license='MIT',
    description="It will get the product data from ali express",
    long_description=description,
    author='Sardar Badar Saghir',
    author_email='dataentrybadar@gmail.com',
    url='https://github.com/BadarSaghir/AliProductExtractor',
    download_url='https://github.com/BadarSaghir/AliProductExtractor/releases/download/0.1/AliProductExtractor.zip',
    # Keywords that define your package best
    keywords=['Ali express', 'Ali  express product',
              'Ali express product scraper', 'scraper Ali express', 'scraper', 'extractor'],
    install_requires=[
        'selenium==4.0.0a1',
        'webdriver_manager==3.8.5',
        ''

    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.10',
    ],
)

# Ali Express Product Extractor

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

Dillinger requires [Node.js](https://nodejs.org/) v10+ to run.

Install the dependencies and devDependencies and start the server.

pip install aliproductextractor




## Usage example



from AliProductExtractor.scrape_ali_express import aliExtractor
import os

if __name__ == "__main__":
    os.environ['WDM_LOG_LEVEL'] = '0'
    os.environ['WDM_LOCAL'] = '1'
    url = 'https://www.aliexpress.us/item/3256804136971215.html'

    data = aliExtractor(url)

    print(data)





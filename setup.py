from distutils.core import setup
setup(

    name='AliProductExtractor',
    packages=['AliProductExtractor'],
    version='0.1',
    license='MIT',
    description='It will get the product data from ali express',
    author='Sardar Badar Saghir',
    author_email='dataentrybadar@gmail.com',
    url='https://github.com/BadarSaghir/AliProductExtractor',
    download_url='https://github.com/BadarSaghir/AliProductExtractor/releases/download/0.1/AliProductExtractor.zip',
    # Keywords that define your package best
    keywords=['Ali express', 'Ali  express product',
              'Ali express product scraper', 'scraper Ali express', 'scraper', 'extractor'],
    install_requires=[
        'selenium==4.0.0a1',
        'webdriver_manager==3.8.5'

    ],
    classifiers=[
        'Development Status :: 5 - stable',
        'Intended Audience :: Developers, Marketers, Scrapers',
        'Topic :: Software Development :: Scraping',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10.5',
    ],
)

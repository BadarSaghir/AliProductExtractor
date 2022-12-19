from distutils.core import setup
setup(

    name='AliProductExtractor',
    packages=['AliProductExtractor'],
    version='0.1',
    license='MIT',
    # Give a short description about your library
    description='It will get the product dat',
    author='YOUR NAME',  # Type in your name
    author_email='your.email@domain.com',  # Type in your E-Mail
    # Provide either the link to your github or to your website
    url='https://github.com/user/reponame',
    # I explain this later on
    download_url='https://github.com/user/reponame/archive/v_01.tar.gz',
    # Keywords that define your package best
    keywords=['Ali express', 'Ali  express product',
              'Ali express product scraper', 'scraper Ali express'],
    install_requires=[
        'selenium==4.0.0a1',
        'webdriver_manager==3.8.5'

    ],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 5 - stable',
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Scraping',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.10.5',
    ],
)

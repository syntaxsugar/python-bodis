from setuptools import setup

setup(
    name='python-bodis',
    version='0.1.1',
    packages=['bodis_api'],
    url='',
    license='',
    author='Jaromir Fojtu',
    author_email='jaromir.fojtu@gmail.com',
    description='bodis.com API implementation',
    install_requires=[
        'setuptools',
        'BeautifulSoup==3.2.1',
    ]
)
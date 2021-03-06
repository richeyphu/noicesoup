from setuptools import setup

setup(
    name='noicesoup',
    version='0.1.0',
    description='A simple python package for scraping and downloading images from Google',
    url='https://github.com/richeyphu/noicesoup',
    author='Unn&Phu',
    author_email='example@gmail.com',
    license='MIT',
    packages=['noicesoup'],
    install_requires=['requests', 'bs4', 'selenium'],
)

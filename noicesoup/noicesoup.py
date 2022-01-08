"""
A simple python package for scraping and downloading images from Google

Usage:
    $ noicesoup.py [-h] -k KEYWORD [-cd CHROMEDRIVER]

NOTE: Default webdriver is Chrome in relative path "chromedriver"
Images will be saved in "downloads/<keyword>"

This package is currently under development...
"""

from selenium import webdriver
from bs4 import BeautifulSoup
from pathlib import Path

import time
import urllib.request
import os
import argparse


def get_driver():
    path = 'chromedriver'
    driver = webdriver.Chrome(executable_path=path)
    driver.get(f'https://www.google.com/search?q={keyword}&tbm=isch')

    for i in range(0, 7):
        driver.execute_script('window.scrollBy(0,document.body.scrollHeight)')
        try:
            # for clicking show more results button
            driver.find_element(
                '//*[@id="islmp"]/div/div/div/div/div[2]/div[2]/input').click()
        except Exception:
            pass
        time.sleep(3)
    return driver


def download_images(driver):
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    img_tags = soup.find_all('img', class_='rg_i')
    length = len(img_tags)

    # get pics and download
    for i, v in enumerate(img_tags):
        try:
            loading_bar(i + 1, length)
            urllib.request.urlretrieve(
                v['src'], f"{downloads_path}/{keyword}/{str(i + 1)}.jpg")
        except Exception:
            pass
    print()


def loading_bar(n, l):
    print("\rDownloading : {} ({:.2f}%)".format(
        "█" * round(n / l * 100 / 2), n / l * 100), end="")


def create_dir():
    try:
        os.makedirs(f'{downloads_path}/{keyword}')
    except Exception as e:
        print(e)


def main():
    global keyword
    global driver_path
    global downloads_path

    downloads_path = os.path.join(
        str(Path.home()), 'Downloads', 'noicesoup_dl')

    parser = argparse.ArgumentParser(
        description='A simple python package for scraping and downloading images from Google')
    parser.add_argument('-k', '--keyword',
                        help='Input search keyword', required=True)
    parser.add_argument('-cd', '--chromedriver',
                        help='Input ChromeDriver path', default="chromedriver")
    args = parser.parse_args()

    keyword = args.keyword
    driver_path = args.chromedriver
    print(f'{keyword=}')
    create_dir()
    driver = get_driver()
    print('=' * os.get_terminal_size().columns)
    download_images(driver)
    print('=' * os.get_terminal_size().columns)
    print('Done!')


if "__main__" == __name__:
    main()

# coding: utf-8

import logging
import sys
from selenium import webdriver
from .outputs import FileOutput

logging.basicConfig(stream=sys.stdout,
                    level=logging.INFO,
                    format='%(message)s')


class Scraper(object):

    def __init__(self, urls, driver=None, output=None):
        if isinstance(urls, str):
            urls = [urls]

        self.urls = urls

        if output is None:
            output = FileOutput()
        self.output = output

        if driver is None:
            driver = webdriver.Chrome()

        self.driver = driver

    def __enter__(self):
        self.driver.start_client()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.close()

    def get_contents(self):
        for url in self.urls:
            logging.info('Getting content from url {0}'.format(url))

            self.driver.get(url)
            self.driver.implicitly_wait(1)
            file_name = url.split('/')[-1]
            self.output.write(file_name, self.driver.page_source)

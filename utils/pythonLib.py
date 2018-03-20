import requests
from bs4 import BeautifulSoup
import json
import os
import csv


def request_fun(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html5lib')
    return soup


def read_txt_file(filename):
    keywords_file = open(filename, "r")
    keywords = keywords_file.readlines()
    return [keyword.strip().replace('\n', '') for keyword in keywords]

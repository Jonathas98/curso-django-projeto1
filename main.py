import requests
from bs4 import BeautifulSoup

requests = requests
content = requests.content

site = requests.BeautifulSoup(content, 'html.parser')

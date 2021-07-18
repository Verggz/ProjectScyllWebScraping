from bs4 import BeautifulSoup
import requests

def GetItemByUrl(url):
    req = requests.get(url)

    soup = BeautifulSoup(req.text,'lxml')

def GetItemStatsByUrl(url):
    req = requests.get(url)

    soup = BeautifulSoup(req.text,'lxml')
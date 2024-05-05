import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def extract_links(url):
    # Your function implementation here
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = []
    for link in soup.find_all("a"):
        if (
            (href := link.get("href"))
            and (parsed_url := urlparse(href)).scheme
            and parsed_url.netloc
        ):
            links.append(href)
    return links


def is_valid(url):
    # Your function implementation here
    try:
        response = requests.head(url)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

import requests

def crawl_html(url):
    response = requests.get(url)
    return response.content


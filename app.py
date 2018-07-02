from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

from flask import Flask, request, render_template

app = Flask(__name__)


def get_page_data(url):
    hdr = {
        'User-Agent': 'Mozilla/5.0'
    }
    req = Request(url, headers=hdr)
    html = urlopen(req)
    
    bs = BeautifulSoup(html.read(), "html.parser")
    items = bs.find_all('div', {'class': 'ui-item'})
    return items


def find_link(item):
    link = item.find('a')
    return link.attrs['href']

    
def prepare_response(links):
    str="<ol>"
    for l in links:
        str += '<li><a href="https://bikroy.com/{}">{}</a></li>'.format(l,l)
    str += "</ol>"
    return str
    

@app.route('/')
def index():

    links = set()
    for i in range(1,10):
        url = "https://bikroy.com/bn/ads/bangladesh/vehicles?page={}".format(i)
        raw_data = get_page_data(url)
        for r in raw_data:
            link = find_link(r)
            links.add(link)
            
    parsed_response = prepare_response(links) 
    return parsed_response

if __name__ == "__main__":
    app.run()

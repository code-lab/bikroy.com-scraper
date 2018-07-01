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
    links = bs.find('div', {
        'class': 'home-categories'
    })

    .find_all(
        'h4',
        {
            'class': 'menu-item-header'
        }
    )
    print(links)
    return {
        'bs': bs,
#        'categories': categories
    }


def get_categories(raw_data):
    pass


def prepare_response():
    pass



@app.route('/')
def index():
    url = "https://bikroy.com/"
    raw_data = get_page_data(url)
    #print(raw_data['categories'])
    return "Done"
    categories = get_categories(raw_data)
    print(categories)

    parsed_response = prepare_response()


if __name__ == "__main__":
    app.run()

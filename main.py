import requests
from bs4 import Beautifulsoup

res = requests.get('https://news.ycombinator.com/news')
soup = Beautifulsoup(res.text, 'html.parser')
links = soup.select('.storylink')
votes = soup.select('.score')


def create_custom_hn(links, votes):
    hn = []
    for inx, item in enumerate(links):
        title = links[idx].getText()
        hn.append(title)
        return hn

create_custom_hn(links, votes)
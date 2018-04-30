import urllib
from bs4 import BeautifulSoup as bs

def get_rl_status():
    r = urllib.urlopen('http://istheredlinefucked.today/').read()
    soup = bs(r, "html.parser")
    t = soup.findAll("div")
    res = soup.find(id="bottom").text.strip()
    p = soup.prettify('UTF-8','ignore')
    if "Not Really" in res:
        return "OK"
    return "Delayed"

if __name__== "__main__":
    print get_rl_status()

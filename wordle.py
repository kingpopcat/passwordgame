import requests
from bs4 import BeautifulSoup
import datetime
WORDLE_ANSWER_SITE_URL = 'https://www.nytimes.com/svc/wordle/v2/' + str(datetime.datetime.today()).split()[0] + '.json'

def get_site_content(url):
    content = ""
    try:
        content = requests.get(url).content
    except Exception as err:
        print(err)
    return content

def get_wordle_for_today():
    try:
        content = get_site_content(WORDLE_ANSWER_SITE_URL)
        soup = BeautifulSoup (content, "html5lib")
        header = soup.find_all()
        if str(header[0])[47] == '\"':
            return(str(header[0])[48:53])
        return(str(header[0])[47:52])
        
    except Exception as err:
        print(err)

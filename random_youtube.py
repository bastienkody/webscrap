import requests
import bs4


class Rdm_Ytb:
    def __init__(self):
        #https://random-ize.com/random-youtube/
        self.data = requests.get('https://random-ize.com/random-youtube/').text
        self.soup = bs4.BeautifulSoup(self.data, 'html.parser')
        self.line = self.soup.find('iframe')
        self.result = self.line


a = Rdm_Ytb()
print(a.data)

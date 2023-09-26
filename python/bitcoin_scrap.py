import requests
import bs4


class BitcoinPrice:
    def __init__(self):
        #CoinMarketCap (cmc), in dollars
        self.data_cmc = requests.get('https://coinmarketcap.com/').text
        self.soup_cmc = bs4.BeautifulSoup(self.data_cmc, 'html.parser')
        self.line_cmc = self.soup_cmc.find('a', attrs={'href':'/currencies/bitcoin/markets/'})
        self.in_dollars = self.line_cmc.text
        #Bitcoin.fr (fr), in euros
        self.data_fr = requests.get('https://bitcoin.fr/bitcoin-wallets/').text
        self.soup_fr = bs4.BeautifulSoup(self.data_fr, 'html.parser')
        self.body_fr = self.soup_fr.find('div', attrs={'data-live-price': "bitcoin"})
        self.in_euros = self.body_fr.text


if __name__ == '__main__':
    a = BitcoinPrice()
    print(f"{a.in_dollars} btc, source Coinmarketcap")

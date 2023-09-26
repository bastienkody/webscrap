import requests
import bs4


class Currency():
    def __init__(self):
        #https://live.euronext.com/en
        self.data = requests.get('https://live.euronext.com/en').text
        self.soup = bs4.BeautifulSoup(self.data, 'html.parser')
        #EUR / USD
        self.eur_usd_raw = self.soup.find('tr', attrs={'id':'EURUSDFLIT.WFORX'})
        self.eur_usd_name = self.eur_usd_raw.find_next('td')
        self.eur_usd_name_adjst = self.eur_usd_name.text.lstrip().rstrip()
        self.eur_usd_price = self.eur_usd_name.find_next('td')
        self.eur_usd_price_adjst = self.eur_usd_price.text.lstrip().rstrip()
        self.eur_usd_var = self.eur_usd_price.find_next('td')  # daily var (now vs open? but what open time?)
        self.eur_usd_var_adjst = self.eur_usd_var.text.split()
        # EUR / GBP
        self.eur_gbp_raw = self.soup.find('tr', attrs={'id': 'EURGBPFLIT.WFORX'})
        self.eur_gbp_name = self.eur_gbp_raw.find_next('td')
        self.eur_gbp_name_adjst = self.eur_gbp_name.text.lstrip().rstrip()
        self.eur_gbp_price = self.eur_gbp_name.find_next('td')
        self.eur_gbp_price_adjst = self.eur_gbp_price.text.lstrip().rstrip()
        self.eur_gbp_var = self.eur_gbp_price.find_next('td')  # daily var (now vs open? but what open time?)
        self.eur_gbp_var_adjst = self.eur_gbp_var.text.split()
        # EUR / NOK
        self.eur_nok_raw = self.soup.find('tr', attrs={'id': 'EURNOKFLIT.WFORX'})
        self.eur_nok_name = self.eur_nok_raw.find_next('td')
        self.eur_nok_name_adjst = self.eur_nok_name.text.lstrip().rstrip()
        self.eur_nok_price = self.eur_nok_name.find_next('td')
        self.eur_nok_price_adjst = self.eur_nok_price.text.lstrip().rstrip()
        self.eur_nok_var = self.eur_nok_price.find_next('td')  # daily var (now vs open? but what open time?)
        self.eur_nok_var_adjst = self.eur_nok_var.text.split()
        # EUR / JPY
        self.eur_jpy_raw = self.soup.find('tr', attrs={'id': 'EURJPYFLIT.WFORX'})
        self.eur_jpy_name = self.eur_jpy_raw.find_next('td')
        self.eur_jpy_name_adjst = self.eur_jpy_name.text.lstrip().rstrip()
        self.eur_jpy_price = self.eur_jpy_name.find_next('td')
        self.eur_jpy_price_adjst = self.eur_jpy_price.text.lstrip().rstrip()
        self.eur_jpy_var = self.eur_jpy_price.find_next('td')  # daily var (now vs open? but what open time?)
        self.eur_jpy_var_adjst = self.eur_jpy_var.text.split()
        # EUR / CHF
        self.eur_chf_raw = self.soup.find('tr', attrs={'id': 'EURCHFFLIT.WFORX'})
        self.eur_chf_name = self.eur_chf_raw.find_next('td')
        self.eur_chf_name_adjst = self.eur_chf_name.text.lstrip().rstrip()
        self.eur_chf_price = self.eur_chf_name.find_next('td')
        self.eur_chf_price_adjst = self.eur_chf_price.text.lstrip().rstrip()
        self.eur_chf_var = self.eur_chf_price.find_next('td')  # daily var (now vs open? but what open time?)
        self.eur_chf_var_adjst = self.eur_chf_var.text.split()
        # GBP / USD
        self.gbp_usd_raw = self.soup.find('tr', attrs={'id': 'GBPUSDFLIT.WFORX'})
        self.gbp_usd_name = self.gbp_usd_raw.find_next('td')
        self.gbp_usd_name_adjst = self.gbp_usd_name.text.lstrip().rstrip()
        self.gbp_usd_price = self.gbp_usd_name.find_next('td')
        self.gbp_usd_price_adjst = self.gbp_usd_price.text.lstrip().rstrip()
        self.gbp_usd_var = self.gbp_usd_price.find_next('td')  # daily var (now vs open? but what open time?)
        self.gbp_usd_var_adjst = self.gbp_usd_var.text.split()

    def get_price(self, devise=''):
        if devise == '':
            return f"Parité {self.eur_usd_name_adjst} à {self.eur_usd_price_adjst} ({self.eur_usd_var_adjst[0] + self.eur_usd_var_adjst[1]} daily) \nParité {self.eur_gbp_name_adjst} à {self.eur_gbp_price_adjst} ({self.eur_gbp_var_adjst[0] + self.eur_gbp_var_adjst[1]} daily) \nParité {self.eur_nok_name_adjst} à {self.eur_nok_price_adjst} ({self.eur_nok_var_adjst[0] + self.eur_nok_var_adjst[1]} daily) \nParité {self.eur_jpy_name_adjst} à {self.eur_jpy_price_adjst} ({self.eur_jpy_var_adjst[0] + self.eur_jpy_var_adjst[1]} daily) \nParité {self.eur_chf_name_adjst} à {self.eur_chf_price_adjst} ({self.eur_chf_var_adjst[0] + self.eur_chf_var_adjst[1]} daily) \nParité {self.gbp_usd_name_adjst} à {self.gbp_usd_price_adjst} ({self.gbp_usd_var_adjst[0] + self.gbp_usd_var_adjst[1]} daily)"
        elif devise.lower() in ['eurusd', 'eur/usd', 'usd', 'eurodol', 'eurodollar', 'eurodollars', 'dol']:
            return f"Parité {self.eur_usd_name_adjst} à {self.eur_usd_price_adjst} ({self.eur_usd_var_adjst[0] + self.eur_usd_var_adjst[1]} daily)"
        elif devise.lower() in ['eurgbp', 'eur/gbp', 'gbp', 'pound', 'sterlingpound' 'europound', 'eurogbp', 'eurostr']:
            return f"Parité {self.eur_gbp_name_adjst} à {self.eur_gbp_price_adjst} ({self.eur_gbp_var_adjst[0] + self.eur_gbp_var_adjst[1]} daily)"
        elif devise.lower() in ['eurnok', 'eur/nok', 'nok', 'norway', 'krone' 'eurokrone']:
            return f"Parité {self.eur_nok_name_adjst} à {self.eur_nok_price_adjst} ({self.eur_nok_var_adjst[0] + self.eur_nok_var_adjst[1]} daily)"
        elif devise.lower() in ['eurjpy', 'eur/jpy', 'jpy', 'japan', 'yen' 'japan yen']:
            return f"Parité {self.eur_jpy_name_adjst} à {self.eur_jpy_price_adjst} ({self.eur_jpy_var_adjst[0] + self.eur_jpy_var_adjst[1]} daily)"
        elif devise.lower() in ['eurchf', 'eur/chf', 'chf', 'franc suisse']:
            return f"Parité {self.eur_chf_name_adjst} à {self.eur_chf_price_adjst} ({self.eur_chf_var_adjst[0] + self.eur_chf_var_adjst[1]} daily)"
        elif devise.lower() in ['gbpusd', 'gbp/usd']:
            return f"Parité {self.gbp_usd_name_adjst} à {self.gbp_usd_price_adjst} ({self.gbp_usd_var_adjst[0] + self.gbp_usd_var_adjst[1]} daily)"
        else: print('Currency not found. It must be : usd, gbp, nok, jpy, chf compared to eur or gbp/usd')


if __name__ == '__main__':
    a = Currency()
    print(a.get_price())




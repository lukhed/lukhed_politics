from lukhed_basic_utils import requestsCommon as rC
import re

class DOGE:
    def __init__(self):
        self._savings_url = 'https://doge.gov/savings?_rsc=1ddpg'
        self._scrape_savings()
    
    def _scrape_savings(self):
        test = rC.get_soup(self._savings_url)
        receipts = rC.find_elements_by_class(test, 'mx-0 md:mx-20')
        json_str = receipts.get_text(strip=True)
        stop = 1
        
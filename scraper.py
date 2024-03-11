from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import os
from dotenv import load_dotenv

from parsers.TokenParser import TokenParser
from parsers.JsonParser import JsonParser
from WriteCSV import WriteCSV

load_dotenv()

class Scrapper(object):
    
    def __init__(self):
        
        self.cookie = os.getenv("COOKIE")
        self.url = os.getenv("YM_URL")
        self.authorization = os.getenv("AUTHORIZATION")
        self.token_url = os.getenv("YM_ACCESS_TOKEN_URL")
        
        self.page_no = 1
        self.refresh_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMTQzNjgxNCwianRpIjoiMWZjZjM5ZDZjODg1NDc5N2IxMjBmYmZmMjM5MTA5MDciLCJ1c2VyX2lkIjo5MjQ1Nn0.-f1N8VvOPSHoy8C-ZmTPKTjD-u_u2Bmg-Y9uBOdj6cI"
        self.acccess_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEwMTQxNzE0LCJqdGkiOiJmM2UwMzRhMGQ2MzE0ZGEyYjk2YzczMTU5YzkzOGJkOSIsInVzZXJfaWQiOjkyNDU2fQ.G7ZbshCsiyB4tn-LJBIShIB538IBLxkbhY9YxvhaPfo"
        
    def updateToken(self):
        self.acccess_token, self.refresh_token = TokenParser().parse(self.refresh_token)
        
    def scrape(self):        
        has_next = True
        parser = JsonParser()
        csvWriter = WriteCSV()
        
        while has_next:
            print("Scraping page: ", self.page_no)
            headers = {
                "cookie": self.cookie,
                "Authorization": "Bearer " + self.acccess_token
            }
            page_payload = { 
                            "page": self.page_no,
                            "is_masters": 0,
                            "is_phd": 0,
                            "is_undergrad": 1,
                            }
            uni_resp = requests.post(self.url, headers = headers, data = page_payload)
            if uni_resp.status_code == 401:
                self.updateToken()
                continue
            parsed_data = parser.parse(uni_resp.text)
            has_next = parsed_data["has_next"]
            self.page_no = parsed_data["next_page_no"]
            csvWriter.writeIntoCSV(parsed_data["decisions"], "undergrad")
            
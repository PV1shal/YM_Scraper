import json
import os
import requests

class TokenParser:
    
    def __init__(self):
        self.token_url = os.getenv("YM_ACCESS_TOKEN_URL")
        self.cookie = os.getenv("COOKIE")
        
    def parse(self, refresh):
        
        token_headers = {
            "cookie": self.cookie,
        }
        
        refresh_payload = {
            "refresh": refresh
        }
        
        token_resp = requests.post(
            self.token_url,
            headers = token_headers,
            data = refresh_payload
        )
        
        token_data = json.loads(token_resp.text)
        return [token_data["access"], token_data["refresh"]]
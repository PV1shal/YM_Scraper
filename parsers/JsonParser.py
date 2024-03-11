import json

class JsonParser:
    
    def __init__(self):
        pass

    def parse(self, json_data):
        page_data = json.loads(json_data)
        return page_data
import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        #Sends an HTTP GET request using the requests &
        response = requests.get(self.url)
        #returns the content of the response
        return response.content

    def load_json(self):
        #parse the JSON response directly to python list
        response_list = []
        for response in json.loads(self.get_response_body()):
            response_list.append(response)
        return response_list
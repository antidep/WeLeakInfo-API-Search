import requests

api_key = "key"

def search():
    search = input("Data to search:")
    url = "https://api.weleakinfo.to/api?value=" + search + "&type=email&key=" + api_key +""
    response = requests.get(url).json()
    lines = '\n'.join([result['line'] for result in response['result']])
    print("Data: " + lines)

while True:
    search()

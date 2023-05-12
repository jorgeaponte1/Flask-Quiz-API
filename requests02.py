#!/usr/bin/env python3

import requests
from pprint import pprint

# URL of the localhost I will send the get request to.
URL= "http://127.0.0.1:5500/"

def main():
    data = requests.get(URL + "categories").json()
    pprint(data)
    
if __name__ == "__main__":
    main()
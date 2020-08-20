#!/usr/bin/env python3

import requests
import json
import os


def main(data):
    for website in data["websites"]:
        html = requests.get(website["url"])
        if website["searchPhrase"] in html:
            os.system("echo " + website["notificationMessage"] +
                      " | mail " + data["notificationInfo"]["email"])
            print(website["notificationMessage"])


with open("config.json") as json_data_file:
    data = json.load(json_data_file)
print(data)
main(data)

#!/usr/bin/env python
# coding: utf-8

import requests


url = 'http://localhost:9696/predict'
client = {"job": "student", "duration": 280, "poutcome": "failure"}
requests.post(url, json=client).json()
response = requests.post(url, json=client).json()
print(response)

if response['subscribe'] == True:
    print('sending promo email to client')
else:
    print('not sending promo email to client')
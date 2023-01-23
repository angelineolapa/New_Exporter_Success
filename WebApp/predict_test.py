#!/usr/bin/env python
# coding: utf-8

import requests


url = 'http://localhost:9696/predict'

exporter_id = 'xyz-123'
customer = {"exp_region":"amazonia", "product_national":0.0,"pnk":9.85, "other_expenses":0.0, 
           "active_markets":11, "active_products":13, "active_years":3, "prod_class":"section_xi",
           "region":"Asia", "fta":0, "overall_exp":33, "year":20}

response = requests.post(url, json=customer).json()
print(response)
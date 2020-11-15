import pandas as pd
import requests

def get_product_quantities():

    r = requests.get('http://api/products/quantity')
    # r = requests.get('http://localhost:5000/products/quantity')

    return r.json()

from .resources import ProductResource, TransactionListResource
from flask import request
from app import app, api
# import pandas as pd

@app.route('/upc_lookup', methods=['POST'])
def upc_lookup():

    upc = request.json['upc']

    pr = ProductResource()
    return pr.get(upc)

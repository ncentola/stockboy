from .resources import ProductResource, TransactionListResource
from flask import request
from app import app, api, db
import pandas as pd

@app.route('/upc_lookup', methods=['POST'])
def upc_lookup():

    upc = request.json['upc']

    pr = ProductResource()
    return pr.get(upc)

@app.route('/product_quantities', methods=['GET'])
def get_product_quantities():

    data = pd.read_sql('select * from product_quantities_vw', db.engine)
    return data.to_json(orient='records')

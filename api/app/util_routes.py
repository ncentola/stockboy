from .resources import ProductResource, TransactionListResource
from .publisher import Publisher
from flask import request
from app import app, api, db
import pandas as pd
import json

pub = Publisher()

@app.route('/upc_lookup', methods=['POST'])
def upc_lookup():

    upc = request.json['upc']

    pr = ProductResource()
    return pr.get(upc)

@app.route('/product_quantities', methods=['GET'])
def get_product_quantities():

    data = pd.read_sql('select * from product_quantities_vw', db.engine)
    return data.to_json(orient='records')

@app.route('/queue_message', methods=['POST'])
def queue_message():

    pub.publish(routing_key='scanner', message=json.dumps(request.json))
    return {'status': 'success'}

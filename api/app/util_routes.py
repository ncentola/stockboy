from .resources import ProductResource
from flask import request
from app import app, api

@app.route('/upc_lookup', methods=['POST'])
def upc_lookup():

    upc = request.json['upc']

    pr = ProductResource()
    return pr.get(upc)

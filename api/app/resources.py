from flask import request
from flask_restful import Resource

from .models import (
    Transaction,
    Product
)

from .schemas import (
    transaction_schema,
    transactions_schema,
    product_schema,
    products_schema
)

from app import api, db

class TransactionListResource(Resource):
    def get(self):
        transactions = Transaction.query.all()
        return transactions_schema.dump(transactions)

    def post(self):
        new_transaction = Transaction(
            upc=request.json['upc'],
            quantity=request.json['quantity']
        )
        db.session.add(new_transaction)
        db.session.commit()
        return transaction_schema.dump(new_transaction)


class TransactionResource(Resource):
    def get(self, transaction_id):
        transaction = Transaction.query.get_or_404(transaction_id)
        return transaction_schema.dump(transaction)

    # def patch(self, transaction_id):
    #     post = Transaction.query.get_or_404(transaction_id)
    #
    #     if 'title' in request.json:
    #         post.title = request.json['title']
    #     if 'content' in request.json:
    #         post.content = request.json['content']
    #
    #     db.session.commit()
    #     return transaction_schema.dump(post)
    #
    # def delete(self, transaction_id):
    #     post = Transaction.query.get_or_404(transaction_id)
    #     db.session.delete(post)
    #     db.session.commit()
    #     return '', 204

class ProductListResource(Resource):
    def get(self):
        products = Product.query.all()
        return products_schema.dump(products)

    def post(self):
        new_product = Product(
            upc=request.json['upc'],
            data=request.json['data']
        )
        db.session.add(new_product)
        db.session.commit()
        return product_schema.dump(new_product)

class ProductResource(Resource):
    def get(self, upc):
        product = Product.query.get_or_404(upc)
        return product_schema.dump(product)

    # def patch(self, upc):
    #     post = Product.query.get_or_404(upc)
    #
    #     if 'title' in request.json:
    #         post.title = request.json['title']
    #     if 'content' in request.json:
    #         post.content = request.json['content']
    #
    #     db.session.commit()
    #     return product_schema.dump(post)
    #
    # def delete(self, upc):
    #     post = Product.query.get_or_404(upc)
    #     db.session.delete(post)
    #     db.session.commit()
    #     return '', 204

api.add_resource(TransactionListResource, '/transactions')
api.add_resource(TransactionResource, '/transactions/<int:transaction_id>')

api.add_resource(ProductListResource, '/products')
api.add_resource(ProductResource, '/products/<string:upc>')

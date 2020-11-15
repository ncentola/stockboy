from flask import request
from flask_restful import Resource

from datetime import datetime as dt

from .models import (
    Transaction,
    Product,
    ProductQuantity
)

from .schemas import (
    transaction_schema,
    transactions_schema,
    product_schema,
    products_schema,
    product_quantity_schema,
    product_quantities_schema
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

        # create or update an entry in the rollup table
        ProductQuantityResource.patch(self, upc=request.json['upc'])
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

class ProductQuantityListResource(Resource):
    def get(self):
        product_quantities = ProductQuantity.query.all()
        return product_quantities_schema.dump(product_quantities)

    def post(self):
        new_product_quantity = ProductQuantity(
            upc=request.json['upc'],
            quantity=request.json['quantity']
        )
        db.session.add(new_product_quantity)
        db.session.commit()
        return product_quantity_schema.dump(new_product_quantity)

class ProductQuantityResource(Resource):
    def get(self, upc):
        product = ProductQuantity.query.get_or_404(upc)
        return product_quantity_schema.dump(product)

    def patch(self, upc):
        product_quantity = ProductQuantity.query.get(upc)

        if product_quantity is not None:

            if 'quantity' in request.json:
                product_quantity.quantity = product_quantity.quantity + request.json['quantity']
                product_quantity.updated_at = dt.utcnow()

            db.session.commit()
            return product_quantity_schema.dump(product_quantity)

        else:
            request.json['upc'] = upc
            return ProductQuantityListResource.post(self)

    # def delete(self, upc):
    #     post = Product.query.get_or_404(upc)
    #     db.session.delete(post)
    #     db.session.commit()
    #     return '', 204

api.add_resource(TransactionListResource, '/transactions')
api.add_resource(TransactionResource, '/transactions/<int:transaction_id>')

api.add_resource(ProductListResource, '/products')
api.add_resource(ProductResource, '/products/<string:upc>')

api.add_resource(ProductQuantityListResource, '/products/quantity')
api.add_resource(ProductQuantityResource, '/products/quantity/<string:upc>')

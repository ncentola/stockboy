from app import ma

class TransactionSchema(ma.Schema):
    class Meta:
        fields = ('id', 'upc', 'quantity', 'created_at')

class ProductSchema(ma.Schema):
    class Meta:
        fields = ('upc', 'data', 'created_at')

# init Schemas
transaction_schema  = TransactionSchema()
transactions_schema = TransactionSchema(many=True)

product_schema      = ProductSchema()
products_schema     = ProductSchema(many=True)

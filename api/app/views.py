from app import db

db.engine.execute('''DROP VIEW IF EXISTS product_quantities_vw''')

db.engine.execute('''
CREATE OR REPLACE VIEW product_quantities_vw AS
SELECT
    data->>'brand'  as brand
  , data->>'title'  as product
  , data->>'size'   as size
  , quantity
  , updated_at
FROM products p
JOIN product_quantities USING (upc)
''')

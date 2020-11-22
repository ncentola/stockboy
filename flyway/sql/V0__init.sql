CREATE TABLE IF NOT EXISTS transactions (
    id          SERIAL PRIMARY KEY
  , upc         VARCHAR(100)
  , quantity    INT NOT NULL
  , created_at  TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS products (
    upc         VARCHAR(100) PRIMARY KEY
  , data        JSONB
  , created_at  TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS product_quantities (
    upc         VARCHAR(100) PRIMARY KEY
  , quantity    INT
  , updated_at  TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE OR REPLACE VIEW product_quantities_vw AS
SELECT
    data->>'brand'  as brand
  , data->>'title'  as product
  , data->>'size'   as size
  , quantity
  , updated_at
FROM products p
JOIN product_quantities USING (upc);

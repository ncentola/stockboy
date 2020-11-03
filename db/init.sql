-- SET SEARCH_PATH = stockboy.public;

CREATE TABLE public.transactions (
  id         SERIAL PRIMARY KEY,
  upc        VARCHAR NOT NULL,
  quantity   INT NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- CREATE TABLE products (
--   upc       INT PRIMARY KEY,
-- );

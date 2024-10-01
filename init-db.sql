CREATE TABLE IF NOT EXISTS ativos (
    id SERIAL PRIMARY KEY,
    ticker VARCHAR(255) NOT NULL,
    company_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS ativos_prices (
    id SERIAL PRIMARY KEY,
    ativo_id INTEGER NOT NULL,
    price NUMERIC NOT NULL,
    price_open NUMERIC NOT NULL,
    price_high NUMERIC NOT NULL,
    price_low NUMERIC NOT NULL,
    date DATE NOT NULL,
    FOREIGN KEY (ativo_id) REFERENCES Ativos(id)
);
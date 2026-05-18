CREATE TABLE IF NOT EXISTS contacts (
    id           SERIAL PRIMARY KEY,
    name         VARCHAR(100)  NOT NULL,
    email        VARCHAR(150)  NOT NULL,
    message      TEXT          NOT NULL,
    submitted_at TIMESTAMP     DEFAULT NOW()
);
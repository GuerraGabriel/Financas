CREATE TABLE IF NOT EXISTS financa.receita (
    id SERIAL PRIMARY KEY,
    origem CHARACTER VARYING (128),
    valor MONEY NOT NULL DEFAULT 0,
    recebido_em DATE NOT NULL DEFAULT NOW(),
    periodicidade periodicidade
);

CREATE TABLE financa.pagamento ( 
    id SERIAL PRIMARY KEY,
    realizado_em DATE NOT NULL DEFAULT NOW(),
    conta_id INTEGER NOT NULL,
    comprovante CHARACTER VARYING (255),
    observacao TEXT
);

CREATE TABLE financa.tag (
    id SERIAL PRIMARY KEY,
    nome CHARACTER VARYING (128) NOT NULL
);

CREATE TABLE financa.conta (
    id SERIAL PRIMARY KEY,
    nome CHARACTER VARYING (255) NOT NULL,
    descricao TEXT,
    valor MONEY DEFAULT 0 NOT NULL,
    realizada_em DATE NOT NULL DEFAULT NOW(),
    metodo_pagamento CHARACTER VARYING (255) NOT NULL,
    parcelas INTEGER DEFAULT 1 NOT NULL,
    debito_automatico BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE financa.conta_tag (
    conta_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    CONSTRAINT conta_tag_pk PRIMARY KEY (conta_id, tag_id)
);

ALTER TABLE financa.pagamento ADD FOREIGN KEY ("conta_id") REFERENCES "financa"."conta"("id");
ALTER TABLE financa.conta_tag ADD FOREIGN KEY ("conta_id") REFERENCES "financa"."conta"("id");
ALTER TABLE financa.conta_tag ADD FOREIGN KEY ("tag_id") REFERENCES "financa"."tag"("id");

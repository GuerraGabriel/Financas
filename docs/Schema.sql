CREATE TABLE "Receita" (
  "id" integer PRIMARY KEY,
  "origem" varchar,
  "valor" integer,
  "recebido_em" date,
  "peridiciocidade" enum
);

CREATE TABLE "Pagamento" (
  "id" integer PRIMARY KEY,
  "realizado_em" date,
  "conta" integer,
  "comprovante" varchar,
  "observacao" varchar
);

CREATE TABLE "Tag" (
  "id" integer PRIMARY KEY,
  "nome" varchar
);

CREATE TABLE "Conta" (
  "id" integer PRIMARY KEY,
  "nome" varchar,
  "valor" integer,
  "compra_em" date,
  "metodo_pagamento" integer,
  "parcelas" integer,
  "tags" integer,
  "debito_automatico" bool
);

CREATE TABLE "FormaPagamento" (
  "id" integer,
  "nome" varchar,
  "tipo" varchar,
  "banco" varchar
);

ALTER TABLE "Pagamento" ADD FOREIGN KEY ("conta") REFERENCES "Conta" ("id");

ALTER TABLE "Conta" ADD FOREIGN KEY ("metodo_pagamento") REFERENCES "FormaPagamento" ("id");

ALTER TABLE "Conta" ADD FOREIGN KEY ("tags") REFERENCES "Tag" ("id");

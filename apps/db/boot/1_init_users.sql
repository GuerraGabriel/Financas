create role financa_sa;
create role financa_app;

create user sa_financa ENCRYPTED PASSWORD 'admin';
create user financa ENCRYPTED PASSWORD 'admin';

grant financa_sa to sa_financa;
grant financa_sa to postgres;
grant financa_app to financa;
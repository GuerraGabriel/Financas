create schema flyway;
create schema financa;

grant CREATE, USAGE ON SCHEMA financa TO financa_sa ;
grant USAGE ON SCHEMA financa TO financa_app ;

alter role financa_sa SET search_path = financa,flyway,public;
alter role financa_app SET search_path = financa;

alter user sa_financa SET search_path = financa,flyway,public;
alter user financa SET search_path = financa;

grant create on schema financa,flyway to sa_financa;
grant truncate on all tables in schema financa,flyway to sa_financa;

ALTER SCHEMA flyway OWNER TO postgres;
ALTER SCHEMA financa OWNER TO postgres;
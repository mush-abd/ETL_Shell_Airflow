create database if not exists access_log;
use access_log;

create table if not exists access_log(
    timestanp datetime,
    latitude float,
    longitude float,
    visitorid char(37),
    accessed_from_mobile boolean,
    browser_code int
)
DROP TABLE vlgtab1;
CREATE TABLE vlgtab1 (
 key VARCHAR(100)  NOT NULL,
 data TEXT NOT NULL
);
.separator "\t"
.import vlgtab1_input.txt vlgtab1
create index datum on vlgtab1(key);
pragma table_info (vlgtab1);
select count(*) from vlgtab1;
.exit

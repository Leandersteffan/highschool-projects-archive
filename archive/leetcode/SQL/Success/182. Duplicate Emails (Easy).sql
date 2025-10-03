Create table If Not Exists Person (id int, email varchar(255));
Truncate table Person;
insert into Person (id, email) values ('1', 'a@b.com');
insert into Person (id, email) values ('2', 'c@d.com');
insert into Person (id, email) values ('3', 'a@b.com');

--@BLOCK
SELECT a.email AS email FROM person AS a, person AS b
WHERE not a.id = b.id
    AND a.email = b.email
;

--@block
select Email from
(
  select Email, count(Email) as num
  from Person
  group by Email
) as statistic
where num > 1
;

--@block
select Email
from Person
group by Email
having count(Email) > 1;
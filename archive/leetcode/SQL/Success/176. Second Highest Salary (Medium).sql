Create table If Not Exists Employee (id int, salary int);
Truncate table Employee;
insert into Employee (id, salary) values ('1', '100');
insert into Employee (id, salary) values ('2', '200');
insert into Employee (id, salary) values ('3', '300');

--@BLOCK
SELECT MAX(salary) AS SecondHighestSalary FROM
(
    SELECT * FROM Employee
    WHERE
    (
        SELECT MAX(salary) FROM Employee
    ) != salary
) AS statistic;

--@block
SELECT MAX(salary) AS SecondHighestSalary
FROM
(
    SELECT salary FROM Employee
    WHERE salary != (SELECT MAX(salary) FROM Employee)
) AS statistic;

--@block
Select (select salary from employee
group by salary
order by  salary desc limit 2,2) as 'SecondHighestSalary'
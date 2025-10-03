Create table If Not Exists Employee (id int, name varchar(255), salary int, managerId INT);
Truncate table Employee;
insert into Employee (id, name, salary, managerId) values ('1', 'Joe', '70000', '3');
insert into Employee (id, name, salary, managerId) values ('2', 'Henry', '80000', '4');
insert into Employee (id, name, salary) values ('3', 'Sam', '60000');
insert into Employee (id, name, salary) values ('4', 'Max', '90000');

--@block
SELECT * FROM employee;

--@block
SELECT
    a.Name AS 'Employee'
FROM
    Employee AS a,
    Employee AS b
WHERE
    a.managerId = b.id
        AND a.salary > b.salary
;

--@block
SELECT
     a.NAME AS Employee
FROM Employee AS a JOIN Employee AS b
     ON a.ManagerId = b.Id
     AND a.Salary > b.Salary
;

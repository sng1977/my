select * from pds.employees order by FIRST_NAME asc;
select FIRST_NAME, LAST_NAME, SALARY, SALARY*0.15 as tax from pds.employees;
select sum(SALARY) from pds.employees;
select max(SALARY), min(SALARY) from pds.employees;
select avg(SALARY) as avg_salary, count(EMPLOYEE_ID) as employee_num from pds.employees;
#1
SELECT count(distinct e.JOB_ID) as vacant_jobs, count(e.EMPLOYEE_ID) as max_vvacanties
from pds.employees e;

#2
select avg(SALARY), count(EMPLOYEE_ID)
FROM pds.employees e
where e.DEPARTMENT_ID=90
group by e.DEPARTMENT_ID;

#3
select JOB_ID, count(EMPLOYEE_ID)
from pds.employees e
group by e.JOB_ID;

#4
select e.FIRST_NAME, e.LAST_NAME, d.DEPARTMENT_ID, d.DEPARTMENT_NAME
from pds.employees e
join pds.departments d on (e.DEPARTMENT_ID=d.DEPARTMENT_ID);

#5
select 
	e.FIRST_NAME, e.LAST_NAME, j.JOB_TITLE, e.DEPARTMENT_ID
from 
	pds.employees e
	join pds.jobs j on (e.JOB_ID=j.JOB_ID)
	join pds.departments d on (e.DEPARTMENT_ID=d.DEPARTMENT_ID)
	join pds.locations l on (d.LOCATION_ID=l.LOCATION_ID)
where
	l.city='London';

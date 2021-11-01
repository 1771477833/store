SELECT ename 员工姓名,deptno 部门编号 FROM t_employees
WHERE deptno=30

SELECT ename 员工姓名,deptno 部门编号,empno 员工编号 FROM t_employees
WHERE job='经理'

SELECT ename 员工姓名,comm 奖金,sal 薪资 FROM t_employees
WHERE sal<comm

SELECT ename 员工姓名,comm 奖金,sal 薪资 FROM t_employees
WHERE sal*0.6<comm

SELECT ename 员工姓名,deptno 部门编号,empno 员工编号,job 工作 FROM t_employees
WHERE job='经理'
AND deptno=10
OR job='分析员'
AND deptno=20

SELECT * FROM t_employees
WHERE job='经理'
AND deptno=10
OR job='分析员'
AND deptno=20
OR job NOT IN('经理','武装上将')
AND sal>=3000

SELECT ename 员工姓名,comm 奖金 FROM t_employees
WHERE comm='NULL' OR comm<1000

SELECT ename 员工姓名 FROM t_employees
WHERE ename LIKE '___'

SELECT ename 员工姓名,hiredate 入职日期 FROM t_employees
WHERE hiredate>='2000-01-01'

SELECT * FROM t_employees
ORDER BY
deptno ;

SELECT * FROM t_employees
ORDER BY
sal DESC;

SELECT 
	e.deptno,AVG(e.sal) AS avgsal
FROM 
	t_employees AS e
GROUP BY
	deptno;

SELECT t_employees.`job`,COUNT(*) FROM t_employees INNER JOIN t_employees ON t_employees.deptno=t_dept.deptno
GROUP BY deptno;

SELECT * FROM t_employees
WHERE deptno=10

SELECT 
	deptno 部门编号,COUNT(*) 人数
FROM 
	t_employees 
GROUP BY
	deptno;

SELECT job,MAX(sal),MIN(sal),COUNT(*)
FROM t_employees 
GROUP BY job








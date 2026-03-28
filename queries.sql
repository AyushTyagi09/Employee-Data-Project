-- Average salary by department
SELECT department, AVG(salary)
FROM employees
GROUP BY department;

-- Total employees per department
SELECT department, COUNT(*)
FROM employees
GROUP BY department;

-- High salary employees
SELECT * FROM employees
WHERE salary > 50000;

-- Top 3 highest salaries
SELECT name, salary
FROM employees
ORDER BY salary DESC
LIMIT 3;
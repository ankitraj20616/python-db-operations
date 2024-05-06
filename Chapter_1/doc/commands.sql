CREATE DATABASE IF NOT EXISTS python_db_operations;

USE python_db_operations;

CREATE TABLE IF NOT EXISTS employee
                  (EMP_NO INT PRIMARY KEY,
                E_NAME VARCHAR(50),
                JOB VARCHAR(30),
                MGR INT,
                HIR_DATE DATE,
                SAL INT,
                DEPT_NO INT);

INSERT INTO employee
(EMP_NO, E_NAME, JOB, MGR, HIR_DATE, SAL, DEPT_NO)
VALUES
(7369, 'SMITH', 'CLERK', 7902, '1980-12-17', 800, 20),
(7499, 'ALLEN', 'SALESMAN', 7698, '1981-02-20', 1600, 30),
(7521, 'WARD', 'SALESMAN', 7698, '1981-02-22', 1250, 30),
(7566, 'JONES', 'MANAGER', 7839, '1981-03-02', 2975, 20),
(7876, 'ADAMS', 'CLERK', 7788, '1987-05-23', 1100, 20);

SELECT * FROM employee;

SELECT * FROM employee WHERE DEPT_NO = 20;

SELECT * FROM employee WHERE SAL >= 2500;

SELECT * FROM employee WHERE JOB = 'SALESMAN';
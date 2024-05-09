# Chapter 2:- Operators

import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="7260020616@nkit",
                               database="python_db_operations")

mycursor = mydb.cursor()

# mycursor.execute("""INSERT INTO employee
#                  (EMP_NO, E_NAME, JOB, MGR, HIR_DATE, SAL, DEPT_NO)
#                 VALUES
#                 (7902, 'FORD', 'ANALYST', 7566, '1981-12-03', 3000, 20),
#                 (7934, 'MILLER', 'CLERK', 7782, '1982-01-23', 1300, 10);""")

# mydb.commit()

# IN Operator:-
# Ex:-

# mycursor.execute("SELECT * FROM employee WHERE DEPT_NO IN (10, 20)")
# mycursor.execute("SELECT * FROM employee WHERE JOB IN ('CLERK', 'ANALYST')")

# for row in mycursor:
#     print(row)

# LIKE Operator:-
# Ex:-

# mycursor.execute("SELECT * FROM employee WHERE E_NAME LIKE 'S%'")
# mycursor.execute("SELECT * FROM employee WHERE E_NAME LIKE '%_LL_%'")
# mycursor.execute("SELECT * FROM employee WHERE E_NAME LIKE '%_E_'")
# mycursor.execute("SELECT * FROM employee WHERE E_NAME LIKE '___R%'")
# mycursor.execute("SELECT * FROM employee WHERE JOB LIKE '_____'")
# mycursor.execute("SELECT * FROM employee WHERE E_NAME LIKE '_____%'")

# for row in mycursor:
#     print(row)

# BETWEEN Operator:-
# Ex:-

# mycursor.execute("SELECT * FROM employee WHERE SAL BETWEEN 800 AND 1100")

# for row in mycursor:
#     print(row)

# IS Operator:-
# Ex:-

# mycursor.execute("SELECT * FROM employee WHERE MGR IS null")

# for row in mycursor:
#     print(row)

# LOGICAL Operators:-
# mycursor.execute("SELECT E_NAME FROM employee WHERE JOB = 'SALESMAN' AND DEPT_NO = 30")
# mycursor.execute("SELECT E_NAME FROM employee WHERE JOB = 'SALESMAN' AND DEPT_NO = 30 AND SAL > 1500")
# mycursor.execute("SELECT E_NAME FROM employee WHERE E_NAME LIKE 'S%' OR E_NAME LIKE 'A%'")
# mycursor.execute("SELECT * FROM employee WHERE DEPT_NO NOT IN (10 , 20)")
# mycursor.execute("SELECT * FROM employee WHERE E_NAME NOT LIKE 'S%'")
# mycursor.execute("SELECT * FROM employee WHERE MGR IS NOT NULL AND DEPT_NO = 30")
# mycursor.execute("SELECT * FROM employee WHERE JOB NOT IN ('MANAGER', 'CLERK') AND DEPT_NO IN (10, 20) AND SAL BETWEEN 1000 AND 3000")
# mycursor.execute("SELECT * FROM employee WHERE SAL NOT BETWEEN 1000 AND 2000 AND DEPT_NO IN (10, 20, 30) AND JOB != 'SALESMAN'")
# mycursor.execute("SELECT * FROM employee WHERE E_NAME LIKE '%O%'")

# for row in mycursor:
#     print(row)


# SORTING:-

# mycursor.execute("SELECT * FROM employee ORDER BY SAL ASC")
mycursor.execute("SELECT * FROM employee ORDER BY SAL DESC")

for row in mycursor:
    print(row)
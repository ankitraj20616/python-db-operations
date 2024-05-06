import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="7260020616@nkit")

my_cursor = mydb.cursor()

my_cursor.execute("CREATE DATABASE IF NOT EXISTS python_db_operations;")

my_cursor.execute("USE python_db_operations;")

my_cursor.execute("""CREATE TABLE IF NOT EXISTS employee
                  (EMP_NO INT PRIMARY KEY,
                E_NAME VARCHAR(50),
                JOB VARCHAR(30),
                MGR INT,
                HIR_DATE DATE,
                SAL INT,
                DEPT_NO INT);""")

# my_cursor.execute("""INSERT INTO employee
#                 (EMP_NO, E_NAME, JOB, MGR, HIR_DATE, SAL, DEPT_NO)
#                 VALUES
#                 (7369, 'SMITH', 'CLERK', 7902, '1980-12-17', 800, 20),
#                 (7499, 'ALLEN', 'SALESMAN', 7698, '1981-02-20', 1600, 30),
#                 (7521, 'WARD', 'SALESMAN', 7698, '1981-02-22', 1250, 30),
#                 (7566, 'JONES', 'MANAGER', 7839, '1981-03-02', 2975, 20),
#                 (7876, 'ADAMS', 'CLERK', 7788, '1987-05-23', 1100, 20);
#                 """)

# mydb.commit()

# my_cursor.execute("SELECT * FROM employee;")
# for row in my_cursor:
#     print(row)

# Assignment :- 1
# my_cursor.execute("SELECT * FROM employee WHERE DEPT_NO = 20;")
# for row in my_cursor:
#     print(row)


# Assignment :- 2
# my_cursor.execute("SELECT * FROM employee WHERE SAL >= 2500;")
# for row in my_cursor:
#     print(row)

#Assignment :- 3
my_cursor.execute("SELECT * FROM employee WHERE JOB = 'SALESMAN';")
for row in my_cursor:
    print(row)
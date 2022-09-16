# 题目

### Define Database

##### 创造Database



##### 预览

```sql
DESCRIBE student;
```




### Query 


##### 逻辑关系

```sql
SELECT student.name, student.major
FROM student
WHERE student <> 'sdfsd'
ORDER BY student_id DESC;
LIMIT 2
```

还有可以用 IF 函数
WHEN 的用法都可以属于逻辑关系里, 下面有WHEN的用

```sql

UPDATE salary
SET
    sex = CASE sex
        WHEN 'm' THEN 'f'
        ELSE 'm'
    END;


SELECT T2.Request_at as Day, 0 + ROUND(SUM(IF(T2.Status <> 'completed',1,0)) / SUM(1),2) as 'Cancellation Rate'
FROM(
        SELECT T1.*
        FROM Trips AS T1
        LEFT JOIN (Select Users_Id, Role
             FROM Users
             Where Users.Banned = 'Yes') As U1
        ON T1.Client_Id = U1.Users_Id or T1.Driver_Id = U1.Users_Id
        WHERE CASE WHEN U1.Role = 'client' THEN T1.Client_Id <> U1.Users_Id
                   WHEN U1.Role = 'driver' THEN T1.Driver_Id <> U1.Users_Id
                   ELSE TRUE END) AS T2
WHERE T2.Request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY T2.Request_at
ORDER BY T2.Request_at;

```

### IN

注意 IN 一般是 IN ('a','b','c')

如果要放在query里,一般需要再用一个select 套用

```sql
SELECT * FROM Table1 WHERE id NOT IN (SELECT id FROM Table2)

```

#### Order
DESC ASC 倒序正序


特殊的order
```sql

WHERE
   x_field IN ('f', 'p', 'i', 'a') ...
ORDER BY
   CASE x_field
      WHEN 'f' THEN 1
      WHEN 'p' THEN 2
      WHEN 'i' THEN 3
      WHEN 'a' THEN 4
      ELSE 5 --needed only is no IN clause above. eg when = 'b'
   END, id



ORDER_BY cast(registration_no as int) ASC

```

[特殊排序规则](https://stackoverflow.com/questions/6332043/sql-order-by-multiple-values-in-specific-order ":)")

[var 转 int 排序](https://stackoverflow.com/questions/16519648/sql-for-ordering-by-number-1-2-3-4-etc-instead-of-1-10-11-12/16520873 ":)")

#### 逻辑运算
<,<= >= > , <>, AND OR
<> 是不等于

IN ('xc','sdfsd','sdfsdf')

#### 位运算

and &
or |
XOR ^
左右移为 << >>
INVERT ~
BIT COUNT 得到最高位 BIT_COUNT(64) -> 1, BIT_COUNT(BINARY 64) -> 7


#### 种类

```sql

SELECT DISTINCT sex
FROM employee;
```

#### From 很多table
FROM 多个table的本质是,比如说一个TABLE 有 1,2,3 行,另一个是 A,B,C 行 

```sql
SELECT *
FROM table1, table2

```
就会形成 
1 A
2 A
3 A
1 B
2 B
3 B
1 C
2 C
3 C

所以如果其中一个是 NONE的空集的话,整个都会是空集,这个非常值得注意

其实 From A, B
就是 Inner join 或者Cross Join,

所以这种情况我们往往要用LEFT JOIN避免空集

#### GROUP BY

```sql
SELECT COUNT(sex), sex
FROM employee
GROUP BY sex;

SELECT SUM(total_sales), emp_id
FROM works_with
GROUP BY emp_id;


SELECT class
FROM courses
GROUP BY class
HAVING COUNT(student) >= 5;

```

GROUP BY 之后要用 HAVING 来做这个, WHERE 还是对每个行做判断, HAVING 是 整合之后的做判断


有时候GROUP By必须用一些特殊的函数组合,会有不一样的效果

```sql
SELECT D1.id, 
IF(D1.month = 'Jan', D1.revenue, Null) as "Jan_Revenue",
IF(D1.month = 'Feb', D1.revenue, Null) as "Feb_Revenue",
IF(D1.month = 'Mar', D1.revenue, Null) as "Mar_Revenue",
IF(D1.month = 'Apr', D1.revenue, Null) as "Apr_Revenue",
IF(D1.month = 'May', D1.revenue, Null) as "May_Revenue",
IF(D1.month = 'Jun', D1.revenue, Null) as "Jun_Revenue",
IF(D1.month = 'Jul', D1.revenue, Null) as "Jul_Revenue",
IF(D1.month = 'Aug', D1.revenue, Null) as "Aug_Revenue",
IF(D1.month = 'Sep', D1.revenue, Null) as "Sep_Revenue",
IF(D1.month = 'Oct', D1.revenue, Null) as "Oct_Revenue",
IF(D1.month = 'Nov', D1.revenue, Null) as "Nov_Revenue",
IF(D1.month = 'Dec', D1.revenue, Null) as "Dec_Revenue"
FROM Department as D1
GROUP BY D1.id;

# SELECT D1.id, 
# MAX(IF(D1.month = 'Jan', D1.revenue, Null)) as "Jan_Revenue",
# MAX(IF(D1.month = 'Feb', D1.revenue, Null)) as "Feb_Revenue",
# MAX(IF(D1.month = 'Mar', D1.revenue, Null)) as "Mar_Revenue",
# MAX(IF(D1.month = 'Apr', D1.revenue, Null)) as "Apr_Revenue",
# MAX(IF(D1.month = 'May', D1.revenue, Null)) as "May_Revenue",
# MAX(IF(D1.month = 'Jun', D1.revenue, Null)) as "Jun_Revenue",
# MAX(IF(D1.month = 'Jul', D1.revenue, Null)) as "Jul_Revenue",
# MAX(IF(D1.month = 'Aug', D1.revenue, Null)) as "Aug_Revenue",
# MAX(IF(D1.month = 'Sep', D1.revenue, Null)) as "Sep_Revenue",
# MAX(IF(D1.month = 'Oct', D1.revenue, Null)) as "Oct_Revenue",
# MAX(IF(D1.month = 'Nov', D1.revenue, Null)) as "Nov_Revenue",
# MAX(IF(D1.month = 'Dec', D1.revenue, Null)) as "Dec_Revenue"
# FROM Department as D1
# GROUP BY D1.id;


```

经常 我们遇到一些情况是我们既要一些group的性质, 然后保留一些行的特殊属性, 往往要结合Join, group只能展示组合属性。


比如这个答案里的 
[Get records with max value for each group of grouped SQL results](https://stackoverflow.com/questions/12102200/get-records-with-max-value-for-each-group-of-grouped-sql-results  ":)")

```sql
SELECT o.*
FROM `Persons` o                    # 'o' from 'oldest person in group'
  LEFT JOIN `Persons` b             # 'b' from 'bigger age'
      ON o.Group = b.Group AND o.Age < b.Age
WHERE b.Age is NULL                 # bigger age not found
```

最大化问题, 结合where is null, 确实巧妙。


##### WITH .. AS 
然后Derived Table 要整一个名字赋值, 然后如果要join 它, 可以用一个temporary 的table 表示
[SQL - Query Self Join without executing it twice](https://stackoverflow.com/questions/35839590/sql-query-self-join-without-executing-it-twice ":)")


```sql
WITH MyQueryAlias1 AS (30 minutes sql query here)
SELECT q1.field1
FROM   MyQueryAlias1 q1
       JOIN MyQueryAlias1 q2
       ON q1.field2 = q2.field3
```

注意, WITH xx AS xx 她的顺序和平时是相反的。

```sql
WITH A1 AS (SELECT d1.dept_no, d1.emp_no, s1.salary
      FROM dept_emp as d1
      LEFT JOIN salaries as s1
      ON d1.emp_no = s1.emp_no
      WHERE d1.to_date = '9999-01-01' and s1.to_date = '9999-01-01')
SELECT A1.*
FROM A1
LEFT JOIN A1 AS A2
ON A1.dept_no = A2.dept_no and A1.salary < A2.salary
WHERE A2.salary is NULL;

```



#### 日期的处理

日期的处理不能只用 + -, 有特殊的function
```sql
SELECT W1.id
FROM Weather as W1, Weather as W2
WHERE W2.recordDate = subdate(W1.recordDate, 1) and W2.Temperature < W1.Temperature;

SELECT DATE_ADD("2017-06-15", INTERVAL 10 DAY);

SELECT SUBDATE("2017-06-15", INTERVAL -2 MONTH);


```
小时分钟都可以用。

#### 基础 SQL function

###### COUNT
```sql
SELECT COUNT(emp_id)
from employee;
```

##### AVG

##### SUM

1. MAX
2. MIN

然后我们就可以用来选 第 N 大的数了

先 N 的limit 然后求里面 最大或者最小的

这个逻辑是可以的,
但是 SQL 不允许 nested qurry 里面使用 LIMIT, (应该说不能在IN 里用)

```sql 
# Write your MySQL query statement below
Select MIN(Salary) as SecondHighestSalary
FROM Employee
WHERE Id in (
    select Id
    From Employee
    Order by Salary DESC LIMIT 2
);
```
这样是没办法编译的。

但是如果是JOIN 就可以窝
```sql
# Write your MySQL query statement below
Select MIN(Salary) as SecondHighestSalary
FROM Employee as X
JOIN (
    select Id
    From Employee
    Order by Salary DESC LIMIT 2
) AS Y ON X.Id = Y.Id;
```

注意这样写的话要给那个新表一个名字
(还是有个问题, 就是如果没有第N大的数字的话,还是会有输出)


---
还有一个办法是 LIMIT 有一个range 的功能比如说
LIMIT 2,2;
就是第2个, 

但其实不是range。。

这个limit是有点搞笑的

第一个数字是从第几个开始,0 是第一位,1 是第二位,
第二个数字是长度,如果超出原来的table的长度的话就会有Null代替

---
挺 tricky 的一个部分是,如果两个数同大, 那怎么算呢？ 用 distinct

```sql
Select(
Select DISTINCT(Salary)
FROM Employee
ORDER by Salary DESC
LIMIT 1,1
)  as SecondHighestSalary;

```


#### MAX data WITH other column
要找到最大的值,然后对应其他的信息, 要在 from 里写一个subquery, 比如：

求第二高的工资的人 (题目要求不用order)
```sql
WITH m as (SELECT max(s1.salary) as M FROM salaries AS s1 WHERE to_date = '9999-01-01')
SELECT s2.emp_no, s2.salary, e1.last_name, e1.first_name
FROM salaries as s2, m, employees as e1
WHERE s2.to_date = '9999-01-01' and s2.emp_no = e1.emp_no and
s2.salary = (SELECT max(s3.salary) from salaries as s3 where s3.salary < m.M);

```

有一个巧妙的网友给的答案 求第几高的,可以参考这个 group by , having count 的思路

```sql
select e.emp_no,s.salary,e.last_name,e.first_name
from
employees e
join 
salaries s on e.emp_no=s.emp_no 
and  s.to_date='9999-01-01'
and s.salary = 
(
     select s1.salary
     from 
     salaries s1
     join
     salaries s2 on s1.salary<=s2.salary 
     and s1.to_date='9999-01-01' and s2.to_date='9999-01-01'
     group by s1.salary
     having count(distinct s2.salary)=2
 )


```






### SQL Variable

定义格式是 @variable_name := xxxx

比如如果我们要给一个列表一个序号

```sql
SELECT value, (@a := @a + 1) as 'Rank' 
FROM (
	SELECT value, @a := 0 FROM Order_test
) as T;
```

这里的 Rank 好像是因为是一个其他内置函数的关键词,所以用‘’包着,


##### Rank Problem

利用刚刚的Variable 我们就可以Rank了

```sql
SELECT scores.Score, A.Rank
FROM scores
LEFT JOIN 
(
	SELECT Score, @curRank := @curRank + 1 as 'Rank'
	FROM (
		SELECT DISTINCT Score, @curRank := 0 FROM scores ORDER BY Score DESC) as temp) as A
 ON scores.Score = A.Score
 Order By Score DESC;

```


更专门化的Rank可以这样：
```sql
select
    score,
    dense_rank() over(order by score desc) as 'Rank'
from scores

```

要理解这个得先理解Window Function 和 Over


第一例子是  OVER (PARTITION BY xx)

```sql

Rank() over(PARTITION BY E1.DepartmentId Order By Salary DESC)

```

dense_rank 和 rank 两个函数的区别也很直观,比如 100, 200, 200, 300 

dense rank 输出 1, 2, 2 ,3
rank 输出, 1,2,2,4
就可以 partition by 某个东西然后再调用函数。有点像group by 和运用函数的结合。


注意 GROUP BY 和 PARTITION BY 的重要区别, PARTITION by 不做整合, 他会保留每一行的信息,这也是为什么它可以同时输出其他列的信息。

所以这个例子：

```sql

SELECT DISTINCT(e1.dept_no), d1.dept_name, t1.title, COUNT(t1.title) OVER(PARTITION BY e1.dept_no, t1.title ) as 'count'
FROM departments as d1, dept_emp as e1, titles as t1
WHERE d1.dept_no = e1.dept_no 
        AND t1.emp_no = e1.emp_no 
        AND t1.to_date = '9999-01-01' 
        AND e1.to_date = '9999-01-01'
ORDER BY e1.dept_no;

```

如果坚持使用partition by 的话, 要用distinct

[牛客网例题](https://www.nowcoder.com/practice/4bcb6a7d3e39423291d2f7bdbbff87f8?tpId=82&tags=&title=&diffculty=0&judgeStatus=0&rp=1 ":)")

#### Consecutive number

求连续几个相同的数,

我用了非常笨的Left Join 方法, 我估计在我会的几个语法里唯一能用的了

```sql

Select DISTINCT Num as ConsecutiveNums
FROM logs
LEFT JOIN (
    Select Id as id1, Num as num1, plustwo.num2 as num3
    from Logs as plusone
    LEFT JOIN (
        SELECT Id as id2, Num as num2 from Logs) as plustwo
    On Id = plustwo.id2 + 1) as combine
ON Id = combine.id1 + 1
WHERE Num = combine.num1 and Num = combine.num3;

```

好吧, 答案也是用了类似的思想, 但是ID 相当于是一个 Prime Key, 所以可以直接这样, 用where 就能做一个类似JOIN功能的东西。还是比较巧妙的。

```sql
SELECT DISTINCT
    l1.Num AS ConsecutiveNums
FROM
    Logs l1,
    Logs l2,
    Logs l3
WHERE
    l1.Id = l2.Id - 1
    AND l2.Id = l3.Id - 1
    AND l1.Num = l2.Num
    AND l2.Num = l3.Num
;

```


用Count 可以巧妙的搞N 个 连续的 (不太行, 没法整N个相等)

```sql
SELECT c1.Id 
FROM consecutive c1 
WHERE $n = (SELECT count(*) 
           FROM consecutive c2 
           WHERE c2.Id 
           BETWEEN c1.Id AND (c1.Id + $n - 1)
           );

```

#### GROUP BY HAVING

也是一个重要的用法：

```sql
SELECT Email
FROM Person
GROUP by Email
HAVING COUNT(Email) >= 2;
```
HAVING 和 Where 有时候容易弄混, 记住 Having 是专门为了 aggregates 的数据, WHERE 是为了 row by row 的数据的




##### 括号in 的用法

找到每个部门最高工资的,

(我的之前的用法）

```sql

SELECT D1.Name AS 'Department', E1.Name as 'Employee', Salary
FROM Employee as E1,
     Department as D1,
     (SELECT E2.DepartmentId as Did, MAX(SALARY) as maxTemp
     FROM Employee AS E2
     GROUP BY E2.DepartmentId) as A
WHERE E1.Salary = A.maxTemp and 
      E1.DepartmentId = Did and
      D1.Id = E1.DepartmentId;

```

(什么时候用 Join 什么时候用 where)

<img src="/post_asset/2020-12-08-SQL_1.png" alt="2020-12-08-SQL_1.png failed" width="400"/>


```sql
SELECT
    Department.name AS 'Department',
    Employee.name AS 'Employee',
    Salary
FROM
    Employee
        JOIN
    Department ON Employee.DepartmentId = Department.Id
WHERE
    (Employee.DepartmentId , Salary) IN
    (   SELECT
            DepartmentId, MAX(Salary)
        FROM
            Employee
        GROUP BY DepartmentId
	)
;

```

##### 删除重复的数据

```sql
DELETE P1 FROM Person As P1,
     (Select Id FROM Person GROUP BY Email) as P2
WHERE 
     P1.Id <> P2.Id;

```
这里的where 是无效的, 这里只要有一个不等于被满足,都会被纳入到这个系列里, 所以会导致所有的row都被删除。

```sql
DELETE p1 FROM Person p1,
    Person p2
WHERE
    p1.Email = p2.Email AND p1.Id > p2.Id


OR

DELETE P1 FROM Person As P1,
     (Select * FROM Person GROUP BY Email) as P2
WHERE 
     P1.Email = P2.Email and P1.Id <> P2.Id;

```
这能才能把想要的避开。Group By 还有一个问题,就是她可能会选出不想要的Id,就是把Id 小的先给去掉了,可能会造成表格的不连续。





### Replace 

```sql

REPLACE(str, find_string, replace_with)

UPDATE titles_test
SET emp_no = REPLACE(emp_no, '10001', '10005')
WHERE id = '5';
```


### RENAME

```sql
RENAME TABLE titles_test TO titles_2017;

```


#### INDEX 的处理

```sql

SHOW INDEX FROM table_name # 展示所有的index 关系 index 名称等

DROP INDEX index_name ON table_name  # 清除某个index

CREATE UNIQUE INDEX index_name ON table_name(column_name); # 添加某种index

```
INDEX 的用处是加快查询, 使用的时候是这样的：

```sql
SELECT * FROM salaries FORCE INDEX(idx_emp_no) WHERE emp_no = 10005
SELECT * FROM salaries USE INDEX(idx_emp_no) WHERE emp_no = 10005
```

强制index 和普通index 有什么区别？


### view

[为什么要使用VIEW](https://stackoverflow.com/questions/2680207/what-is-a-good-reason-to-use-sql-views ":)")

```sql

CREATE VIEW actor_name_view AS
SELECT first_name as first_name_v, last_name as last_name_v
FROM actor;

```

### 创建一个 PROCEDURE

```
DROP TABLE IF EXISTS number;
CREATE TABLE number(
	id INT(8) PRIMARY KEY,
  	value DOUBLE,
  	name VARCHAR(45)
);

drop PROCEDURE if exists myproc;
CREATE PROCEDURE myproc()
BEGIN
  DECLARE i int DEFAULT 0;
  WHILE (i <= 100) DO
      INSERT INTO number (id, value, name) VALUES( i, RAND(), 'alan');
      SET i = i + 1;
  END WHILE;
END;

CALL myproc();

```

#### Window Functions & Over





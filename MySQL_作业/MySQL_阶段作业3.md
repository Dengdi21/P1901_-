# MySQL_阶段作业3

## 建库建表
a.建立一个公司数据库(gongsi) 

```
 CREATE DATABASE gongsi;
```
  
b.建立一张部门表department
 b_id 部门编号 主键 自增长
 b_name 部门名称  非空  

```
CREATE TABLE department
(
b_id INT(20) PRIMARY KEY AUTO_INCREMENT,
b_name VARCHAR(255) NOT NULL);
```

c.建立一张员工表employee
 y_id 员工编号  主键，自增长
 y_name 姓名
 y_sex 性别
 y_age 年龄
 y_address 住址  默认值：不详
 b_id 部门编号   外键列
 
 ```
CREATE TABLE employee
(
y_id int(50) PRIMARY KEY AUTO_INCREMENT,
y_name char(255),
y_sex char(50),
y_age int(50),
y_address VARCHAR(255) DEFAULT '不详',
b_id INT(20),
CONSTRAINT De_Id FOREIGN KEY(b_id) 
REFERENCES department(b_id)
); 
 ```
 
1、查询年龄在25至30岁之间的男员工的姓名和住址。 

```
SELECT y_name,y_address FROM employee 
WHERE y_age >= 25 and y_age <= 30 and y_sex = '男';
```

2、查询财务部所有40岁以下男员工的所有信息。

```
SELECT b.* FROM department AS a JOIN employee AS b
ON
a.b_id = b.b_id
WHERE 
a.b_name = '财务部' 
AND b.y_sex = '男' 
AND y_age < 40;
```

3、查询人事部年龄最大的女员工姓名。

```
SELECT b.y_name FROM department AS a 
JOIN employee AS b ON a.b_id = b.b_id 
WHERE 
a.b_name = '人事部'
AND b.y_sex = '女' 
ORDER BY y_age DESC 
LIMIT 1;
```

4、2号新到一名员工，已知姓名，性别，年龄，将此员工加入到员工表。
 
```
INSERT INTO employee(y_name,y_sex,y_age) 
VALUES('李四','男',32);
```

5、在员工表中，将人事部年龄大于30岁的女同事，调到后勤部。

```
设人事部部门编号为2，后勤部部门编号为1：
UPDATE department AS a JOIN employee AS b 
SET b.b_id = 1 
WHERE b.b_id = 2 
AND b.y_sex = '女' 
AND b.y_age > 30;
```

6：查询每个部门年龄最大的员工，显示部门名字和年龄。

```
SELECT a.b_name,MAX(b.y_age) AS max_age 
FROM department AS a JOIN employee AS b 
ON a.b_id = b.b_id 
GROUP BY a.b_name
```

7：查询每个部门各有多少人，显示部门名字和人数，按人数倒序，如果人数相同，按部门编号正序。

```
SELECT a.b_name,COUNT(b.b_id) AS number 
FROM department AS a JOIN employee AS b 
ON a.b_id = b.b_id 
GROUP BY a.b_name 
ORDER BY COUNT(b.b_id) DESC,a.b_id; 
```

8：将张三的的名字改为李四，并调到财务部。

```
设财务部部门编号为3：
UPDATE employee STE y_name = '李四',b_id = 3 
WHERE y_name = '张三';
```

9：将后勤部年龄大于60岁的员工删除。

```
后勤部部门编号为1：
DELETE FROM employee WHERE b_id = 1 AND y_age > 60;
```

10：查询财务部年龄不在20-30之间的男生信息。

```
财务部部门编号为2：
SELECT * FROM employee 
WHERE y_sex = '男' AND b_id = 2 
AND y_age NOT IN (20,30);
```
# MySQL_阶段作业4

## 设教学数据库Education有三个关系：学生关系S（SNO，SNAME，AGE，SEX，SDEPT）；学习关系SC（SNO，CNO，GRADE）；课程关系C（CNO，CNAME，CDEPT，TNAME）

### 查询问题：
1：查所有年龄在20岁以下的学生姓名及年龄。

```
SELECT SNAME,AGE FROM S WHERE AGE < 20; 
```

2：查考试成绩有不及格的学生的学号。

```
SELECT SNO FROM SC WHERE GRADE <60; 
```

3：查所年龄在20至23岁之间的学生姓名、系别及年龄。

```
SELECT SNAME,SDEPT,AGE FROM S 
WHERE AGE >= 20 AND AGE <= 23;
```

4：查计算机系、数学系、信息系的学生姓名、性别。

```
SELECT SNAME,SEX FROM S 
WHERE SDEPT IN('计算机系','数学系','信息系'); 
```

5：查既不是计算机系、数学系、又不是信息系的学生姓名、性别。

```
SELECT SNAME,SEX FROM S 
WHERE SDEPT NOT IN('计算机系','数学系','信息系'); 
```

6：查所有姓“刘”的学生的姓名、学号和性别。

```
SELECT SNAME,SNO,SEX FROM S WHERE SNAME LIKE '刘%';
```

7：查姓“上官”且全名为3个汉字的学生姓名。

```
SELECT SNAME FROM S WHERE SNAME LIKE '上官_';
```

8：查所有不姓“张”的学生的姓名。

```
SELECT SNAME FROM S WHERE SNAME NOT LIKE '张%';
```

9：查DB_Design课程的课程号。

```
SELECT CNO FROM C WHERE CNAME = 'DB_Design';
```

10：查缺考的学生的学号和课程号。

```
SELECT SNO,CNO FROM SC WHERE GRADE IS NULL;
```

11：查年龄为空值的学生的学号和姓名。

```
SELECT SNO,SNAME FROM S WHERE AGE IS NULL;
```

12：查计算机系20岁以下的学生的学号和姓名。

```
SELECT SNO,SNAME FROM S 
WHERE AGE < 20 AND SDEPT = '计算机系';
```

13：查计算机系、数学系、信息系的学生姓名、性别。

```
SELECT SNAME,SEX FROM S WHERE SDEPT IN('计算机系','数学系','信息系');
```

14：查询选修了C3课程的学生的学号和成绩，其结果按分数的降序排列。

```
SELECT SNO,GRADE FROM SC 
WHERE CNO = 'C3' ORDER BY GRADE DESC;
```

15：查询全体学生的情况，查询结果按所在系升序排列，对同一系中的学生按年龄降序排列。

```
SELECT * FROM S ORDER BY SDEPT,AGE DESC; 
```

16：查询学生总人数。

```
SELECT COUNT(*) AS total FROM S;
```

17：查询选修了课程的学生人数。

```
SELECT COUNT(*) AS total1 FROM SC;
```

18：计算选修了C1课程的学生平均成绩。

```
SELECT AVG(GRADE) AS C1_AVG FROM SC WHERE CNO = 'C1';
```

19：查询学习C3课程的学生最高分数。

```
SELECT MAX(GRADE) AS C3_MAX FROM SC WHERE CNO = 'C3';
```

20：查询各个课程号与相应的选课人数。

```
SELECT CNO,COUNT(CNO) AS NUMBER FROM SC GROUP BY CNO;
```

21：查询计算机系选修了3门以上课程的学生的学号。

```
SELECT S.SNO, COUNT(S.SNO) AS NUMBER FROM S JOIN SC
ON S.SON = SC SNO
WHERE S.SDEPT = '计算机系' 
GROUP BY S.SNO 
HAVING COUNT(S.SNO) > 2;
```

22：求基本表S中男同学的每一年龄组（超过50人）有多少人？要求查询结果。按人数升序排列，人数相同按年龄降序排列。

```
SELECT AGE,COUNT(AGE) AS NUMBER FROM S 
GROUP BY AGE 
ORDER BY COUNT(AGE),AGE DESC;
```

23：查询每个学生及其选修课程的情况。

```
SELECT SC.SNO,C.* FROM SC JOIN C 
ON SC.CNO = C.CNO;
```

24：查询选修了C2课程且成绩在90分以上的所有学生。

```
SELECT S.* FROM S JOIN SC
ON S.SNO = SC.SNO 
WHERE GRADE > 90 AND CNO = 'C2';
```

25：查询每个学生选修的课程名及其成绩。

```
SELECT SC.SNO,C.CNAME,SC.GRADE FROM SC JOIN C
ON SC.CNO = C.CNO 
```

26：统计每一年龄选修课程的学生人数。

```
SELECT S.AGE,COUNT(S.AGE) total FROM S JOIN SC 
ON S.SNO = SC.SNO 
GROUP BY S.AGE;
```

27：查询选修了C2课程的学生姓名。

```
SELECT S.SNAME FROM S JOIN SC ON S.SNO = SC.SNO 
WHERE SC.CNO = 'C2';
```

28：查询与“张三”在同一个系学习的学生学号、姓名和系别。

```
SELECT SNO,SNAME,SDEPT FROM S 
WHERE SDEPT = 
(SELECT SDEPT FROM S WHERE SNAME = '张三');
```

29：查询选修课程名为“数据库”的学生学号和姓名。

```
SELECT S.SNO,S.SNAME FROM C,SC,S WHERE S.SNO = SC.SNO AND SC.CNO = C.CNO AND C.CNAME = '数据库';
```

30：查询与“张三”在同一个系学习的学生学号、姓名和系别。

```
SELECT SNO,SNAME,SDEPT FROM S 
WHERE SDEPT = 
(SELECT SDEPT FROM S WHERE SNAME = '张三');
```

31：查询选修课程名为“数据库”的学生学号和姓名。

```
SELECT S.SNO,S.SNAME FROM C,SC,S WHERE S.SNO = SC.SNO AND SC.CNO = C.CNO AND C.CNAME = '数据库';
```

32：查询选修了C2课程的学生姓名。

```
 SELECT S.SNAME FROM S JOIN SC ON S.SNO = SC.SNO 
 WHERE SC.CNO = 'C2';
```

33：查询所有未选修C2课程的学生姓名。

```
SELECT S.SNAME FROM S JOIN SC ON S.SNO = SC.SNO 
WHERE SC.CNO != 'C2';
```

34：查询与“张三”在同一个系学习的学生学号、姓名和系别。

```
SELECT SNO,SNAME,SDEPT FROM S 
WHERE SDEPT = 
(SELECT SDEPT FROM S WHERE SNAME = '张三');
```

35：查询选修了全部课程的学生姓名。

```
假设有五门选修课：
SELECT S.SNAME FROM S,SC 
WHERE S.SNO = 
(SELECT SNO FROM SC GROUP BY SNO 
HAVING COUNT(SNO) = 5);
```
36：查询所学课程包含学生S3所学课程的学生学号。

```
SELECT SNO FROM SC WHERE CNO = 'S3';
```
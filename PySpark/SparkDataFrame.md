


# Initialize Spark SQL

```py
from pyspark.sql import HiveContext

hive_context = HiveContext(sparkSession)

df = hive_context.sql("""
select *
from a_table
"""
)

```



# Basic & Common Function of Spark DataFrame


## Create Or Copy & Scheme

Scheme means the sql columns types, and other definition

```py

## Create DF
spark.createDataFrame(X_pd, schema=schema)


### Full example 


from pyspark.sql.types import StructType,StructField 
from pyspark.sql.types import StringType, IntegerType, ArrayType
data = [
    (("James","","Smith"),["Java","Scala","C++"],"OH","M"),
    (("Anna","Rose",""),["Spark","Java","C++"],"NY","F"),
    (("Julia","","Williams"),["CSharp","VB"],"OH","F"),
    (("Maria","Anne","Jones"),["CSharp","VB"],"NY","M"),
    (("Jen","Mary","Brown"),["CSharp","VB"],"NY","M"),
    (("Mike","Mary","Williams"),["Python","VB"],"OH","M")
 ]
        
schema = StructType([
     StructField('name', StructType([
        StructField('firstname', StringType(), True),
        StructField('middlename', StringType(), True),
         StructField('lastname', StringType(), True)
     ])),
     StructField('languages', ArrayType(StringType()), True),
     StructField('state', StringType(), True),
     StructField('gender', StringType(), True)
 ])

df = spark.createDataFrame(data = data, schema = schema)
df.printSchema()
df.show(truncate=False)

```


<b> Ouptut </b> 

```

root
 |-- name: struct (nullable = true)
 |    |-- firstname: string (nullable = true)
 |    |-- middlename: string (nullable = true)
 |    |-- lastname: string (nullable = true)
 |-- languages: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- state: string (nullable = true)
 |-- gender: string (nullable = true)

+----------------------+------------------+-----+------+
|name                  |languages         |state|gender|
+----------------------+------------------+-----+------+
|[James, , Smith]      |[Java, Scala, C++]|OH   |M     |
|[Anna, Rose, ]        |[Spark, Java, C++]|NY   |F     |
|[Julia, , Williams]   |[CSharp, VB]      |OH   |F     |
|[Maria, Anne, Jones]  |[CSharp, VB]      |NY   |M     |
|[Jen, Mary, Brown]    |[CSharp, VB]      |NY   |M     |
|[Mike, Mary, Williams]|[Python, VB]      |OH   |M     |
+----------------------+------------------+-----+------+


```

## Display
```py

## into visualiszed lines
df.show(5)

df.show() ## default 500 lines ?


## into list of rows
df.head(5)

```

## Filter | Search | Where

[sparkbyexample](https://sparkbyexamples.com/pyspark/pyspark-where-filter/ ":)")

.filter === .where

``` py

# Operation inside braket
df.filter(df.state != "OH") \
    .show(truncate=False) 
df.filter(~(df.state == "OH")) \
    .show(truncate=False)
df.filter( (df.state  == "OH") & (df.gender  == "M") ) \
    .show(truncate=False)  


```


```py
# Sql where statement


```

many other funciton like

- like
- rlike

- isin


- array_contains


- startswith
- endswith

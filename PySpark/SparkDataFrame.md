


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



spark.createDataFrame(X_pd, schema=schema)


```

## Display
```py

## into visualiszed lines
df.show(5)

df.show() ## default 500 lines ?


## into list of rows
df.head(5)

```

## Filter | Search



```py



```

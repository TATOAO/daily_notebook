
# Initialize Spark Session

## from sql

```py

from pyspark.sql import SparkSession

spark = SparkSession.bulider.master("yarn").appName("any_name").getOrCreate()


#### to config using .config ####

SparkSession.builder.\
.config("spark.yarn.queue", "queue_name")\
.config("spark.executor.instances", "2")\
.config("spark.executor.memory", "8")\
.config("spark.executor.cores", "2")\
.config("spark.default.parallelism", "20")\
.config("spark.sql.catelogImplementation", "hive")\
.config("spark.driver.extraJavaOptions", "-Duser.timezone=GMT+8")\
.config("spark.executor.extraJavaOptions", "-Duser.timezone=GMT+8")\
.config("spark.sql.session.timeZone", "GMT+8")\
```


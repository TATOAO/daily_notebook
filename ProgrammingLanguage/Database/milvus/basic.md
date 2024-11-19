


# 1 Connect

```python
from pymilvus import MilvusClient, utility, connections

client = MilvusClient(url="http://localhost:19530")

# or 
connections.connect(host='127.0.0.1', port = '19530')
```



## 1.1. check collections
```python

collections = utility.list_collections()
```

## 1.2. drop collection

```python
utility.drop_collection(collection_name)

```


## 1.3 create collection

```python
from pymilvus import FieldSchema, DataType

fields = [
    FieldSchema(name = "id", dtype=DateType.INT64, is_primary=True, auto_id=True),
    FieldSchema(name = "title", dtype=DateType.VARCHAR, max_length=500),
    FieldSchema(name = "title_vector", dtype=DateType.FLOAT_VECTOR, dim = 256),
]


```

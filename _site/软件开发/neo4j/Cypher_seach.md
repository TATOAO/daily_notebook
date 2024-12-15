

# search all nodes and relationships



## search all nodes:

```cypher
MATCH (n)
RETURN n
```


## display all nodes, relationships


```cypher
START n=node(*) MATCH (n)-[r]->(m) RETURN n,r,m;
```




### relationship jumps? 
[k:KNOWS*..4] is structural information to use in a path (seen later). Here, \*..4 says "Match the pattern, with the relationship k which can be repeated between 1 and 4 times.



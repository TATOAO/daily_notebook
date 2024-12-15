
[cheatsheet](https://neo4j.com/docs/cypher-cheat-sheet/5/aura-dbe/ ":)")



# Create node

CREATE (charlie:Person:Actor {name: 'Charlie Sheen'}), (oliver:Person:Director {name: 'Oliver Stone'})

1. charlie node名称
2. :Person:Actor  相当于node的tag
3. {name: 'Charlie Sheen'}  node 属性


# Create edge/relationship

CREATE (charlie:Person:Actor {name: 'Charlie Sheen'})-[:ACTED_IN {role: 'Bud Fox'}]->(wallStreet:Movie {title: 'Wall Street'})<-[:DIRECTED]-(oliver:Person:Director {name: 'Oliver Stone'})


如果要服用之前的nodes

MATCH (charlie:Person {name: 'Charlie Sheen'}), (oliver:Person {name: 'Oliver Stone'})
CREATE (charlie)-[:ACTED_IN {role: 'Bud Fox'}]->(wallStreet:Movie {title: 'Wall Street'})<-[:DIRECTED]-(oliver)

# Delete Node



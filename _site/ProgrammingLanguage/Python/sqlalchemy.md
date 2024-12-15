
# connect

```py
db_url = 'sqlite:///your_database.db'
engine = create_engine(db_url, connect_args={'timeout': 30})
Session = sessionmaker(bind=engine)
metadata = MetaData()
metadata.reflect(bind=engine)
```

# query


## raw sql
```py
with engine.connect() as connection:
    result = connection.execute(text('SELECT * FROM your_table'))
```


## use framework

```py

# get data method 1
USERS = meta_data.tables['users']
# get data method 2
table = Table(table_name, metadata, autoload_with=db_engine)


# View the columns present in the users table
print(USERS.columns)

# You can run sqlalchemy queries
query = db.select([
    USERS.c.id,
    USERS.c.first_name,
    USERS.c.last_name,
])

result = engine.execute(query).fetchall()

```


## session.query vs  engine.execute

Differences Between session.query and engine.execute
Event Handling:

session.query: Fully integrated with SQLAlchemy ORM's event system. You can attach listeners to events like before_insert, before_update, etc., to preprocess or validate data.
engine.execute: Bypasses ORM events because it operates at a lower level, dealing directly with SQL statements. Listeners attached to ORM events won't affect operations executed via engine.execute.
Abstraction Level:

session.query: High-level abstraction, using mapped classes and ORM features.
engine.execute: Low-level, raw SQL execution, without ORM features.
Use Cases:

session.query: Preferred for ORM operations where you want to take advantage of object-relational mapping, automatic event handling, and other high-level abstractions.
engine.execute: Suitable for executing custom or complex SQL statements directly, bypassing ORM.
Conclusion
Use session.query and related ORM methods if you need to leverage SQLAlchemy's event system for preprocessing data before insertions or updates.
Use engine.execute for raw SQL execution where you don't require the high-level features of the ORM, such as event handling.


For example:
```py
def records_and_update(table, db_engine, data_row: dict):
    with db_engine.connect() as conn:
        with conn.begin():
            primary_key_name = inspect(table).primary_key.c.keys()[0]
            where_clause = table.c.get(primary_key_name) == data_row[primary_key_name]
            exam_exist = conn.execute(table.select().where(where_clause))
            existing = exam_exist.fetchone()

            if existing:
                conn.execute(
                    table.update().where(where_clause).values(data_row)
                )
            else:
                conn.execute(table.insert().values(data_row))
```
This will by pass the ORM, event listen methods.

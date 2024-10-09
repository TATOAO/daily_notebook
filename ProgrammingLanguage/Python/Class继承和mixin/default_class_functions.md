


# with ..  Context manager

```Python

with open("./somefile.txt") as f:
    contents = f.read()
    print(contents)

```

When the with block finishes, it makes sure to close the file, even if there were exceptions.

In Python, you can create Context Managers by creating a class with two methods: __enter__() and __exit__().


```py

class MySuperContextManager:
    def __init__(self):
        self.db = DBSession()

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        self.db.close()


async def get_db():
    with MySuperContextManager() as db:
        yield db

```



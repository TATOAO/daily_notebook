pydantic





```py
from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    friends: list[int]


external_data = {
    "id" : 2032,
    "name": 'alan',
}

user = User(**external_data)
```

报错： 默认写法的话全部的属性项目都是必填
friends
  Field required [type=missing, input_value={'id': 2032, 'name': 'alan'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.0.1/v/missing



# population with Field name


```python
from pydantic import BaseModel, ConfigDict, Field


class Resource(BaseModel):
    name: str = Field(alias="identifier")
    model_config = ConfigDict(populate_by_name=True)


r1 = Resource(name="a name")  # works
r2 = Resource(identifier="a name")  # works thanks to populate_by_name=True

print(r1.name)  # works
print(r2.identifier)

```

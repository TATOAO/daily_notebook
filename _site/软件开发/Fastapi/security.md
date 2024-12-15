

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

```

from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}
```

oauth2_scheme 看起来只是吧 bear xxx 里面的token解析出来








# 如何调用tokenUrl


```python
import requests

url = "http://127.0.0.1:8000/token"

payload = {'username': 'alice',
'password': 'secret2'}
files=[

]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
```




# password lib

1. pyjwt
2. passlib

PyJWT: We need to install PyJWT to generate and verify the JWT tokens in Python.

PassLib: is a great Python package to handle password hashes. It supports many secure hashing algorithms and utilities to work with them.



```python

from passlib.context import CryptContext

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


to_encode = data.copy()
if expires_delta:
    expire = datetime.now(timezone.utc) + expires_delta
else:
    expire = datetime.now(timezone.utc) + timedelta(minutes=15)
to_encode.update({"exp": expire})

encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

```






# jwt encode decode

jwt =  "JSON Web Tokens".


```python
# jwt_expire.py
from datetime import datetime, timedelta, timezone
import time
import jwt

ACCESS_TOKEN_EXPIRE_MINUTES = 1
SECRET_KEY = "xxxxx"
ALGORITHM = "HS256"


data: dict ={"sub": 'alan'}
to_encode = data.copy()
expire = datetime.now(timezone.utc) + timedelta(seconds=5)

# 这是一个固定的入产 exp
to_encode.update({"exp": expire})
# 如果没有会立马报错
# to_encode.update({"ss": expire})

encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


for i in range(20):

    payload = jwt.decode(encoded_jwt, SECRET_KEY, algorithms=[ALGORITHM])
    # 超过expire 时间，jwt.decode 会立马报错
    print(encoded_jwt)
    print(payload)
    time.sleep(0.5)


```
# cd 软件开发/Fastapi && python security.md





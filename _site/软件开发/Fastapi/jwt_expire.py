
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

print(encoded_jwt)

for i in range(20):

    payload = jwt.decode(encoded_jwt, 'sfewf', algorithms=[ALGORITHM])
    # 超过expire 时间，jwt.decode 会立马报错
    print(encoded_jwt)
    print(payload)
    time.sleep(0.5)

    # raise ExpiredSignatureError("Signature has expired")
    # jwt.exceptions.ExpiredSignatureError: Signature has expired


# cd 软件开发/Fastapi && python jwt_expire.py && cd - 

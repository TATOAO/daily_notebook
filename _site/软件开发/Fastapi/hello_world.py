from datetime import datetime, timedelta, timezone
import time
import jwt

ACCESS_TOKEN_EXPIRE_MINUTES = 1
SECRET_KEY = "ceff06d79480f619d6eb03ca56de53be7444c189da9462c712aae356c98d8590"
ALGORITHM = "HS256"


data: dict ={"sub": 'alan'}
to_encode = data.copy()
expire = datetime.now(timezone.utc) + timedelta(seconds=5)
to_encode.update({"sss": expire})

encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


for i in range(20):
    payload = jwt.decode(encoded_jwt, SECRET_KEY, algorithms=[ALGORITHM])
    print(encoded_jwt)
    print(payload)
    time.sleep(0.5)





# 软件开发/Fastapi/hello_world.py
# python hello_world.py
# if __name__ == "__main__":
#     main()



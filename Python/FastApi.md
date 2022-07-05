

# 写get function

``` py

from fastapi import FastAPI, Request


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/test/")
async def test(request: Request):
    params = request.query_params
    print(params)
    print(dir(params))
    print(params['dd'])
    return 'ssss'

```


# 运行
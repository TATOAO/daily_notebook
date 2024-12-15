from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()


data = {
    "plumbus": {"description": "Freshly pickled plumbus", "owner": "Morty"},
    "portal-gun": {"description": "Gun to create portals", "owner": "Rick"},
}


class OwnerError(Exception):
    pass


def get_username():
    try:
        yield "Rick"
    except OwnerError as e:
        raise HTTPException(status_code=400, detail=f"Owner error: {e}")
    finally:
        print('this is finished')
        


@app.get("/items/{item_id}")
def get_item(item_id: str, username: Annotated[str, Depends(get_username)]):
    if item_id not in data:
        raise HTTPException(status_code=404, detail="Item not found")
    item = data[item_id]
    if item["owner"] != username:
        raise OwnerError(username)
    return item




################################################################################





from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()


class InternalError(Exception):
    pass


def get_username():
    try:
        yield "Rick"
    except InternalError:
        print("We don't swallow the internal error here, we raise again 😎")
        raise


@app.get("/items/{item_id}")
def get_item2(item_id: str, username: Annotated[str, Depends(get_username)]):
    if item_id == "portal-gun":
        raise InternalError(
            f"The portal gun is too dangerous to be owned by {username}"
        )
    if item_id != "plumbus":
        raise HTTPException(
            status_code=404, detail="Item not found, there's only a plumbus here"
        )
    return item_id


"""
Q: My question is, using such a depends, catch the exception and than raise the same exception. what is the point to using it ?

A: 

The example demonstrates how to use dependencies in FastAPI with exception handling, but you’re right to question why the exception is caught and raised again. Here’s the purpose:

Dependency Injection: The get_username function is a dependency injected into the route handler. FastAPI dependencies can perform any logic before the route function executes, such as authentication, database access, etc. In this case, it just provides a username.

Handling Internal Errors: The try-except block in get_username catches InternalError. In real-world applications, this might be useful if you want to handle internal issues (logging, additional cleanup) before re-raising the error. It allows you to intercept the error and add custom logic (logging, cleanup) without completely silencing it.

Re-raising Exception: By catching and re-raising, you ensure that any side effects (like logging or notifications) happen, but the exception still propagates to the correct place, so FastAPI can handle it or return an error response.

In this case, the print statement suggests that normally you would do more (e.g., log to a monitoring system) before re-raising. While it may seem redundant in this simplified example, in a real scenario, it could provide a controlled way of dealing with internal errors without swallowing them completely.

"""

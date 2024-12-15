

# What is ASGI?

ASGI stands for Asynchronous Server Gateway Interface.
It's a successor to the WSGI (Web Server Gateway Interface), which was designed for synchronous Python web applications.
ASGI is designed to handle both synchronous and asynchronous requests, allowing Python web frameworks like FastAPI, Django Channels, and others to support modern web use cases.



exmaple of usage:

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

ulimit -c 0 && gunicorn -w 3 -k uvicorn.workers.UvicornWorker engine:app --bind 0.0.0.0:8080

main -> main.py => app = instance of the application

equal to 

in Python
```python
def main():
    import uvicorn 
    uvicorn.run(app="engine:app", port = port, host="0.0.0.0")
```



Examples of ASGI Servers:
1. Uvicorn:
Lightweight, fast, and ideal for production use with frameworks like FastAPI.
2. Daphne:
Used by Django Channels for asynchronous Django applications.
3. Hypercorn:
Supports multiple protocols, including HTTP/1, HTTP/2, and WebSockets.
4. gunicorn
Built-in multiprocess management (via -w workers), Built-in robust process supervision and restarts




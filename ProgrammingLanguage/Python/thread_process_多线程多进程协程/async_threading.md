


```python
# 如果在一个新的线程，有两个等价的创建新loop的方法

# Option 1 
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
try:
    loop.run_until_complete(self.start()) 
finally:
    loop.close()

# Option 2
asyncio.run(self.start())

```

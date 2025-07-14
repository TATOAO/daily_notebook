import redis

# connect to redis server
r = redis.Redis(host='localhost', port=6379, db=0)

# Add a message to a stream
message_id = r.xadd('mystream', {'field1': 'value1', 'field2': 'value2'})
print(f"Message added with ID: {message_id}")

# check healthy
print(r.ping())
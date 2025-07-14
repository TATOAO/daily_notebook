import redis

# connect to redis server
r = redis.Redis(host='localhost', port=6379, db=0)

messages = r.xread({'mystream': '$'})
for stream, message_list in messages:
    for message_id, fields in message_list:
        print(f"ID: {message_id}, Fields: {fields}")
import redis
import json

client = redis.Redis(host='localhost', port=6379)

# Store JSON data
user_data = {'name': 'Joongho', 'age': 30, 'hobbies': ['coding', 'reading']}
client.set('user:123', json.dumps(user_data))

# Retrieve and decode JSON data
retrieved_data = json.loads(client.get('user:123').decode())
print("Retrieved JSON data:", retrieved_data)

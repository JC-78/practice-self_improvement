import time
import redis

# Setup Redis connection (default port is 6379)
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
# Setting a value with an expiration time (TTL - time-to-live)
redis_client.set('temp_key', 'temporary_value', ex=5)  # Key will expire in 5 seconds

# Incrementing an integer value
redis_client.set('counter', 0)
redis_client.incr('counter')  # Increment by 1 (counter becomes 1)
redis_client.incrby('counter', 10)  # Increment by 10 (counter becomes 11)
print(redis_client.get(f"counter")) #b'11' b for byte string, which is smaller size than regular string 
# Checking if a key exists
exists = redis_client.exists('counter')  # Returns 1 if key exists, 0 otherwise
print(f"Counter key exists: {exists}")

# Deleting a key
redis_client.delete('temp_key')

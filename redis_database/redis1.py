import time
import redis
from pymemcache.client import base

# Setup Redis connection (default port is 6379)
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Setup Memcached connection (default port is 11211)
# memcached_client = base.Client(('localhost', 11211))

# Define number of iterations for the test
num_operations = 10000

# Data to store
key = "sample_key"
value = "This is some test data" * 10  # Make the value reasonably large


def test_redis():
    # Measure time taken to set values in Redis
    start_time = time.time()
    for i in range(num_operations):
        redis_client.set(f"{key}_{i}", value)
    redis_set_time = time.time() - start_time

    # Measure time taken to get values from Redis
    start_time = time.time()
    for i in range(num_operations):
        redis_client.get(f"{key}_{i}")
    redis_get_time = time.time() - start_time

    return redis_set_time, redis_get_time


# def test_memcached():
#     # Measure time taken to set values in Memcached
#     start_time = time.time()
#     for i in range(num_operations):
#         memcached_client.set(f"{key}_{i}", value)
#     memcached_set_time = time.time() - start_time

#     # Measure time taken to get values from Memcached
#     start_time = time.time()
#     for i in range(num_operations):
#         memcached_client.get(f"{key}_{i}")
#     memcached_get_time = time.time() - start_time

#     return memcached_set_time, memcached_get_time


# Run and compare
redis_set_time, redis_get_time = test_redis()
# memcached_set_time, memcached_get_time = test_memcached()

# Print results
print(f"Redis SET time: {redis_set_time:.4f} seconds")
print(f"Redis GET time: {redis_get_time:.4f} seconds")
# print(f"Memcached SET time: {memcached_set_time:.4f} seconds") #commented out cuz I didn't want to home brew install memcached
# print(f"Memcached GET time: {memcached_get_time:.4f} seconds")

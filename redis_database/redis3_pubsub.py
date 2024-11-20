import redis
import threading
import time

def message_listener():
    pubsub = client.pubsub()
    pubsub.subscribe('notifications')

    print("Subscribed to 'notifications' channel. Waiting for messages...")
    for message in pubsub.listen():
        if message['type'] == 'message':
            print(f"Received message: {message['data'].decode()}")

# Start the listener in a separate thread
client = redis.Redis(host='localhost', port=6379)
listener_thread = threading.Thread(target=message_listener, daemon=True)
listener_thread.start()

# Publish messages
time.sleep(2)
client.publish('notifications', 'Hello, Redis!')
client.publish('notifications', 'This is a test message!')
time.sleep(2)

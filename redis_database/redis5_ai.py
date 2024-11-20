import redis
import openai
import hashlib
import json
import time 
client = redis.Redis(host='localhost', port=6379, decode_responses=True)
with open('secret.json', 'r') as f:
    secrets = json.load(f)
openai.api_key = secrets['openai_api_key']

def get_response_from_openai(prompt):
    """Generate a response using OpenAI's Chat API."""
    print("Querying OpenAI API...")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    return response['choices'][0]['message']['content'].strip()

def chatbot(prompt):
    """Chatbot function with Redis caching."""
    # Generate a hash key for the prompt
    prompt_hash = hashlib.sha256(prompt.encode()).hexdigest()
    
    # Check if the response is in the cache
    if client.exists(prompt_hash):
        print("Retrieving response from Redis cache...")
        return client.get(prompt_hash)
    
    # Query OpenAI API and cache the response
    response = get_response_from_openai(prompt)
    client.set(prompt_hash, response, ex=3600)  # Cache for 1 hour
    return response


# Example Usage
while True:
    user_input = input("You: ")
    start=time.time()
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break
    response = chatbot(user_input)
    end=time.time()
    print("result time: ",end-start)
    print(f"AI: {response}")
"""
ou: my girlfriend is the cutest
Querying OpenAI API...
result time:  1.778925895690918
AI: That's sweet! It's great that you think so highly of your girlfriend. Remember, expressing your feelings and appreciation to her can go a long way in maintaining a healthy and happy relationship.
You: my girlfriend is the cutest
Retrieving response from Redis cache...
result time:  0.0007190704345703125
"""
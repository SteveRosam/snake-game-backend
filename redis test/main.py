import redis
import json

# Connect to Redis
# client = redis.Redis(host='redis', port=6379, decode_responses=True)
server_url = 'redis'
port = 6379

client = redis.Redis(host=server_url, port=port, db=0)


###############

print("connecting")
# Connect to Redis server
client = redis.Redis(host=server_url, port=port, db=0)
print("Connected")

print("Testing 1")
# Test setting a key
client.set('test_key', 'test_value')

print("Testing 2")
# Test getting the key
value = client.get('test_key').decode('utf-8')

print("Testing 3")
# Print the result
print(f"Value for 'test_key': {value}")

# Clean up
client.delete('test_key')

print("Done")

################

# Get all keys from Redis
keys = client.keys('*')

# Print all keys and their values
for key in keys:
    value = client.get(key)
    try:
        # Try to parse the value as JSON
        value = json.loads(value)
    except json.JSONDecodeError:
        pass  # If it's not JSON, just keep the value as is
    print(f"{key}: {value}")


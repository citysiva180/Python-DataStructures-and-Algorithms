import redis
r = redis.Redis(
    password="GZMOQGsfT4Ot1IZPrVIqgLGBJQ67CE36",
    host="redis-14511.c92.us-east-1-3.ec2.cloud.redislabs.com",
    port=14511,
    decode_responses=True)

# r.set('foo', 'bar')
# r.mset({'jupiter': 'planet', 'sun': 'star'})
r.hset('captains', 'enterprise', 'kirk')
r.hset('captains', 'voyager', 'janeway')
r.hget('captains', 'enterprise')

# r.lpush('ships', 'enterprise')
# r.lpush('ships', 'deep space nine')

from functools import wraps

from r_pack.r_pack import RedisProvider


def cached(name):

	redis_provider = RedisProvider()

	def decorator(f):
		@wraps(f)
		def wrapper(*args, **kwargs):
			cache = redis_provider.redis_client.get(name)
			if cache is not None:
				print('from redis')
				return cache
			else:
				print('call function')
				result = f(*args, **kwargs)
				redis_provider.redis_client.set(name, result)
				return result
		return wrapper
	return decorator

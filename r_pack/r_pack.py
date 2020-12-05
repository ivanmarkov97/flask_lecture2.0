from utils import singleton
import redis


@singleton
class RedisProvider:

	def __init__(self):
		self._redis_client = redis.Redis(host='localhost', port=6379, db=0)

	@property
	def redis_client(self):
		return self._redis_client

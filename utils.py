from functools import wraps


def singleton(cls):

	_instances = {}

	@wraps(cls)
	def wrapper(*args, **kwargs):
		if cls in _instances:
			return _instances[cls]
		else:
			_instances[cls] = cls(*args, **kwargs)
			return _instances[cls]
	return wrapper


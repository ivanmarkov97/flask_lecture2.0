class Item:

	"""
	Класс описывающий один item с его атрибутами и логикой работы с ними
	"""

	def __init__(self, item_id: int, name: str, description: str, price: int, status: int) -> None:
		"""
		Инициализирует item по входным аргументам.

		Args:
			_id - идентификатов item
			name - Имя
			description - Описание
			...
		"""
		self._item_id = item_id
		self._name = name
		self._description = description
		self._price = price
		self._status = status

	@property
	def item_id(self):
		return self._item_id

	@property
	def name(self):
		return self._name

	@property
	def price(self):
		return self._price

from typing import List

from mysql.connector import connect

from config import MysqlDBConfig
from model.db_interface import DBInterface
from model.models import Item


class MysqlDB(DBInterface):

	def __init__(self) -> None:
		config = MysqlDBConfig()
		self._config = {
			'db': config.db,
			'user': config.user,
			'password': config.password,
			'host': config.host,
			'port': config.port
		}

	def get_all_items(self) -> List[Item]:
		conn = connect(**self._config)
		cursor = conn.cursor()
		_sql = "SELECT item_id, name, description, price, status FROM items"
		cursor.execute(_sql)
		result = cursor.fetchall()
		items = [Item(item_id=raw[0],
		              name=raw[1],
		              description=raw[2],
		              price=raw[3],
		              status=raw[4])
		         for raw in result]
		return items

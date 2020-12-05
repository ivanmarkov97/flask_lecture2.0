from flask import Flask
from flask.views import MethodView

from model.db_interface import DBInterface
from model.mysql_db import MysqlDB
from r_pack.r_pack import RedisProvider
from views.item import ItemView

app = Flask(__name__)
db_connector = MysqlDB()
redis_provider = RedisProvider()


class ItemController(MethodView):

	def __init__(self, connector: DBInterface):
		self._connector = connector

	def get(self):
		items = self._connector.get_all_items()
		item_view = ItemView(url_back='')
		return item_view.show_item_list(items)


app.add_url_rule('/', view_func=ItemController.as_view('index', connector=db_connector))

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5001)

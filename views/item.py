from typing import List

from flask import render_template

from model.models import Item
from cache_tool import cached


class ItemView:

	def __init__(self, url_back):
		self._url_back = url_back

	@cached(name='list_items')
	def show_item_list(self, items: List[Item]):
		return render_template('items.html', list_items=items, back=self._url_back)

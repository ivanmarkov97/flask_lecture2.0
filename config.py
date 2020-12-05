from utils import singleton


@singleton
class MysqlDBConfig:

	db = 'joom'
	user = 'root'
	password = 'root'
	host = '127.0.0.1'
	port = 3306

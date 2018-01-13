# spider_for_btc

pip install requests

pip install pymysql

pip install lxml

pip install web.py
修改config.py的内容 配置数据库连接

建立数据库 
CREATE TABLE `history_message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type_name` varchar(30) NOT NULL,
  `market_price` varchar(30) DEFAULT NULL,
  `sell_price` varchar(30) DEFAULT NULL,
  `timestamp` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4989 DEFAULT CHARSET=latin1

启动爬虫服务 python collect.py &

启动API服务 python apicontrol.py 8001 &

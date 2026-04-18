README.md

datetime模塊支持特殊的日期和時間對象，並能夠以各種方式創建和合併這些對象。

import datetime as dt

dt.datetime(year, month, day, hour, minute, second, microsecond, timezone)

要將datetime對象格式化（format）成字符串，可以使用strftime方法；
要解析（parse）字符串並將其轉換為datetime對象，可以使用strptime函數。
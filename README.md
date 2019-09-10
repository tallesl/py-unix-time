# unix-time

[![](https://badge.fury.io/py/unix-time.svg)](https://pypi.org/project/unix-time)

Unix timestamp made easy.

```py
from unix_time import *

now = ts_now()  # 1568122835, 2019-09-10T13:40:35
today = ts_today()  # 1568073600, 2019-09-10T00:00:00
yesterday = ts_yesterday()  # 1567987200, 2019-09-09T00:00:00

some_time = 1111111111  # 1111111111, 2005-03-18T01:58:31
some_date = ts_date(some_time)  # 1111104000, 2005-03-18T00:00:00
```


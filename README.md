# unix-time

[![](https://badge.fury.io/py/unix-time.svg)](https://pypi.org/project/unix-time)

Unix timestamp made easy.

```py
from unix_time import *

now = ts_now()  # 1568078625, 2019-09-10T01:23:45

yesterday = ts_yesterday()  # 1567987200, 2019-09-09T00:00:00
today = ts_today()  # 1568073600, 2019-09-10T00:00:00
tomorrow = ts_tomorrow()  # 1568160000, 2019-09-11T00:00:00

from datetime import datetime

dt = datetime.fromisoformat('2019-09-10T01:23:45+00:00')

date_plus_time = ts(dt)  # 1568078625, 2019-09-10T01:23:45
date_no_time = ts_date(dt)  # 1568073600, 2019-09-10T00:00:00
```


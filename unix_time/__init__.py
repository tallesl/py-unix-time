from datetime import date, datetime, timedelta
from typing import Union


def ts(dt: Union[date, datetime]) -> int:
    return int(_to_datetime(dt).timestamp())


def ts_date(dt: datetime) -> int:
    return ts(dt.replace(hour=0, minute=0, second=0, microsecond=0))


def ts_now() -> int:
    return ts(datetime.now())


def ts_today() -> int:
    return ts(datetime.today())


def ts_yesterday() -> int:
    return ts(date.today() - timedelta(days=1))


def ts_tomorrow() -> int:
    return ts(date.today() - timedelta(days=-1))


# https://stackoverflow.com/a/1937631
def _to_datetime(dt: Union[date, datetime]) -> datetime:
    return datetime(*dt.timetuple()[:6]) if type(dt) is date else dt

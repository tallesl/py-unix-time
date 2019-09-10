from datetime import datetime


def ts_date(_ts: int) -> int:
    return int(_ts / 86400) * 86400


def ts_now() -> int:
    return int(datetime.now().timestamp())


def ts_today() -> int:
    return ts_date(ts_now())


def ts_yesterday() -> int:
    return ts_today() - 86400

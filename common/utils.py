import pytz
from datetime import datetime


def isLogin(request):
    if request.user.is_authenticated:
        return True
    else:
        return False


# TODO: add it to the other views
def get_time_stamp():
    return int(datetime.now(tz=pytz.utc).timestamp() * 1000)


def get_datetime(date):
    return datetime.fromtimestamp(date / 1000).strftime('%Y-%m-%d %H:%M')

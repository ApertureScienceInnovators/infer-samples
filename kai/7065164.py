import datetime
import pytz

unaware = datetime.datetime(2011, 8, 15, 8, 15, 12, 0)
aware = datetime.datetime(2011, 8, 15, 8, 15, 12, 0, pytz.UTC)


now_aware = pytz.utc.localize(unaware)
aware == now_aware
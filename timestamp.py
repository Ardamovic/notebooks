from datetime import datetime
from pytz import timezone
from pytz import utc

def unix_time( date, time, tz="UTC" ):
    local = timezone (tz)
   
    yy = int(date.split('-')[0])
    mm = int(date.split('-')[1])
    dd = int(date.split('-')[2])
    hhh  = int(time.split(':')[0])
    mmm  = int(time.split(':')[1])
    sss  = int(float(time.split(':')[2]))
   
    loc_dt = local.localize(datetime(yy, mm, dd, hhh, mmm, sss))
    utc_dt = loc_dt.astimezone(utc)
    timestamp = utc_dt.replace(tzinfo=utc).timestamp()
   
    return int(timestamp)

  
def date_time( time, tz="UTC" ):
    local = timezone(tz)
    return datetime.fromtimestamp(time,local)

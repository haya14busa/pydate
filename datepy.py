#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
#
# Author    : haya14busa
# URL       : http://haya14busa.com
# Reference : http://d.hatena.ne.jp/yutakikuchi/20130617/1371425713
# Created   : 2013-08-06
from datetime import *
import time

# DATETIME
def getDateTime():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# TimeStamp Unix Time
def getTimeStamp():
    return str(int(time.time()))

def dt2ts(dtime):
    utime = str( int( time.mktime( datetime.strptime( dtime, "%Y-%m-%d %H:%M:%S" ).timetuple() ) ) )
    # utime = datetime.strptime(dtime, '%Y-%m-%d %H:%M:%S').timetuple()
    # utime = time.mktime(utime)
    # utime = str(int(utime))
    return utime

def ts2dt(utime):
    dtime = str(datetime.fromtimestamp(utime))
    return dtime

if __name__ == '__main__':
    ndt = getDateTime() #str
    nut = getTimeStamp()#str
    print "DATETIME = " + ndt
    print "TIMESTAMP = " + nut
    print "DateTime: {dtime} -> TimeStamp: {utime}".format(
            dtime=ndt, utime=dt2ts(ndt))
    print "TimeStamp: {utime} -> DateTime: {dtime}".format(
            utime=nut, dtime=ts2dt(float(nut)))



# encoding=utf-8
import time
import random


def member(num=1):
    return range(1, num+1)

data = member(80)

for i in xrange(1, 5+1):
    time.sleep(5)
    who = random.choice(data)
    print "The man number of {} get out.".format(who)
    data.remove(who)

print u"结束"

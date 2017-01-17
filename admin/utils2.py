# encoding=utf-8
import random


def member(num=1):
    return range(1, num+1)

data = member(80)

who = random.choice(data)
print "The man number of {} get reward.".format(who)
data.remove(who)

print u"结束"

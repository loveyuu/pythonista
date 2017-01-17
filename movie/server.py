# -*- coding: utf-8 -*-
import thriftpy
from thriftpy.thrift import TProcessor

from models.student import Student

pp_thrift = thriftpy.load("movie.thrift", module_name="pp_thrift")


class Dispatcher(object):
    def ping(self, name):
        print("ping pong!")
        return 'pong {}'.format(name)

    def register2(self, uid, uname, age):
        stu = Student(uid, uname, age)
        return stu.uname


app = TProcessor(pp_thrift.PingService, Dispatcher())

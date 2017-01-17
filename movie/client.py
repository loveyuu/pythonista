# -*- coding: utf-8 -*-

import thriftpy

from thriftpy.rpc import client_context

pp_thrift = thriftpy.load("movie.thrift", module_name="pp_thrift")


def main():
    with client_context(pp_thrift.PingService, '127.0.0.1', 6000) as c:
        pong = c.ping('linbin')
        print(pong)
        print c.register2(1001, "linbin", 24)
        return c.register2(1001, "linbin", 24)


if __name__ == '__main__':
    main()

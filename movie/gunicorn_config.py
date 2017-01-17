# -*- coding: utf-8 -*-
workers = 5
threads = 5
worker_class = "thriftpy_gevent"
thrift_protocol_factory = "thriftpy.protocol:TBinaryProtocolFactory"
thrift_transport_factory = "thriftpy.transport:TBufferedTransportFactory"

errorlog = "-"
loglevel = "info"

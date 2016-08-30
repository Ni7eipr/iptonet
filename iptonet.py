# !/usr/bin/env python
# coding: utf-8

# author:End1ng

from IPy import IP
import sys

if len(sys.argv) != 3:
    print u"usage:\n\tpython iptonet.py 最小IP 最大IP"
    sys.exit()
# 最小IP
ipf = sys.argv[1].strip()

# 最大IP
ipl = sys.argv[2].strip()

preip = ".".join(ipf.split(".")[:-1])
# for x in IP("127.0.0.0/25"):
#     print x

for x in range(31,23,-1):
        for xx in range(256):
            ip = preip + '.%d/%d' % (xx,x)
            try:
                ipnet = IP(ip)
                # print len(ipnet),ipnet
                if ipf in ipnet and ipl in ipnet:
                    print ip
                    sys.exit()
            except:
                pass

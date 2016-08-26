# !/usr/bin/env python
# coding: utf-8

from IPy import IP
import sys

# 最小IP
ipf = """
61.213.189.201
""".strip()

# 最大IP
ipl = """
61.213.189.243
""".strip()

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

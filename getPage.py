#!/usr/bin/env python
# *-* coding=utf-8 *-*

import urllib2
import cookielib
import re


def getUid(sessionID):
    """log in using sessionID ant return uid, I get sessionID from firebug"""

    cookie = "t" + "=" + str(sessionID)

    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
    urllib2.install_opener(opener)
    req = urllib2.Request("http://www.renren.com")
    req.add_header("Cookie", cookie)
    content = urllib2.urlopen(req)

    html = content.read()
    # print(html)
    uid = re.search("'ruid':'(\d+)'",html).group(1)

    print "Login and got uid sucessfully"
    return uid

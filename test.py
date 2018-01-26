# -*- coding: utf-8 -*-

import urllib
import urllib2
import re


page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)


user_agent = 'Mozilla/4.0(comaptible; MSIE 5.5; Windows NT'
headers = {'User-Agent': user_agent}
try:
    request = urllib2.Request(url, headers=headers)
    respons = urllib2.urlopen(request)
#	print respons.read()
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason

content = respons.read().decode('utf-8')
pattern_author = re.compile(u'<h2>(.*?)\s*</h2>',re.S)
pattern_content = re.compile(u'<div class="content">\s*(.*?)\s*</div>',re.S)
pattern_comment = re.compile(u'<i class="number">(\d*)</i>\s*评论',re.S) 
find_author = re.findall(pattern_author, content)
find_content = re.findall(pattern_content, content)
find_comment = re.findall(pattern_comment, content)

if find_author:
    for i in xrange(len(find_author)):
    	content= find_content[i].replace("<br/>",",")
        result = str(i)+" "+find_author[i]+" " + \
            find_content[i]+" "+str(find_comment[i])
        print result



#!/usr/bin/python
import time
list = ['raj','shital','Rajjo']
dict = {}
dict['one'] = "This is one"
dict[2]= "This is two"
tinydict = {'name': 'RAJ','code':'RRU001', 'dept': 'TELEMETRY'}
print dict['one']
print dict[2]
print tinydict
print tinydict.keys()
print tinydict.values()
print list
dict = {'Name': 'raj', 'Age': 33};
print "Equivalent String : %s" % str (dict)
dict2 = dict.copy()
print "New Dictionary : %s" % str(dict2)

t = time.localtime()
print "time.asctime(t): %s " % time.asctime(t)

print "time.ctime() : %s" % time.ctime()

print "time.gmtime() : %s" % time.gmtime()



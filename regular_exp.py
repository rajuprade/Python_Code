#!/usr/bin/python
import re
phone = "2004-959-559 #This is Phone Number"
# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print "Phone Num : ", num
# Remove anything other than digits
num = re.sub(r'\D', "", phone)
print "Phone Num : ", num

line = "Cats are smarter than dogs";
matchObj = re.search( r'(.*) are(\.*)', line, re.M|re.I)
if matchObj:
	print "matchObj.group() : ", matchObj.group()
	print "matchObj.group(1) : ", matchObj.group(1)
	print "matchObj.group(2) : ", matchObj.group(2)
else:
	print "No match!!"

 ## Suppose we have a text with many email addresses
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

 ## Here re.findall() returns a list of all the found email strings
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str) ## ['alice@google.com', 'bob@abc.com']
for email in emails:
 # do something with each found email string
	print email

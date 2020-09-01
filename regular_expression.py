#!/usr/bin/python
import re
str = 'purple alice-b@google.com monkey dishwasher'
match = re.search('([\w.-]+)@([\w.-]+)', str)
if match:
	print match.group()
## 'alice-b@google.com' (the whole match)
	print match.group(1) ## 'alice-b' (the username, group 1)
	print match.group(2) ## 'google.com' (the host, group 2)

## Suppose we have a text with many email addresses
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
## Here re.findall() returns a list of all the found email strings
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str) ## ['alice@google.com', 'bob@abc.com']
for email in emails:
# do something with each found email string
	print email

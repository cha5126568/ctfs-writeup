from hashlib import *

i = 0
while True:
	s = md5("DIMIGO" + str(i)).hexdigest()
	if unicode(s[-6:]) == "000000":
		print "DIMIGO" + str(i)
		exit()
	i += 1

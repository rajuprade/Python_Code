import subprocess
import os
with open(os.devnull, "wb") as limbo:
	for n in xrange(2, 25):
                ip="192.168.70.{0}".format(n)
                result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],
                        stdout=limbo, stderr=limbo).wait()
                if result:
                        print ip, "inactive"
                else:
                        print ip, "active"


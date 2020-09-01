import subprocess
import os

hostname=['C00','C01','C02','C03','C04','C05','C06','C08','C09','C10','C11','C12','C13','C14','E02','E03','E04','E05','E06','S01','S02','S03','S04','S06','W01','W02','W03','W04','W05','W06'];

with open(os.devnull, "wb") as limbo:
        for n in xrange(31, 61):
                ip="192.168.{0}.3".format(n)
                hostid = n -31
                result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],
                        stdout=limbo, stderr=limbo).wait()
                if result:
                        print hostname[hostid],ip, "inactive"
                else:
                        print hostname[hostid],ip, "active"

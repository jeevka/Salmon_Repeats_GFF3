import sys
import re

for i in xrange(100):
    N = "%03d" % (i,)
    Fname = "Sal_Ref" + N + ".fa.out" 
    File = "/mnt/users/jeevka/Salmon_3p6Chr_Masked_021214/Single_Files/" + Fname
    F1 = open(File,"r")
    data = F1.readlines()
    for j in xrange(3,len(data)):
        temp = data[j].split()
        txt = temp[4] + "\t" + "Salmon" + "\t" +"Repeat" + "\t" + temp[5] + "\t" + temp[6] + "\t.\t.\t.\t" + "ID=" + temp[9] + ";Name="+ temp[10]
        print txt
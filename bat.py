import os
import subprocess

cont = True
while cont == True:
    f = open('/sys/class/power_supply/ADP1/online')
    status = int(f.read(1))
    #print(status)
    #print(type(status))

    if status == 1:
        subprocess.call("/bin/ac.sh")
        #subprocess.call("/bin/prueba.sh")
        cont = False
    elif status == 0:
        subprocess.call("/bin/battery.sh")
        cont = False
    else:
        continue

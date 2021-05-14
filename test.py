import ControlPowermeter as fpm
from ThorLabsMotors.PowerMeter import TLPM

#print(pm.open_powermeter('1909736'))
# prints <ThorLabs.TLPM.TLPM object at 0x000001EDACF060A0>


#print(pm.close_powermeter(pm.open_powermeter('1909736')))
# prints None

pm = fpm.open_powermeter('1909736')
fpm.measure_power(pm, 0, 930)
print(fpm.measure_power(pm, 0, 930))
fpm.measure_row(pm, 0, 930)
fpm.close_powermeter(pm)
#prints nothing at call

# pm = fpm.open_powermeter('1909736')
# print(fpm.read_power(pm))
# fpm.close_powermeter(pm)
#
# pm = TLPM()
# print(pm.findRsrc())

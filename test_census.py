from ThorLabsMotors.RotationMount import move_abs, open_serial, get_info
import Settings.offset_settings as offset_settings
import Settings.com_settings as com_settings

bus = open_serial(com_settings.com1,  timeout=0.5)

get_info(bus, 0)

# move_abs(bus, 0, 45)

bus.close()

'''
b'0IN0E1140050920201501016800023000\r\n'
b'1IN0E1140050820201501016800023000\r\n'
'''
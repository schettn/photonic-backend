import ctypes
from ThorLabsMotors import PowerMeter
import time



def open_powermeter(serialnumber):
    '''
    Description
    -----------
          Open the powermeter.

    Parameters
    ----------
    serialnumber : str
        Serial number of the powermeter

    Returns
    -------
    powermeter : ThorLabsMotors.PowerMeter.TLPM object
    '''
    powermeter = PowerMeter.TLPM()
    deviceCount = ctypes.c_uint32()
    powermeter.findRsrc(ctypes.byref(deviceCount))
    # returns (0, <cparam 'P' (00000161BE6D5A88)>)
    print('-----')
    print(powermeter.findRsrc(ctypes.byref(deviceCount)))
    print('-----')
    print(deviceCount.value)
    for i in range (0, deviceCount.value):
        # deviceCount.value = no. of powermeters, is 1 if one powermeter is connected
        resourceName = powermeter.getRsrcName(i)[1]
        # resourceName is e.g. <ctypes.c_char_Array_1024 object at 0x00000161B8FAD8C0>
        print('-----')
        print('resourceName:')
        print(resourceName)
        print('-----')
        print(powermeter.getRsrcName(i))
        # getRsrcName for each instance returns tuple (0, <ctypes.c_char_Array_1024 object at 0x00000161B8FAD8C0>)
        print('-----')
        print(ctypes.c_char_p(resourceName.raw).value)
        # prints b'USB0::0x1313::0x8072::1909736::INSTR'
        if serialnumber in str(ctypes.c_char_p(resourceName.raw).value):
            powermeter.open(resourceName)
            print('-----')
            print(powermeter)
            print('-----')
            print('Powermeter: ' + str(powermeter) + ' opened')
            # <ThorLabsMotors.PowerMeter.TLPM object at 0x0000027A391360A0>
            return powermeter

def close_powermeter(powermeter):
    '''
    Description
    -----------
          Close the powermeter.

    Parameters
    ----------
    powermeter : class
        Python object of the powermeter
    '''
    powermeter.close()
    print('Powermeter closed')

def measure_power(powermeter, unit, wavelength):
    '''
    Read the power in a certain unit and in a definite wavelenght.

    Parameters
    ----------
    powermeter : class
        Python object of the powermeter.
    unit : int
        0 - power measured in Watt
        1 - power measured in dBm
    wavelenght : float
        Wavelenght to use to compute the power from the detected current in nm.

    Returns
    -------
    power : float
        Power read from the powermeter in uW.

    '''
    powermeter.setPowerUnit(unit)
    powermeter.setWavelength(wavelength)
    power = powermeter.measPower()[1]
    return power

def measure_row(powermeter, unit, wavelength):
    powermeter.setPowerUnit(unit)
    powermeter.setWavelength(wavelength)
    power_measurements = []
    times = []
    for count in range(0, 5):
        power = powermeter.measPower()[1]
        # returned value is already c_double().value
        power_measurements.append(power)
        print('-----')
        print(power)
        print(count)
        time.sleep(0.5) # do I need this? for 600 values this takes 300 secs
    print('-----')
    print(power_measurements)

# def makefigure_wpscan(positions, powers):
#     '''
#     Plots the power vs. positions of the data acquired from the waveplate.

#     Parameters
#     ----------
#     positions : list
#         list of positions of the wave plate
#     powers : list
#         list of the corresponding powers

#     Returns
#     -------
#     None.

#     '''
#     pylab.figure()
#     pylab.plot(positions, powers, '.-', label='wp scan ')
#     pylab.legend()
#     # title('Uses PM100USB')
#     pylab.xlabel('Angle (degrees)')
#     pylab.ylabel('Power (uW)')
#     pylab.tight_layout()
#     pylab.tight_layout()
#     pylab.show()

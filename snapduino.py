from pyfirmata import Arduino, util
import snapext
import serial.tools.list_ports

for i in serial.tools.list_ports.comports():
	if i[2][12:16] == '2341':
		a = Arduino(i[0])
	else:
		pass
it = util.Iterator(a)
it.start()
analog_report = []
handler = snapext.SnapHandler

pin11=a.get_pin('d:11:p')
pin10=a.get_pin('d:10:p')
pin9=a.get_pin('d:9:p')
pin6=a.get_pin('d:6:p')
pin5=a.get_pin('d:5:p')
pin3=a.get_pin('d:3:p')
pwms = {11: pin11, 10: pin10, 9: pin9, 6: pin6, 5: pin6, 3: pin3}

@handler.route('/digitalwrite')
def digitalwrite(setting, pin):
	a.digital[pin].write(setting)

@handler.route('/digitalpwm')
def digitalpwm(setting, pin):
	pwms.get(pin).write(setting)

@handler.route('/digitalread')
def digitalread(pin):
	a.digital[pin].read()

@handler.route('/analogread')
def analogwrite(pin):
	if not pin in analog_report:
		a.analog[pin].enable_reporting()
	return a.analog[pin].read()

snapext.main(handler, 8282)

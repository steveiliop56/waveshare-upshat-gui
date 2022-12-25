from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import ina219 as s
import threading
import time
import os

ina219 = s.INA219(addr=0x42)

powershut = 10

def get_stats():
    global bus_voltage, shunt_voltage, current, power, p
    while True:
        bus_voltage = ina219.getBusVoltage_V()
        shunt_voltage = ina219.getShuntVoltage_mV() / 1000
        current = ina219.getCurrent_mA()
        power = ina219.getPower_W()
        p = (bus_voltage - 6)/2.4*100
        if(p > 100):p = 100
        if(p < 0):p = 0
      
thread = threading.Thread(target=get_stats)
thread.daemon = True
thread.start()

def setpowerlimit():
  global powershut
  while True:
    powershut = powershut
    batpower = float("{:3.1f}".format(p))
    if batpower <= powershut:
      print("Shutting down in 5 seconds!")
      time.sleep(5)
      os.system("sudo poweroff")
      

thread = threading.Thread(target=setpowerlimit)
thread.daemon = True
thread.start()

# Create your views here.

#def index(request):
#    return render(request, "app/index.html")

def index(request):
  global bus_voltage, power, p, current
  template = loader.get_template('app/index.html')
  context = {
    'voltage': "{:6.3f} V".format(bus_voltage),
    'power': "{:6.3f} W".format(power),
    'percent': "{:3.1f} %".format(p),
    'current': "{:9.6f} A".format(current/1000),
    'powershut': powershut,
  }
  return HttpResponse(template.render(context, request))

def sv(request, value):
  global powershut
  powershut = value
  print("Raspberry pi will shutdown when battery percent is below: " + str(powershut) + "%")
  return HttpResponse(200)
# This server runs on Pi, sends Pi's your 4 arguments from the vcgencmds, sent as Json object.

# details of the Pi's vcgencmds - https://www.tomshardware.com/how-to/raspberry-pi-benchmark-vcgencmd
# more vcgens on Pi 4, https://forums.raspberrypi.com/viewtopic.php?t=245733
# more of these at https://www.nicm.dev/vcgencmd/
# Brendan McBride

import socket
import os, time
import json

s = socket.socket()
host = '10.102.13.210' # Localhost
port = 5000
s.bind((host, port))
s.listen(5)

def pi_temperature():
    # Defines the core temperature from Pi
    t = os.popen('vcgencmd measure_temp').readline()
    return t.strip()

def pi_memoryusage():
    # Defines the memory usage of the ARM processor
    m = os.popen('vcgencmd get_mem arm').readline()
    return m.strip()

def pi_cpuvoltage():
    # Defines the CPU voltage
    cpuv = os.popen('vcgencmd measure_volts').readline()
    return cpuv.strip()
    
while True:
  c, addr = s.accept()
  print ('Got connection from',addr)
  
  # Collects the data from the Pi
  temperature = pi_temperature()
  memory = pi_memoryusage()
  voltage = pi_cpuvoltage()
  
  # JSON object that contains the collected data
  data = {
      "Temperature": temperature,
      "Memory usage": memory,
      "CPU voltage": voltage
  }

  res = bytes(json.dumps(data), 'utf-8') # needs to be a byte
  c.send(res) # sends data as a byte type
  c.close()

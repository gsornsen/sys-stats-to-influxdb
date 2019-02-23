#!/usr/bin/env python
# encoding: utf-8

import re
import subprocess
import time
import json
import sys

def get_cpu_temperature(id):
    cpu_temp = None
    command = ['sensors', id]
    temperatures = subprocess.getoutput(command)
    for match in re.findall("(.*?)\:\s+\+?(.*?)°C", temperatures):
        if 'Package id 0' in match:
            cpu_temp = float(match[1])
            if __debug__:
                print('CPU Temp: {}'.format(cpu_temp))
            break
    return cpu_temp

def get_gpu_temperature():
    gpu_temp = None
    command = subprocess.check_output('nvidia-smi -q -d TEMPERATURE', shell=True)
    temperatures = "".join(map(chr, command)).split('\n')
    for line in temperatures:
        if 'GPU Current Temp' in line:
            match = re.findall("\d{1,3}\sC", line)
            gpu_temp = float(match[0][:-2])
            if __debug__:
                print('GPU Temp: {}'.format(gpu_temp))
            break
    return gpu_temp

def get_temperatures():
    cpu_temperature = get_cpu_temperature('coretemp-isa-0000')
    gpu_temperature = get_gpu_temperature()
    temperature_dict = {
        "CPU_Temp": cpu_temperature,
        "GPU_Temp": gpu_temperature,
    }
    #return json.dumps(temperature_dict)
    return temperature_dict

def main():
    try:
        while True:
            current_temperatures = get_temperatures()
            print(current_temperatures)
            time.sleep(1)
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == '__main__':
    main()
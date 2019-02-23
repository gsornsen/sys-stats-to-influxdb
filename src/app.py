#!/usr/bin/env python
# encoding: utf-8

from util.influxdb_writer import Writer
from util.temperatures import get_cpu_temperature, get_gpu_temperature, get_temperatures
from datetime import datetime
import time
import os
import json
import sys


def main():
    db = 'System-Resources'
    hostname = os.uname()[1]
    while True:
        try:
            current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
            current_temperatures = get_temperatures()
            json_body = [
            {
                "measurement": "System-Resources",
                "tags": {
                    "host": hostname,
                    "location": "home"
                },
                "time": current_time,
                "fields": current_temperatures
            }    
            ]
            data = json.dumps(json_body)
            if __debug__:
                print(data)
            db_writer = Writer()
            db_writer.check_db(db)
            db_writer.write(data, db)
            time.sleep(1)
        except KeyboardInterrupt:
            sys.exit(0)

if __name__ == '__main__':
    main()

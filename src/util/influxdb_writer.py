#!/usr/bin/env python
# encoding: utf-8

from influxdb import InfluxDBClient
from datetime import datetime
import time
import json
import random

class Writer():
    def __init__(self, host='localhost', port=8086, db='test'):
        self.host = host
        self.port = port
        self.db = db
        self.client = InfluxDBClient(host, port, db)

    def check_db(self, db):
        list_of_db_dicts = self.client.get_list_database()
        list_of_dbs = [value.get('name') for value in list_of_db_dicts]
        if db not in list_of_dbs:
            if __debug__:
                print('Creating db: {}'.format(db))
            self.client.create_database(db)

    def write(self, data=None, db='test'):
        self.client.switch_database(db)
        if data is not None:
            try:
                if __debug__:
                    print("Writing data")
                data = json.loads(data)
                self.client.write_points(data)
            except TypeError as e:
                print(e)


def main():
    while True:
        current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
        this_writer = Writer()
        this_writer.check_db('test')
        json_body = [
        {
            "measurement": "cpu_load_short",
            "tags": {
                "host": "server01",
                "region": "us-west"
            },
            "time": current_time,
            "fields": {
                "cpu_load": random.uniform(0.0, 10.0),
            }
        }
        ]
        data = json.dumps(json_body)
        this_writer.write(data, 'test')
        time.sleep(0.5)


if __name__ == '__main__':
    main()

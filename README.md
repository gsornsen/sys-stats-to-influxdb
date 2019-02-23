# sys-stats-to-influxdb
This is a quick python program to inject real-time CPU and GPU temperatures into InfluxDB. The purpose is to have a real-time data going into a time-series database, so I can practice using modern web-based front-ends to visualize real-time data. 

## OS Dependencies

* Nvidia GPU
* Nvidia Drivers
* Ubuntu-like distro
* lm-sensors package
* influxdb package
* influxdb-client package

```bash
$ sudo add-apt-repository ppa:graphics-drivers/ppa
$ sudo apt update
$ sudo apt install lm-sensors influxdb influxdb-client
$ sudo apt purge nvidia-*
$ sudo apt install nvidia-driver-xxx nvidia-kernel-source-xxx nvidia-utils-xxx
```

## Python Dependencies
* influxdb
```bash
$ python3 -m pip install influxdb
```

## How to Run

```bash
$ git clone https://github.com/gsornsen/sys-stats-to-influxdb.git
$ cd sys-stats-to-influxdb/src
$ python3 app.py
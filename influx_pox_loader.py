#!/usr/bin/python3

import os
from datetime import datetime
import serial
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
ORG = os.getenv("ORG")
BUCKET = os.getenv("BUCKET")

client = InfluxDBClient(
    url="https://us-west-2-1.aws.cloud2.influxdata.com", token=TOKEN
)
write_api = client.write_api(write_options=SYNCHRONOUS)

# Serial device mounted at /dev/ttyUSB0 with a 9600 baudrate
ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=1)
sample = []

while True:
    sample = ser.readline().decode("utf-8").split()
    if len(sample) == 12:
        spo2 = sample[3]
        try:
            spo2 = int(spo2.lstrip("SPO2=").rstrip("%"))
        except ValueError:
            continue
        bpm = sample[4]
        try:
            bpm = int(bpm.lstrip("BPM="))
        except ValueError:
            continue
        pii = sample[5]
        try:
            pii = float(pii.lstrip("PI=").rstrip("%"))
        except ValueError:
            continue

        point = (
            Point("spo2")
            .tag("uid", "0001")
            .field("spo2", spo2)
            .field("bpm", bpm)
            .field("perf_index", pii)
            .time(datetime.utcnow(), WritePrecision.NS)
        )

        write_api.write(BUCKET, ORG, point)

    else:
        continue

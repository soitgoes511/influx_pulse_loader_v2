## InfluxDB V2 (Cloud Instance) loader for Masimo Rad-8 Pulse-Oximeter

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This is my current pulse-oximeter loader to an InfluxDB cloud instance. The Influx libraries are different from
my previous version as this sends data to a 2.x version of the database. For version >=1.8, InfluxDB switched
to using Flux as the only query language. Version 1.8 is neutral and can utilize both InfluxQL and Flux.

A dotenv file was used to store my secrets/tokens. To make use of this scripts, you will need:

1. Masimo Rad-8 Pulse-Oximeter (have a Rad-7 and need to test, but have not yet)
2. Ability to capture ASCII from DB9 connection (I use a raspberry pi Zero W)
3. InfluxDB Cloud Instance (Free for 30-day data retention w/ a few other constraints)
⋅⋅1. [InfluxDB AWS Link](https://us-west-2-1.aws.cloud2.influxdata.com/login)

One other difference from my older version is that I am capturing SPO2, BPM & Perfusion Index.
Alarm codes are also available, but I have not parsed nor decoded those. Perhaps someday I will.

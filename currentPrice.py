#!/usr/bin/python3

import influxdb_client
import asyncio
import tibber
from influxdb_client.client.write_api import SYNCHRONOUS

conf = configparser.ConfigParser()
conf.read('config.ini')

client = influxdb_client.InfluxDBClient(
   url=conf["influx"]["url"],
   token=conf["influx"]["token"],
   org=conf["influx"]["org"]
)

write_api = client.write_api(write_options=SYNCHRONOUS)

async def main():
    access_token = conf["tibber"]["token"]
    tibber_connection = tibber.Tibber(access_token)
    await tibber_connection.update_info()
    home = tibber_connection.get_homes()[0]
    await home.update_info()
    await home.update_price_info()

    await tibber_connection.close_connection()
    p = influxdb_client.Point("tibber").field("cost", home.current_price_info["total"])
    write_api.write(bucket=conf["influx"]["bucket"], org=conf["influx"]["org"], record=p)



if __name__ ==  '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
